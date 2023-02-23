# PPE2-Projet_lac

## Membres

- Yingzi LIU

- Danyel KANLIBICAK

- Xiaohua CUI



## Journal





### 2023.02.01

**Xiaohua :** J'ai créé le compte sur gitlab, j'ai travaillé avec le groupe pour créer le dépôt de notre projet, et on a enfin les branches `main`, `page`, ainsi qu'une branche individuelle `xiaohua`. Voici le [dépôt du projet](https://gitlab.com/ppe2023/ppe2_lcd).



---





### 2023.02.04

**Yingzi :** En suivant les consignes données dans TP1 et avec l'aide des membres du groupe, j'ai créé des branches séparées à partir de la branche racine pour déposer les dump textes du corpus, le script python, le journal du bord, et après que tous les membres aient terminé TP1ex1 et fusionné entre eux, j'ai ajouté le tag nommé ex1fin à la version finale de TP1ex1.


***

### 2023.02.06

**Yingzi :** Après avoir pratiqué le changement et la fusion entre les différentes branches, je me suis familiarisé avec ces opérations et j'ai commencé à travailler sur ex2r1, où j'ai d'abord importé le module os, qui fournit un ensemble très riche de méthodes pour travailler avec les fichiers et les répertoires. 

Dans le script python, j'ai tout abord définir une fonction qui construit une liste de chaînes de caractères en lisant le contenu de tous les fichiers texte dans un répertoire spécifié. Cette fonction définit le chemin du répertoire contenant les fichiers texte à lire, qui est './exercices/S1/Corpus/'. Ensuite, elle initialise une liste vide appelée 'list_contenu' qui sera remplie avec le contenu des fichiers texte. La boucle for parcourt tous les noms de fichiers dans le répertoire spécifié à l'aide de la fonction 'os.listdir'. Pour chaque nom de fichier, la fonction 'open' est utilisée pour ouvrir le fichier en mode lecture ('r') et le contenu du fichier est lu avec la méthode 'read'. Le contenu est ensuite ajouté à la liste 'list_contenu'.

Finalement, ma fonction retourne la liste 'list_contenu' qui contient toutes les chaînes de caractères correspondant au contenu des fichiers texte dans le répertoire spécifié.

En gros, l'idée c'est que je voudrais cette fonction permet de lire le contenu de plusieurs fichiers texte dans un répertoire spécifié et de stocker le contenu dans une liste de chaînes de caractères pour les membres de mon groupe puissent l'utiliser dans les exo r2 et r3.

A la fin de cet exercice, j'ai ajouté le tag pour mon exercice nommé ex2r1, et j'ai laissé mon groupe terminer les exercices r2 et r3 avant de faire git merge.

***


### 2023.02.08

**Yingzi :** Aujourd'hui, après avoir suivi le cours sur les principes de nomination des branches, j'ai retravaillé les noms des branches et organisé le contenu dans chaque branche.



**Xiaohua :** Depuis le dernier cours, j'ai appris les commandes et les principes de git comme `merge`, `checkout`, `branch`, etc. Aussi j'ai réussi à finir les exercices sur les 4 sites de git graphiques sur iCampus. Avec les efforts des membres de notre groupe, j'ai fini le TD1 et ai crée des branches correspondants. On est encore en train de mettre en pratique les opérations de git et on se sent de plus en plus à l'aise quant aux opérations et gestions de notre dépôt.

***

### 2023.02.