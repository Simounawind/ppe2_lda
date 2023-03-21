import feedparser
import argparse

def extract_title_description(xml_file):
    # Lecture du contenu du fichier XML avec feedparser
    feed = feedparser.parse(xml_file)
    print("Titre : ", feed.feed.title)
    print("Description : ", feed.feed.subtitle)
    # Extraction du titre et de la description de chaque article
    
    for entry in feed.entries:
        print("Titre : ", entry.title)
        print("Description : ", entry.summary)
        print("\n")

if __name__ == "__main__":
    # Définition des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Extraire le titre et la description de chaque article d'un fichier XML")
    parser.add_argument("xml_file", type=str, help="Chemin du fichier XML à traiter")
    args = parser.parse_args()

    # Extraction du titre et de la description de chaque article du fichier XML
    extract_title_description(args.xml_file)