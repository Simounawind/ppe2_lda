import re
from pathlib import Path

# Objectif : extraire et afficher le titre et la description de chaque article dans un fichier XML.

# premier choix : module "re" avec argparse
# Si le fichier est importé en tant que module, la fonction title_descr peut être appelée directement


def re_parser(fic):
    fic_path = Path(fic)
    xml = fic_path.read_text()
    # 1. trouver chaque article comme un élément dans une liste
    art_pattern = re.compile('<item>.*?</item>')
    art_liste = art_pattern.findall(xml)
    # 2. dans chaque article, trouver son titre et description
    for article in art_liste:
        tit_pattern = re.compile(r"<title><!\[CDATA\[(.*?)\]\]></title>")
        titre = tit_pattern.search(article).group(1)
        desc_pattern = re.compile(
            r"<description><!\[CDATA\[(.*?)\]\]></description>")
        description = desc_pattern.search(article).group(1)
        yield titre, description
