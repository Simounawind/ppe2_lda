import pickle
from pprint import pprint
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim.models import Phrases
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import smart_open
import tarfile
import re
import os.path
import io
import json
from xml.etree import ElementTree as ET
import argparse
from datastructures import Corpus, Article, Analyse
import logging
import pyLDAvis.gensim_models
import sys
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# 定义一个函数：
# 1. 通过ElementTree来获得xml里的的tokens
# 2.


def load_file_xml(xml_file, type, pos=[]):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # corpus
    corpus = []
    for analyse in root.iter('analyse'):
        single_article = []
        for token in analyse.iter('token'):
            if pos == []:
                token_1 = token.get(type)  # type可能是lemma或者forme
                if token_1 is not None:
                    single_article.append(token_1)
            else:
                if token.get('pos') in pos:
                    token_1 = token.get(type)
                    if token_1 is not None:
                        single_article.append(token_1)
        corpus.append(single_article)
    return corpus


def load_file_json(json_file, type, pos=[]):
    with open(json_file, 'r') as f:
        data = json.load(f)
    corpus = []
    for article in data['content']:
        single_article = []
        for token in article['analyse']:
            if pos == []:
                token_1 = token[type]
                if token_1 is not None:
                    single_article.append(token_1)
            elif token.get('pos') in pos:
                token_1 = token[type]
                if token_1 is not None:
                    single_article.append(token_1)
        corpus.append(single_article)
    return corpus


def load_file_pickle(pickle_file, type, pos=[]):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
    corpus = []
    for article in data.content:
        single_article = []
        for token in article.analyse:
            if pos == []:
                token_1 = token.__getattribute__(type)
                if token_1 is not None:
                    single_article.append(token_1)
            elif token.pos in pos:
                token_1 = token.__getattribute__(type)
                if token_1 is not None:
                    single_article.append(token_1)
        corpus.append(single_article)
    return corpus


# Compute bigrams.
# Add bigrams and trigrams to docs (only ones that appear 20 times or more).
# 为docs添加bigrams和trigrams（只添加出现20次或更多的bigrams和trigrams）

def bigram(docs):
    bigram = Phrases(docs, min_count=10)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                # Token is a bigram, add to document.
                docs[idx].append(token)
    return docs


# bigram是一个Phrases对象，可以用来生成bigrams
# Phrases 函数用来生成bigrams，min_count是指bigrams出现的最小次数
    # 这里的token是一个bigram，比如原文本为 machine learning is not easy, 则遍历生成的bigrams为: machine_learning, learning_is, is_not, not_easy
    # 如果token是一个bigram，就添加到文档中
    # Token is a bigram, add to document.

###############################################################################
# We remove rare words and common words based on their *document frequency*.
# Below we remove words that appear in less than 20 documents or in more than
# 50% of the documents. Consider trying to remove words only based on their
# frequency, or maybe combining that with this approach.
# 我们根据词在文档中的出现频率来去除稀有词和常见词。
# 在下面的代码中，我们去除在20个文档中出现的词或者在50%以上的文档中出现的词。

# Remove rare and common tokens.

# Create a dictionary representation of the documents.

def filter_extremes(docs):
    dictionary = Dictionary(docs)
    dictionary.filter_extremes(no_below=5, no_above=0.9)
    return dictionary


# # Filter out words that occur less than 20 documents, or more than 50% of the documents.
# dictionary.filter_extremes(no_below=20, no_above=0.5)

###############################################################################
# Finally, we transform the documents to a vectorized form. We simply compute
# the frequency of each word, including the bigrams.
# 最后，我们将文档转换为向量化形式。并计算每个单词的频率，包括bigrams的频率

# Bag-of-words representation of the documents.
# 词袋表示法，corpus是一个二维数组，每个元素是一个文档，每个文档是一个二元组，二元组的第一个元素是词的id，第二个元素是词的频率


def doc2bow(docs, dictionary):
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    return corpus

###############################################################################
# Let's see how many tokens and documents we have to train on.
#


