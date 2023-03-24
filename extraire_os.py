#!/usr/bin/env python3

import os
import argparse

if __name__ == "__main__":
    # Définition des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Extraire le titre et la description de chaque article d'un fichier XML")
    parser.add_argument("directory", type=str, help="Chemin du fichier XML à traiter")
    parser.add_argument("--category", type=str, help="Catégorie à filtrer (ex: sport)")
    parser.add_argument("--date", type=str, help="Date à filtrer (ex: 2022-01-01)")
    parser.add_argument("--output", type=str, help="Nom du fichier XML de sortie")
    args = parser.parse_args()
    # open & read files in a directory
    # Set the directory path
    directory = args.directory
    category = args.category
    date = args.date
    output = args.output

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # if filename.endswith(".txt"):  # Process only files with .txt extension
        filepath = os.path.join(directory, filename)  # Corpus/sample.xml
        # Call extraire.py script and pass the file path as argument
        os.system(f"python extraire_feed_parser.py {filepath} --category {category} --date {date} --output {output}")