from title_descr_re import re_parser
from title_descr_etree import etree_parser
import re
from xml.etree import ElementTree as et
import argparse
import sys
from typing import Optional, List, Dict
from datetime import date
from pathlib import Path
import pickle
from datastructures import Corpus, Article, Analyse
from exports import write_json, write_xml
import nlp_modules
from tqdm import tqdm
import gensim_lda_pred as lda


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


def categorie_of_ficname(ficname: str) -> Optional[str]:
    for nom, code in cat_dict.items():
        if code in ficname:
            return nom
    return None


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
                                c = categorie_of_ficname(fic.name)
                                yield(fic, str(d), c)


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
    else:
        print("méthode non disponible", file=sys.stderr)
        sys.exit()
    # f = un fichier xml, obtenu par yield, soit le "yield(fic)"

    # creation du corpus
    tk_parser = nlp_modules.create_parser()
    print('l\'analyse commence, veuillez patienter...')
    corpus = Corpus(args.categories, args.s, args.e, args.corpus_dir, [])
    for f, dt, c in tqdm(parcours_path(Path(args.corpus_dir),
                                       start_date=date.fromisoformat(args.s),
                                       end_date=date.fromisoformat(args.e),
                                       categories=args.categories)):
        for title, desc in tqdm(fonc(f)):
            if title and desc is not None:
                article = Article(title, desc, dt, c, [])
                corpus.content.append(article)
                analyse_dict = nlp_modules.trankit_analyse(
                    tk_parser, title + " " + desc)
                for forme in analyse_dict:
                    token = Analyse(forme, analyse_dict.get(forme)[
                        0], analyse_dict.get(forme)[1])
                    article.analyse.append(token)
     # d'après le format de fichier de sortie, on écrit le résultat dans le fichier correspondant
    if args.o.endswith(".js"):
        print('parsing done, outputed in the file de format json you required')
        write_json(corpus, args.o)

    # output xml
    elif args.o.endswith(".xml"):
        print('parsing done, outputed in the xml file you required')
        write_xml(corpus, args.o)

    elif args.o.endswith(".pickle"):
        print(
            'parsing done, outputed in the file pickle you required, may not that visible')
        with open(args.o, 'wb') as f:
            pickle.dump(corpus, f)
        with open(args.o, 'rb') as r:
            returned_data = pickle.load(r)

    else:
        print('parsing done, outputed in the terminal')
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
# S10: LDA tourner sur les données "en bricolant" le script
    continue_ou_non = input(
        "Do you want to start the LDA topic module ? (y/n): ")
    if continue_ou_non.lower() == 'y':
        use_saved_data = input("Do you want to use saved data? (y/n): ")
        if use_saved_data.lower() == 'y':
            pass
        else:
            pass
# ↑ problem non résolu : je ne sais pas comment lier les deux scripts ensemble, et comment faire pour que le script de LDA puisse utiliser automatiquement les données de ce script.
# Il n'y a pour moi qu'une seule solution, c'est d'utiliser input() pour demander à l'utilisateur de choisir les paramètres pour entraîner le modèle LDA, mais je ne sais pas si c'est une bonne solution.