###############################################################################
# Training
# 接下来，我们开始训练LDA模型。我们首先讨论如何设置一些训练参数。
# --------
#
# We are ready to train the LDA model. We will first discuss how to set some of
# the training parameters.
#
# 首先，我们需要设置一些训练参数，比如说，我们需要设置多少个主题，每次训练的文档数，训练的轮数等等。
# First of all, the elephant in the room: how many topics do I need? There is
# really no easy answer for this, it will depend on both your data and your
# application. I have used 10 topics here because I wanted to have a few topics
# that I could interpret and "label", and because that turned out to give me
# reasonably good results. You might not need to interpret all your topics, so
# you could use a large number of topics, for example 100.
#
# chunksize 是控制每次训练的文档数，增加chunksize会加快训练速度，至少在文档可以轻松放入内存的情况下。
# 如果chunksize超过了文档的数量，那么就会一次性处理所有的文档。
# chunksize可以影响模型的质量，
# ``chunksize`` controls how many documents are processed at a time in the
# training algorithm. Increasing chunksize will speed up training, at least as
# long as the chunk of documents easily fit into memory. I've set ``chunksize =
# 2000``, which is more than the amount of documents, so I process all the
# data in one go. Chunksize can however influence the quality of the model, as
# discussed in Hoffman and co-authors [2], but the difference was not
# substantial in this case.
#
# ``passes`` controls how often we train the model on the entire corpus.
# Another word for passes might be "epochs". ``iterations`` is somewhat
# technical, but essentially it controls how often we repeat a particular loop
# over each document. It is important to set the number of "passes" and
# "iterations" high enough.
#  ``passes`` 控制了我们对整个语料库训练模型的次数。另一个词可能是“epochs”。
# ``iterations`` 是一个技术性的词，但实际上它控制了我们对每个文档重复特定循环的次数。设置“passes”和“iterations”足够高是很重要的。
# I suggest the following way to choose iterations and passes. First, enable logging (as described in many Gensim tutorials), and set ``eval_every = 1`` in ``LdaModel``. When training the model look for a line in the log that
# looks something like this::
# 我建议你选择iterations和passes的方式如下。首先，启用日志（如许多Gensim教程中所述），并在LdaModel中设置eval_every = 1。训练模型时，查找日志中类似于下面的一行：
# eval_every = 1表示每次训练完一个文档就计算一次模型的困惑度，然后打印出来
#    2016-06-21 15:40:06,753 - gensim.models.ldamodel - DEBUG - 68/1566 documents converged within 400 iterations
#
# If you set ``passes = 20`` you will see this line 20 times. Make sure that by
# the final passes, most of the documents have converged. So you want to choose
# both passes and iterations to be high enough for this to happen.
# 也就是说，如果你设置了passes = 20，那么你会看到这一行20次。确保最后的passes中，大多数文档都收敛了。因此，你需要选择passes和iterations足够高，以便发生这种情况。
#
# We set ``alpha = 'auto'`` and ``eta = 'auto'``. Again this is somewhat
# technical, but essentially we are automatically learning two parameters in
# the model that we usually would have to specify explicitly.
# 我们设置alpha = 'auto'和eta = 'auto'。这也是技术性的，但实际上我们正在自动学习模型中的两个参数，通常我们必须明确指定。

# passes和iterations的区别：
# passes是对整个语料库的训练次数，iterations是对每个文档的训练次数
# Train LDA model.

# Set training parameters.
def train_lda_model(corpus, dictionary, num_topics=20, chunksize=2000, passes=20, iterations=400, eval_every=None):
    # Make a index to word dictionary.
    temp = dictionary[0]  # This is only to "load" the dictionary.
    id2word = dictionary.id2token
    model = LdaModel(
        corpus=corpus,
        id2word=id2word,
        chunksize=chunksize,
        alpha='auto',
        eta='auto',
        iterations=iterations,
        num_topics=num_topics,
        passes=passes,
        eval_every=eval_every
    )
    return model


###############################################################################
# We can compute the topic coherence of each topic. Below we display the
# average topic coherence and print the topics in order of topic coherence.
#
# Note that we use the "Umass" topic coherence measure here (see
# :py:func:`gensim.models.ldamodel.LdaModel.top_topics`), Gensim has recently
# obtained an implementation of the "AKSW" topic coherence measure (see
# accompanying blog post, http://rare-technologies.com/what-is-topic-coherence/).
#
# If you are familiar with the subject of the articles in this dataset, you can
# see that the topics below make a lot of sense. However, they are not without
# flaws. We can see that there is substantial overlap between some topics,
# others are hard to interpret, and most of them have at least some terms that
# seem out of place. If you were able to do better, feel free to share your
# methods on the blog at http://rare-technologies.com/lda-training-tips/ !

