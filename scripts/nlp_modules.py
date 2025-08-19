# arsenal of NLP modules
import spacy
import trankit
import stanza


def trankit_parser():
    return trankit.Pipeline('french', gpu=False)


def trankit_analyse(parser, text: str):
    desc_analyse = {}
    fr_output = parser.posdep(text)
    lemma_doc = parser.lemmatize(text)
    for x in lemma_doc.get('sentences'):
        for token in x.get('tokens'):
            analyse_contenu = []
            analyse_contenu.append(token.get('lemma'))
            for y in fr_output.get('sentences'):
                for token2 in y.get('tokens'):
                    if token2.get('text') == token.get('text'):
                        analyse_contenu.append(token2.get('upos'))
            desc_analyse[token.get('text')] = analyse_contenu
    return desc_analyse


def spacy_parser():
    return spacy.load("fr_core_news_sm")


def spacy_analyse(parser, text: str):
    doc = parser(text)
    desc_analyse = {}
    for token in doc:
        analyse_contenu = []
        analyse_contenu.append(token.lemma_)
        analyse_contenu.append(token.pos_)
        desc_analyse[token.text] = analyse_contenu
    return desc_analyse


def stanza_parser():
    return stanza.Pipeline('fr')


def stanza_analyse(parser, text: str):
    doc = parser(text)
    desc_analyse = {}
    for sent in doc.sentences:
        for word in sent.words:
            analyse_contenu = []
            analyse_contenu.append(word.lemma)
            analyse_contenu.append(word.upos)
            desc_analyse[word.text] = analyse_contenu
    return desc_analyse
