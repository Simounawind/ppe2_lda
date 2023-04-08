
import spacy
import trankit
import stanza
from trankit import Pipeline
import json


fr_nlp = stanza.Pipeline('fr')

en_doc = fr_nlp(
    "Barack Obama was born in Hawaii.  He was elected president in 2008.")
# print(en_doc)

print("---------------------------------------------    -   -   ")
p = Pipeline('french')
txt = "Bon, je sais pas ce que est lui."
fr_output = p.posdep(txt)
lemmatized_doc = p.lemmatize(txt)
# print(fr_output)
# print(lemmatized_doc)
# for i in lemmatized_doc.get('sentences'):
#     for token in i.get('tokens'):
#         print(token.get('text'), token.get('lemma'))

# print("###############################################")
desc_analyse = {}
for x in lemmatized_doc.get('sentences'):
    for token in x.get('tokens'):
        analyse_contenu = []
        analyse_contenu.append(token.get('lemma'))
        for y in fr_output.get('sentences'):
            for token2 in y.get('tokens'):
                if token2.get('text') == token.get('text'):
                    analyse_contenu.append(token2.get('upos'))
        desc_analyse[token.get('text')] = analyse_contenu
print(desc_analyse)

# analyse = Analyse(trankit_analyse[0]) form lemma pos
