###################################### Partie r2
import sys
def construit_liste_de_chaines_r2():
    list_contenu = []
    for line in sys.stdin:
        list_contenu.append(line)
    return list_contenu

# construit_liste_de_chaines()
print(construit_liste_de_chaines_r2())

######################################

def count_words(corpus_list):
    dictionnaire_freq = {}
    for sing_contenu in corpus_list:
        mots = sing_contenu.split()
        for mot in mots:
            if mot in dictionnaire_freq:
                dictionnaire_freq[mot] += 1
            else:
                dictionnaire_freq[mot] = 1
    return dictionnaire_freq


def doc_freq(corpus):
    nb_doc = {}
    for doc in corpus:
        words = set(doc.split())
        for word in words:
            if word in nb_doc:
                nb_doc[word] += 1
            else:
                nb_doc[word] = 1
    return nb_doc


def lexique():
    liste_gros = construit_liste_de_chaines()
    dict_freq = count_words(liste_gros)
    dict_occurence = doc_freq(liste_gros)
    len_liste_final = len(dict_freq)
    for i in range(len_liste_final):
        key = list(dict_freq)[i]
        value1 = list(dict_freq.values())[i]
        value2 = list(dict_occurence.values())[i]
        print("{0:^20}|{1:^20}|{2:^20}".format(key, value1, value2))


# lexique()

