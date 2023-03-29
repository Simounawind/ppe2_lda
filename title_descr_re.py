import re
import pathlib
import argparse


# Objectif : extraire et afficher le titre et la description de chaque article dans un fichier XML.

# premier choix : module "re" avec argparse
# Si le fichier est importé en tant que module, la fonction title_descr peut être appelée directement

def title_descr(xml):
    # 1. trouver chaque article comme un élément dans une liste
    art_pattern = re.compile('<item>.*?</item>')
    art_liste = art_pattern.findall(xml)
    # 2. dans chaque article, trouver son titre et description
    for article in art_liste:
        tit_pattern = re.compile(r"<title><!\[CDATA\[(.*?)\]\]></title>")
        titre = tit_pattern.search(article).group(1)
        print("---Titre : ",titre)
        desc_pattern = re.compile(r"<description><!\[CDATA\[(.*?)\]\]></description>")
        description = desc_pattern.search(article).group(1)
        print("---Description : ",description)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description= "le script sert à extraire et afficher le titre et la description de chaque article dans un fichier XML")
    parser.add_argument('chemin_xml', type=str,
                        help='le chemin du fichier xml')
    args = parser.parse_args()
    fic = pathlib.Path(args.chemin_xml)
    xml = fic.read_text()
    title_descr(xml)
