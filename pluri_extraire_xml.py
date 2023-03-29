import pathlib
import argparse
from title_descr_etree import title_descr


# Objectif : parcourir les fichiers et, extraire et afficher le titre et la description de chaque article correspondant à une catégorie

# Etape 1 : obtenir les fichiers d'après l'input
parser = argparse.ArgumentParser(
    description="le script sert à extraire et afficher le titre et la description de chaque article dans un fichier XML")
parser.add_argument('root', type=str,
                    help='le dossier root qui contient des dossiers/fichiers xml')

parser.add_argument('--date', type=str,
                    help='le dossier root qui contient des dossiers/fichiers xml')

parser.add_argument('--cat', type=str,
                    help='le dossier root qui contient des dossiers/fichiers xml')
args = parser.parse_args()


# Etape 2 : filtrer les fichiers selon les exigences, répondant aux critères suivants  :
# 1. les fichiers sont au format XML
# 2. les fichiers XML comme "fil1646762506-v1.xml" doivent être exclus.
# 3. les fichiers sont de bonne date et de bonne catégorie.

# La fonction dessous renvoie une liste qui contient le chemin des fichiers xml qu'on veut trouver.
def fichiers_pf():
    # créer une dictionnaire pour lier les strings aux codes.
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
    dossier_racine = pathlib.Path(args.root)
    selected_paths = []
    for folder_path in dossier_racine.glob('**/*'):
        if folder_path.is_file() and folder_path.suffix == '.xml' and not folder_path.stem.startswith('fil'):
            with open('fichiers.txt', 'a') as f:
                f.write(f'{folder_path}\n')
            path_str = str(str(folder_path))
            if args.date and args.cat:
                cat_nom = args.cat
                cat_cible = cat_dict[cat_nom]
                date_cible = args.date
                if date_cible in path_str:
                    if cat_cible in path_str:
                        selected_paths.append(str(folder_path))
                        with open('fichiers_selected.txt', 'a') as fs:
                            fs.write(f'{folder_path}\n')
            elif args.date:
                date_cible = args.date
                if date_cible in path_str:
                    selected_paths.append(str(folder_path))
            elif args.cat:
                cat_nom = args.cat
                cat_cible = cat_dict[cat_nom]
                if cat_cible in path_str:
                    selected_paths.append(str(folder_path))
            else:
                print('Deux arguments exigés. Aucun argument n\'est défini')
                print(
                    'Reessayer avec au moins un argument sous forme comme \"python xxxx.py --date Mon/21 --cat culture\"')
                break
    return selected_paths


if __name__ == '__main__':
    # ecrire les contenus obtenus dans un nouveau fichier xml:
    with open('xml_filtre.xml', 'a') as d:
        d.write(f'<?xml version="1.0" encoding="UTF-8"?>\n')
        d.write(f'<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/" xmlns:content="http://purl.org/rss/1.0/modules/content/">\n')
        d.write(f'<corpus>\n')

    d.close
    xml_liste = fichiers_pf()
    for xml in xml_liste:
        # La fonction title_descr, fini dans l'exo 1, est appelé ici.
        title_descr(xml)
        title_list, descr_list = title_descr(xml)
        for i in range(len(title_list)):
            t = title_list[i]
            d = descr_list[i]
            with open('xml_filtre.xml', 'a') as d2:
                d2.write(f'<item>')
                d2.write(f'<title>'+t+'</title>')
                d2.write(f'<description>' + d + '</description>')
                d2.write(f'</item>\n')
    with open('xml_filtre.xml', 'a') as d:
        d.write(f'</corpus>\n</rss>')

    # exo 2 fini
