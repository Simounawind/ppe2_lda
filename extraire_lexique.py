import sys
import os

import argparse


# Exo-s2-r1

parser = argparse.ArgumentParser(
    description="Obtenir un argument par bash command, un argument qui indique le chemin des fichiers")
parser.add_argument('chemin', type=str, nargs='+',
                    help='le chemin relatif des fichiers')
args = parser.parse_args()


# r3 , obtenir des données à partir de "ls"


def r3():
    list_contenu = []
    for txtname in sys.stdin:
        txtname = txtname.replace('\n', '')
        with open(txtname, 'r') as file:
            data = file.read()
            list_contenu.append(data)
    return list_contenu


# r3 , obtenir des données à partir de "ls"


def r3():
    list_contenu = []
    for txtname in sys.stdin:
        txtname = txtname.replace('\n', '')
        with open(txtname, 'r') as file:
            data = file.read()
            list_contenu.append(data)
    return list_contenu

# Exo1-s1-r1


def construit_liste_de_chaines(corpus_path):
    list_contenu = []
    for txtname in (corpus_path):
        with open(txtname, 'r') as file:
            data = file.read()
            list_contenu.append(data)
    return list_contenu


# Exo1-s1-r2
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


# Exo1-s1r3
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


# pour afficher
def lexique(chemin):
    liste_gros = construit_liste_de_chaines(chemin)


def lexique():
    liste_gros = r3()
    dict_freq = count_words(liste_gros)
    dict_occurence = doc_freq(liste_gros)
    len_liste_final = len(dict_freq)
    for i in range(len_liste_final):
        key = list(dict_freq)[i]
        value1 = list(dict_freq.values())[i]
        value2 = list(dict_occurence.values())[i]
        print("{0:^20}|{1:^20}|{2:^20}".format(key, value1, value2))


if __name__ == '__main__':
    lexique(args.chemin)
    lexique()  # pour afficher


def lexique():
    liste_gros = r3()
    dict_freq = count_words(liste_gros)
    dict_occurence = doc_freq(liste_gros)
    len_liste_final = len(dict_freq)
    for i in range(len_liste_final):
        key = list(dict_freq)[i]
        value1 = list(dict_freq.values())[i]
        value2 = list(dict_occurence.values())[i]
        print("{0:^20}|{1:^20}|{2:^20}".format(key, value1, value2))


if __name__ == '__main__':
    if __name__ == '__main__':
    lexique(args.chemin)
