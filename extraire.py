import re
import argparse

# Définition des motifs réguliers pour extraire le titre et la description
title_pattern = re.compile(r"<title><!\[CDATA\[(.*?)\]\]></title>")
description_pattern = re.compile(r"<description><!\[CDATA\[(.*?)\]\]></description>")
# title_pattern_2 = re.compile(r"<title>(.*?)</title>")
def extract_title_description(xml_file):
    # Lecture du contenu du fichier XML
    with open(xml_file, "r") as f:
        xml_content = f.read()
    
    # Recherche de chaque article dans le fichier XML
    article_pattern = re.compile(r"<item>.*?</item>", re.DOTALL)
    articles = article_pattern.findall(xml_content)
   

    # Extraction du titre et de la description de chaque article
    for article in articles:
        title_match = title_pattern.search(article)
        if title_match:
            title = title_match.group(1).strip()
            print("Titre : ", title)
        
        description_match = description_pattern.search(article)
        if description_match:
            description = description_match.group(1).strip()
            print("Description : ", description)
        
        print("\n")

if __name__ == "__main__":
    # Définition des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Extraire le titre et la description de chaque article d'un fichier XML")
    parser.add_argument("xml_file", type=str, help="Chemin du fichier XML à traiter")
    args = parser.parse_args()
    
    # Extraction du titre et de la description de chaque article du fichier XML
    extract_title_description(args.xml_file)
