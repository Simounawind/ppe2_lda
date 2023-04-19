
import spacy
import trankit
import stanza


def create_parser():
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
