import xml.etree.ElementTree as ET
import argparse


# Objectif : extraire et afficher le titre et la description de chaque article dans un fichier XML.

# deuxieme choix : module "etree" avec argparse
# Si le fichier est importé en tant que module, la fonction title_descr peut être appelée directement
def etree_parser(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    print(root.findall('item'))
    title_list = []
    descr_list = []
    for article in root.findall(".//item"):
        title = article.find('title').text
        description = article.find('description').text
        print("---Titre:", title)
        print("---Description:", description)
        print("------------------------------------------------")
        title_list.append(title)
        descr_list.append(description)
    return title_list, descr_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="le script sert à extraire et afficher le titre et la description de chaque article dans un "
                    "fichier XML")
    parser.add_argument('chemin_xml', type=str,
                        help='le chemin du fichier xml')
    args = parser.parse_args()
    etree_parser(args.chemin_xml)
