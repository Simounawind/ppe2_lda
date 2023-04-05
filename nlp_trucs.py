
import spacy
import trankit
import stanza
from trankit import Pipeline


fr_nlp = stanza.Pipeline('fr')

en_doc = fr_nlp(
    "Barack Obama was born in Hawaii.  He was elected president in 2008.")
print(en_doc)

print("---------------------------------------------    -   -   ")
p = Pipeline('french')
fr_output = p.posdep(
    '''On pourra toujours parler à propos d'Averroès de "décentrement du Sujet".''')
print(fr_output)
