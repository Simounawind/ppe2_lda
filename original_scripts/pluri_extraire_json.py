from title_descr_re import re_parser
from title_descr_etree import etree_parser
from title_descr_feedparser import feedparser_parser
import re
from xml.etree import ElementTree as et
import argparse
import sys
from typing import Optional, List, Dict
from datetime import date
from pathlib import Path
import json  

# Objectif : parcourir les fichiers et, extraire et afficher le titre et la description de chaque article correspondant à une catégorie
MONTHS = ["Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec"]

DAYS = [f"{x:02}" for x in range(1, 32)]


cat_dict = {
    'une': '0,2-3208,1-0,0',
    'international': '0,2-3210,1-0,0',
    'europe': '0,2-3214,1-0,0',
    'societe': '0,2-3224,1-0,0',
    'idees': '0,2-3232,1-0,0',
    'economie': '0,2-3234,1-0,0',
    'actualite-medias': '0,2-3236,1-0,0',
    'sport': '0,2-3242,1-0,0',
    'planete': '0,2-3244,1-0,0',
    'culture': '0,2-3246,1-0,0',
    'livres': '0,2-3260,1-0,0',
    'cinema': '0,2-3476,1-0,0',
    'voyage': '0,2-3546,1-0,0',
    'technologies': '0,2-651865,1-0,0',
    'politique': '0,57-0,64-823353,0',
    'sciences': 'env_sciences',
}


def convert_month(mon: str) -> int:
    m = MONTHS.index(mon) + 1
    return m


# Etape 2 : filtrer les fichiers selon les exigences, répondant aux critères suivants  :
# 1. les fichiers sont au format XML, placés dans un dossier Corpus/Mmm/JJ/19-00-00/
# 2. les fichiers sont de bonne période et de bonne(s) catégorie(s).
# 3. les fichiers XML comme "fil1646762506-v1.xml" doivent être exclus. Les fichiers attendus doivent avoir leur code de categorie dans leur nom

# La fonction 'parcours_path' prend en entrée un répertoire corpus_dir et plusieurs arguments optionnels
# Elle itère sur chaque fichier XML dans le répertoire et renvoie un générateur qui produit un par un les fichiers XML qui répondent aux critères spécifiés.
def parcours_path(corpus_dir: Path, categories: Optional[List[str]] = None, start_date: Optional[date] = None, end_date: Optional[date] = None):
    if categories is not None and len(categories) > 0:
        # 对于所有在categories列表里的c，我们依次在cat-code里找出其对应的答案
        categories = [cat_dict[c] for c in categories]
    else:
        categories = cat_dict.values()  # on prend tout

    for month_dir in corpus_dir.iterdir():
        if month_dir.name not in MONTHS:
            # on ignore les dossiers qui ne sont pas des mois
            continue  # 跳出这次循环，进行下一个month_dir的判断
        m_num = convert_month(month_dir.name)  # 对于Jan,我们将其对应到数字形式 m_num = 1
        for day_dir in month_dir.iterdir():
            if day_dir.name not in DAYS:
                # on ignore les dossiers qui ne sont pas des jours    2022-07-21  2022-09-13
                continue
            # selon le format "2022-01-25",on 生成对应的date对象
            d = date.fromisoformat(f"2022-{m_num:02}-{day_dir.name}")
            if (start_date is None or start_date <= d) and (end_date is None or end_date >= d):  # 保证该日期符合在开始和结束日期之间。
                for time_dir in day_dir.iterdir():
                    if re.match(r"\d\d-\d\d-\d\d", time_dir.name):  # 对应19-00-00
                        for fic in time_dir.iterdir():
                            # 进一步过滤xml文件的名称
                            if fic.name.endswith(".xml") and any([c in fic.name for c in categories]):
                                # un générateur qui produit un par un les fichiers XML qui répondent aux critères spécifiés.
                                yield(fic)


if __name__ == "__main__":
    # Etape 1 : obtenir les fichiers d'après l'input
    parser = argparse.ArgumentParser(
        description="le script sert à extraire et afficher le titre et la description de chaque article dans un fichier XML")
    parser.add_argument(
        "-m", help="méthode de parsing (etree ou re)", default="etree")
    parser.add_argument(
        "-s", help="start date (iso format)", default="2022-06-15")
    parser.add_argument("-e", help="end date (iso format)",
                        default="2022-09-01")
    parser.add_argument("-o", help="output file (stdout if not specified")
    parser.add_argument(
        "corpus_dir", help="root dir of the corpus data,qui contient des dossiers/fichiers xml")
    parser.add_argument("categories", nargs="*",
                        help="la ou les catégories des fichiers XML désirés")
    args = parser.parse_args()
    if args.m == 'etree':
        fonc = etree_parser
        print("vous avez choisi etree pour parser")
    elif args.m == 're':
        fonc = re_parser
        print("vous avez choisi re pour parser")
    elif args.m == 'feedparser':
        fonc = feedparser_parser
        print("vous avez choisi feedparser pour parser")
    else:
        print("méthode non disponible", file=sys.stderr)
        sys.exit()
    # f = un fichier xml, obtenu par yield, soit le "yield(fic)"

    if 'xml' in args.o:     # ecrire les contenus obtenus dans un nouveau fichier xml
        print('parsing already done, outputed in the file you required')
        with open(args.o, 'a') as a:
            a.write(f'<?xml version="1.0" encoding="UTF-8"?>\n')
            a.write(f'<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/" xmlns:content="http://purl.org/rss/1.0/modules/content/">\n')
            a.write(f'<corpus>\n')
        for f in parcours_path(Path(args.corpus_dir),
                               start_date=date.fromisoformat(args.s),
                               end_date=date.fromisoformat(args.e),
                               categories=args.categories):
            # print("#######", f, "##########")  # 打印返回值
            # fonc, soit etree, soit re, renvoie le titre et la description du fichier xml traité
            for title, desc in fonc(f):
                if title and desc is not None:
                    print(f"desc: {desc}")
                    with open(args.o, 'a') as d:
                        d.write(f'<item>')
                        d.write(f'<title>'+title+'</title>')
                        d.write(f'<description>' + desc + '</description>')
                        d.write(f'</item>\n')
        with open(args.o, 'a') as c:
            c.write(f'</corpus>\n</rss>')
    elif 'json' in args.o:
        output_json = []
        for f in parcours_path(Path(args.corpus_dir),
                               start_date=date.fromisoformat(args.s),
                               end_date=date.fromisoformat(args.e),
                               categories=args.categories):
            for title, desc in fonc(f):
                if title and desc is not None:
                    print(f"desc: {desc}")
                    output_json.append({'title': title, 'description': desc})
        with open(args.o, 'w') as d:
            d.write(json.dumps(output_json))
    else:
        for f in parcours_path(Path(args.corpus_dir),
                               start_date=date.fromisoformat(args.s),
                               end_date=date.fromisoformat(args.e),
                               categories=args.categories):
            for title, desc in fonc(f):
                if title and desc is not None:
                    print(">>> Titre:", title)
                    print(">>> Description:", desc)
                    print(
                        '------------------------------------------------------------------------------------------------------------------------------')

    # exo 2bis fini
