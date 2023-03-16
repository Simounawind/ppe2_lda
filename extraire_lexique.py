import os
import sys
import glob
import argparse

# r1
parser = argparse.ArgumentParser(
    description="Obtenir un argument par bash command, un argument qui indique le chemin des fichiers")
parser.add_argument('chemin', type=str, nargs='*',
                    help='le chemin relatif des fichiers', default=[])
args = parser.parse_args()


def construit_liste_de_chaines(corpus_path):
    list_contenu = []
    for txtname in (corpus_path):
        with open(txtname, 'r') as file:
            data = file.read()
            list_contenu.append(data)
    return list_contenu


# r2
def r2():
    for txtname in sys.stdin:
        fo = open("combined.txt", "a")
        fo.write(txtname)
        fo.close
    files = glob.glob("exercices/S1/Corpus/*.txt")
    num_lines_list = []

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            # Open each file and count the number of lines in each file
            num_lines_list.append(len(lines))
    with open('combined.txt', 'r') as f:
        lines = f.readlines()
    # Loop through the lines of the combined file and split them into separate files
    list_contenu = []
    line_number = 0
    for i, n in enumerate(num_lines_list):
        content = ''
        for j in range(line_number, line_number+n):
            content += lines[j]
        list_contenu.append(content)
        line_number += n
    return list_contenu


# r3
def r3():
    list_contenu = []
    for txtname in sys.stdin:
        txtname = txtname.replace('\n', '')
        with open(txtname, 'r') as file:
            data = file.read()
            list_contenu.append(data)
    return list_contenu


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


jugement = sys.stdin


def lexique(*chemin):
    liste_gros = []
    argnum = sys.argv
    if len(argnum) == 1:  # 说明是没有argperser的
        print("no argsperser")
        a = 0
        for i in jugement:
            a += 1
        print(a)
        if a > 30:
            print("a =", a)
            print("we choose r2 to input the files, because of cat")
            liste_gros = r2()
        else:
            print("a =", a)
            print("we choose r3 to input the files, because of ls")
            liste_gros = r2()

    elif len(argnum) > 1:
        print("files enter with an argument \'chemin\'")
        # r1
        liste_gros = construit_liste_de_chaines(*chemin)
        print(len(liste_gros))

    dict_freq = count_words(liste_gros)
    dict_occurence = doc_freq(liste_gros)
    len_liste_final = len(dict_freq)
    print("\n\n\n\n=====================Tableau du lexique============================\n\n")
    for i in range(len_liste_final):
        key = list(dict_freq)[i]
        value1 = list(dict_freq.values())[i]
        value2 = list(dict_occurence.values())[i]
        print("{0:^10}|{1:^10}|{2:^10}".format(key, value1, value2))


if __name__ == '__main__':
    lexique(args.chemin)
