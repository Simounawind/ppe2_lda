import feedparser
import argparse
from datetime import datetime
import xml.etree.ElementTree as ET

def is_entry_category(entry, category):
    category_dict= {"une": "3208","international": "3210","europe": "3214","societe": "3224","idees": "3232","economie": "3234","actualite-medias": "3236","sport": "3242","planete": "3244","culture": "3246","livres": "3260","cinema": "3476","voyage": "3546","technologies": "651865","politique": "823353","sciences": "env_sciences"}
    
    # category: idees -> 3232
    # entry.link: https://www.lemonde.fr/idees/article/2022/09/23/clio-ce-que-les-etudes-animales-apportent-a-l-histoire-du-genre_6142893_3232.html
    # -> 3232
    last_underscore = entry.link.rfind("_")

    # 使用切片获取下划线和 .html 之间的子字符串
    substring = entry.link[last_underscore + 1:entry.link.rfind(".html")] # 3232
    if category_dict[category] == substring:
        return True
    return False  
    # if category == entry.link:
    #     return True
    return True
def is_entry_date(entry, date):
    # date: 2022-01-01
    # pubDate: Fri, 23 Sep 2022 16:19:18 +0200
    date = datetime.strptime(date, "%Y-%m-%d")
    pubDate = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    if date.date() == pubDate.date():
        return True
    return False

def extract_title_description(xml_file, category, date, output):
    # # Lecture du contenu du fichier XML avec feedparser
    feed = feedparser.parse(xml_file)
    # Extraction du titre et de la description de chaque article
    root = ET.Element("articles")
    for entry in feed.entries:
        if is_entry_date(entry, date) and is_entry_category(entry, category):
            article = ET.SubElement(root, "article")
            ET.SubElement(article, "title").text = entry.title
            ET.SubElement(article, "description").text = entry.summary
            ET.SubElement(article, "pubDate").text = entry.published
            ET.SubElement(article, "category").text = category

    # Write the XML file to disk
    tree = ET.ElementTree(root)
    tree.write(output) 

if __name__ == "__main__":
    # Définition des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Extraire le titre et la description de chaque article d'un fichier XML")
    parser.add_argument("xml_file", type=str, help="Chemin du fichier XML à traiter")
    parser.add_argument("--category", type=str, help="Catégorie à filtrer (ex: sport)")
    parser.add_argument("--date", type=str, help="Date à filtrer (ex: 2022-01-01)")
    parser.add_argument("--output", type=str, help="Nom du fichier XML de sortie")

    args = parser.parse_args()
    # Extraction du titre et de la description de chaque article du fichier XML
    extract_title_description(args.xml_file, args.category, args.date, args.output)