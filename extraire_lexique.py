import os

def construit_liste_de_chaines():
    dir_path = './exercices/S1/Corpus/'
    list_contenu = []
    for txtname in os.listdir(dir_path):
        with open(dir_path + txtname, 'r') as file:
            data = file.read()
            list_contenu.append(data)
    return list_contenu
construit_liste_de_chaines()
