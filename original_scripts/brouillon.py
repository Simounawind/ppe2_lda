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
                    help='la categorie qu\'on veut extraire')                    
                    
args = parser.parse_args()


# Etape 2 : 对于每个文件：找出所有article，以便后续进行过滤，列表中的每个元素就是一个xml里的内容

def lire_XML():
    dir_path = args.dossier_XML
    fichiers_liste = []
    for txtname in os.listdir(dir_path):
        fic = pathlib.Path(dir_path) / txtname
        xml = fic.read_text()   #从而得出每一个txt的内容
    return xml

    # Etape 3 : 对每一个列表的元素：求出其中符合规范的文章，并得出其中的description和title



    # Etape 4 :

    # premier choix : module "re" avec argparse
    # Si le fichier est importé en tant que module, la fonction title_descr peut être appelée directement

def title_descr(xml):
    # 1. trouver chaque article comme un élément dans une liste
    art_pattern = re.compile('<item>.*?</item>')
    art_liste = art_pattern.findall(xml)
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

    # 2. dans chaque article, trouver son titre et description
    for article in art_liste:
        catline_pattern = re.compile(r"<link>(.*?)</link>")
        cat_line = catline_pattern.search(article).group(1)
        cat_pattern = re.compile(r"(\d{4})\.html")
        cat_num = cat_pattern.search(article).group(1)
        if cat_num == cat_cible:




if __name__ == '__main__':
    xml = lire_XML()
    title_descr(xml)

    