def topic_coherence(model, corpus, num_topics=20):
    top_topics = model.top_topics(corpus)
    avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)
    pprint(top_topics)
    return avg_topic_coherence, top_topics

# 这里的top_topics是一个列表，列表中的每个元素是一个元组，元组中的第一个元素是主题的id，第二个元素是主题的相关性


# Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
# 平均主题相关性是所有主题的主题相关性之和，除以主题数。
# 该值越大，说明主题之间的相关性越高


###############################################################################
# Things to experiment with
# -------------------------
#
# * ``no_above`` and ``no_below`` parameters in ``filter_extremes`` method.
# * Adding trigrams or even higher order n-grams.
# * Consider whether using a hold-out set or cross-validation is the way to go for you.
# * Try other datasets.
#
# Where to go from here
# ---------------------
#
# * Check out a RaRe blog post on the AKSW topic coherence measure (http://rare-technologies.com/what-is-topic-coherence/).
# * pyLDAvis (https://pyldavis.readthedocs.io/en/latest/index.html).
# * Read some more Gensim tutorials (https://github.com/RaRe-Technologies/gensim/blob/develop/tutorials.md#tutorials).
# * If you haven't already, read [1] and [2] (see references).
#
# References
# ----------
#
# 1. "Latent Dirichlet Allocation", Blei et al. 2003.
# 2. "Online Learning for Latent Dirichlet Allocation", Hoffman et al. 2010.
#

# if
# # Partie prediction avec le modèle IDA
# docs = load_file(corpus.content)
# docs_bigrams = bigram(docs)
# dictionary = filter_extremes(docs_bigrams)
# doc_bow = doc2bow(docs_bigrams, dictionary)
# lda_model = train_lda_model(doc_bow, dictionary, num_topics=10,
#                             chunksize=2000, passes=20, iterations=400, eval_every=None)
# avg_topic_coherence, top_topics = topic_coherence(
#     lda_model, doc_bow, num_topics=10)
# print('Average topic coherence: %.4f.' % avg_topic_coherence)
# pprint(top_topics)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ce script permet de créer un modèle LDA à partir d'un corpus, et de prédire les topics d'un nouveau document")
    parser.add_argument("-s", help="input file")
    parser.add_argument(
        "-m", choices=['xml', 'json', 'pickle'], help='Type of input file')
    parser.add_argument(
        "-t", help="choisir le lemma ou la forme")
    parser.add_argument(
        "pos", nargs="*", help="determiner les pos (une liste)")
    parser.add_argument("-n", help="num_topics", default=10)
    parser.add_argument("-c", help="chunksize", default=2000)
    parser.add_argument("-p", help="passes", default=20)
    parser.add_argument("-i", help="iterations", default=400)
    args = parser.parse_args()
# ---------------------------------------------------------------------
    if args.s:
        if args.m == 'xml':
            corpus = load_file_xml(args.s, args.t, args.pos)
        elif args.m == 'json':
            corpus = load_file_json(args.s, args.t, args.pos)
        elif args.m == 'pickle':
            corpus = load_file_pickle(args.s, args.t, args.pos)
        else:
            print('Invalid filetype')
            sys.exit(1)
        corpus = [[token for token in doc if not token.isnumeric()]
                  for doc in corpus]
        docs_c = [[token for token in doc if len(token) > 1] for doc in corpus]
        bi_docs = bigram(docs_c)
        dictionnaire = filter_extremes(bi_docs)
        print(dictionnaire)
        doc_bow = doc2bow(bi_docs, dictionnaire)
        print('Number of unique tokens: %d' % len(dictionnaire))
        print('Number of documents: %d' % len(doc_bow))
        num_topics = args.n
        chunksize = args.c
        passes = args.p
        iterations = args.i
        eval_every = None
        model = train_lda_model(
            doc_bow, dictionnaire, num_topics=num_topics, chunksize=chunksize, passes=passes, eval_every=eval_every)
        topic_coherence(model, doc_bow, num_topics=num_topics)
        # nous allons maintenant sauvegarder le modèle sous forme d
        lda_dp = pyLDAvis.gensim_models.prepare(
            model, doc_bow, dictionnaire)
        pyLDAvis.save_html(lda_dp, 'lda_dp.html')
