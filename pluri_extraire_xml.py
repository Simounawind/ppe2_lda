import re
import pathlib
import argparse
import os


# Objectif : parcourir les fichiers et, extraire et afficher le titre et la description de chaque article correspondant à une catégorie

# Etape 1 : obtenir les fichiers d'après l'input
parser = argparse.ArgumentParser(
    description="le script sert à extraire et afficher le titre et la description de chaque article dans un fichier XML")
parser.add_argument('dossier_XML', type=str,
                    help='le chemin du dossier qui contient des fichiers xml')
parser.add_argument('categorie', type=str,
                    help='la categorie des articles')
args = parser.parse_args()


# Etape 2 : 对于每个文件：找出所有article，以便后续进行过滤，列表中的每个元素就是一个xml里的内容

def lire_XML():
    dir_path = args.dossier_XML
    fichiers_liste = []
    for txtname in os.listdir(dir_path):
        fic = pathlib.Path(dir_path) / txtname
        xml = fic.read_text()  # 从而得出每一个txt的内容
        fichiers_liste.append(xml)
    return fichiers_liste


# Selectionner les articles convenables (selon la date et la categrie)
def filtrer(xml_liste):
    liste_filtre = []
    art_pattern = re.compile('<item>.*?</item>')
    cat_dict = {
        'une': 3208,
        'international': 3210,
        'europe': 3214,
        'societe': 3224,
        'idees': 3232,
        'economie': 3234,
        'actualite-medias': 3236,
        'sport': 3242,
        'planete': 3244,
        'culture': 3246,
        'livres': 3260,
        'cinema': 3476,
        'voyage': 3546,
        'technologies': 651865,
        'politique': 823353,
    }
    cat_nom = args.categorie
    cat_cible = cat_dict[cat_nom]
    for xml in xml_liste:
        # 1. trouver chaque article comme un élément dans une liste
        art_liste = art_pattern.findall(xml)
        # for article in art_liste:
        # dateline_pattern = re.compile(r"<pubDate>(.*?)</pubDate>")
        # date_line = catline_pattern.search(article).group(1)
        # date_pattern = re.compile(r"(\d{4})\.html")
        # cat_num = int(cat_pattern.search(article).group(1))
        # if cat_num == cat_cible:
        #     liste_filtre.append(article)

        # 2. dans chaque article, trouver les infos exactes sur la ligne de categorie et ses numéros (comme "3232" pour idees)
        for article in art_liste:
            catline_pattern = re.compile(r"<link>(.*?)</link>")
            cat_line = catline_pattern.search(article).group(1)
            cat_pattern = re.compile(r"(\d{4})\.html")
            cat_num = int(cat_pattern.search(article).group(1))
            if cat_num == cat_cible:
                liste_filtre.append(article)
    return liste_filtre, cat_nom


# fonctions pour extraire titre et description des articles pertinenets
def title_descr(filtre_liste):
    with open('sortie.txt', 'a') as f:
        f.write("Catégorie : " + cat_num + "\n")
        f.write("########################################" + "\n")
    for article in filtre_liste:
        tit_pattern = re.compile(r"<title><!\[CDATA\[(.*?)\]\]></title>")
        titre = tit_pattern.search(article).group(1)
        print("---Titre : ", titre)
        desc_pattern = re.compile(
            r"<description><!\[CDATA\[(.*?)\]\]></description>")
        description = desc_pattern.search(article).group(1)
        print("---Description : ", description)
        with open('sortie.txt', 'a') as f:
            f.write("Titre:" + titre + "\n")
            f.write("Description:" + description + "\n")
            f.write("-------------------" + "\n")


if __name__ == '__main__':
    xml = lire_XML()
    filtre_liste, cat_num = filtrer(xml)
    title_descr(filtre_liste)
