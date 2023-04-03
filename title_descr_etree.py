import xml.etree.ElementTree as ET


# Objectif : extraire et afficher le titre et la description de chaque article dans un fichier XML.

# deuxieme choix : module "etree" avec argparse
# Si le fichier est importé en tant que module, la fonction title_descr peut être appelée directement
def etree_parser(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    for article in root.findall(".//item"):
        title = article.find('title').text
        description = article.find('description').text
        yield title, description

