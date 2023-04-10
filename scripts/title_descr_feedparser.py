import feedparser
import argparse

def feedparser_parser(xml_file):
    # Lecture du contenu du fichier XML avec feedparser
    feed = feedparser.parse(xml_file)
    # Extraction du titre et de la description de chaque article
    for entry in feed.entries:
        yield entry.title, entry.summary
if __name__ == "__main__":
    # Définition des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Extraire le titre et la description de chaque article d'un fichier XML")
    parser.add_argument("xml_file", type=str, help="Chemin du fichier XML à traiter")
    args = parser.parse_args()

    # Extraction du titre et de la description de chaque article du fichier XML
    extract_title_description(args.xml_file)