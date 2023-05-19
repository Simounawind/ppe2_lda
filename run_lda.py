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




def load_file_xml(xml_file, type, pos=[]):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # corpus
    corpus = []
    for analyse in root.iter('analyse'):
        single_article = []
        for token in analyse.iter('token'):
            if pos == []:
                token_1 = token.get(type)  
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


def bigram(docs):
    bigram = Phrases(docs, min_count=10)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                # Token is a bigram, add to document.
                docs[idx].append(token)
    return docs


def filter_extremes(docs):
    dictionary = Dictionary(docs)
    dictionary.filter_extremes(no_below=5, no_above=0.9)
    return dictionary



def doc2bow(docs, dictionary):
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    return corpus

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


def topic_coherence(model, corpus, num_topics=20):
    top_topics = model.top_topics(corpus)
    avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)
    pprint(top_topics)
    return avg_topic_coherence, top_topics


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
