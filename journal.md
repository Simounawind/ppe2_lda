# PPE2-Projet_LCD



## Membres

- Yingzi LIU

- Danyel KANLIBICAK

- Xiaohua CUI



## Journal

### 2023.02.01

**Danyel :** Creation de compte de gitlab et fait des premier exercise pour connaitre les commands gitlab. Et puis j'ai ajouté SSH Key to Gitlab Account. 


**Xiaohua :** J'ai créé le compte sur gitlab, j'ai travaillé avec le groupe pour créer le dépôt de notre projet, et on a enfin les branches `main`, `page`, ainsi qu'une branche individuelle `xiaohua`. Voici le [dépôt du projet](https://gitlab.com/ppe2023/ppe2_lcd).

---

### 2023.02.04

**Yingzi :** En suivant les consignes données dans TP1 et avec l'aide des membres du groupe, j'ai créé des branches séparées à partir de la branche racine pour déposer les dump textes du corpus, le script python, le journal du bord, et après que tous les membres aient terminé TP1ex1 et fusionné entre eux, j'ai ajouté le tag nommé ex1fin à la version finale de TP1ex1.

---

### 2023.02.06

**Yingzi :** Après avoir pratiqué le changement et la fusion entre les différentes branches, je me suis familiarisé avec ces opérations et j'ai commencé à travailler sur ex2r1, où j'ai d'abord importé le module os, qui fournit un ensemble très riche de méthodes pour travailler avec les fichiers et les répertoires.

Dans le script python, j'ai tout abord définir une fonction qui construit une liste de chaînes de caractères en lisant le contenu de tous les fichiers texte dans un répertoire spécifié. Cette fonction définit le chemin du répertoire contenant les fichiers texte à lire, qui est './exercices/S1/Corpus/'. Ensuite, elle initialise une liste vide appelée 'list_contenu' qui sera remplie avec le contenu des fichiers texte. La boucle for parcourt tous les noms de fichiers dans le répertoire spécifié à l'aide de la fonction 'os.listdir'. Pour chaque nom de fichier, la fonction 'open' est utilisée pour ouvrir le fichier en mode lecture ('r') et le contenu du fichier est lu avec la méthode 'read'. Le contenu est ensuite ajouté à la liste 'list_contenu'.

Finalement, ma fonction retourne la liste 'list_contenu' qui contient toutes les chaînes de caractères correspondant au contenu des fichiers texte dans le répertoire spécifié.

En gros, l'idée c'est que je voudrais cette fonction permet de lire le contenu de plusieurs fichiers texte dans un répertoire spécifié et de stocker le contenu dans une liste de chaînes de caractères pour les membres de mon groupe puissent l'utiliser dans les exo r2 et r3.

A la fin de cet exercice, j'ai ajouté le tag pour mon exercice nommé ex2r1, et j'ai laissé mon groupe terminer les exercices r2 et r3 avant de faire git merge.

---

### 2023.02.08

**Yingzi :** Aujourd'hui, après avoir suivi le cours sur les principes de nomination des branches, j'ai retravaillé les noms des branches et organisé le contenu dans chaque branche.

**Xiaohua :** Depuis le dernier cours, j'ai appris les commandes et les principes de git comme `merge`, `checkout`, `branch`, etc. Aussi j'ai réussi à finir les exercices sur les 4 sites de git graphiques sur iCampus. Avec les efforts des membres de notre groupe, j'ai fini le TD1 et ai crée des branches correspondants. On est encore en train de mettre en pratique les opérations de git et on se sent de plus en plus à l'aise quant aux opérations et gestions de notre dépôt.

---

### 2023.02.12

**Danyel  :** Après avoir ajoutés les fichiers Turc, j'ai ajouté mon script contenant une fonction prenant comme argument une liste de chaîne et retournant un dictionnaire associant chaque mot au nombre de document dans lequel il apparaît.

---

### 2023.02.15

**Xiaohua :** En classe, on m'a dit que je dois segmenter le contenu chinois avec jieba. Enfin j'ai suivi les conseils du professeur et j'ai remplacé le corpus dans la branche `xiaohua` par 10 fichiers texte chinois qui avaient déjà été segmentés. J'ai mis à jour la branche `xiaohua` et l'ai reétiqueter. Aussi les autres membres du groupe ont à nouveau pull et merge ces nouveaux fichiers chinois. Après avoir résolu ce problème, j'ai fait à nouveau le merge des autres deux fonctions.

**Yingzi :** Les membres de notre groupe ont eu un désaccord lors de la fusion de nos scripts respectifs, nous sommes toujours en train de les modifier, j'ai constaté que lorsque je fusionne le script r3, mes scripts disparaissent complètement (les parties qui ne sont pas en conflit sont également manquantes), je ne sais pas quelle en est la raison, ce problème doit encore être résolu.

---

### 2023.02.16

**Xiaohua :** Chacun a fait sa fonction. Donc Ex2 de S1 (Extraction du lexique en python) enfin fini. Réussi à affichier le lexique sous forme de trois colonnes. `mot  | mot_freq | mot_occurence `. Les autres ont aussi réussi à le afficher avec leur script, et le mien est fusionné vers la branche `main`, commit id:[8b2c1ceb](https://gitlab.com/ppe2023/ppe2_lcd/-/commit/8b2c1ceb73fdf6d63f07426bed3e4fa789331911). Et un tag [s1ex2fin](https://gitlab.com/ppe2023/ppe2_lcd/-/tags/s1ex2fin) est crée et est envoyé vers le remote origin.

---

### 2023.02.17

**Xiaohua :** Rename des tags selon le nouveau pdf.

**Xiaohua :** Début des exercices S2, commençant par la création d'une nouvelle branche [XC-s2](https://gitlab.com/ppe2023/ppe2_lcd/-/tree/XC-s2). Avant le changement du groupe, j'avais trouvé qu'on a pas remarqué une défaute pendant la fusion des 3 fonctions (je remarquais que la longueur des deux dictionnaires de `r2` et `r3` est différente, ce qui m'empêche de continuer le TD2)

---

### 2023.02.18

**Xiaohua :** Basés sur les indications de TP1, j'ai vérifié encore une fois le type du résultat de chaque fonction, et avec le nouveau script de `s1ex2r3`, j'ai généré deux dictionnaires de longueur similaire et ai ainsi créé le lexique complet du corpus.

**Xiaohua :** ex1r1 du TD2 fini (les resultats des autres membres restent à merge), tag [XC-s3-e1](https://gitlab.com/ppe2023/ppe2_lcd/-/tags/XC-s3-e1) étiquitté.

**Xiaohua :** Journal enregistré dans [XC-p-s2](https://gitlab.com/ppe2023/ppe2_lcd/-/tree/XC-p-s2), fusionné vers la branche `page`.

**Yingzi :**  Nous nous sommes référés au script donné par les profs et j'ai trouvé que la partie de ma r1 était fondamentalement la même idée que celle donnée par les profs et qu'aucun changement n'était nécessaire, j'ai fini par garder le script que j'avais écrit auparavant, version tag ex2r1. Ensuite, après que le membre de mon équipe ait modifié son script, j'ai fusionné le leur, puis j'ai apporté des modifications au script du prof après que les trois scripts aient été combinés.

---

### 2023.02.19

**Yingzi :**
TP2 exo1-r3 terminée. Dans mon script, l'idée est de construire une liste de chaînes de caractères à partir du contenu de plusieurs fichiers, en lisant les noms des fichiers à partir de l'entrée standard. Pour cela, j'ai importé le module sys(evoqué en cours). Pour chaque nom de fichier, il ouvre le fichier et lit son contenu dans une chaîne de caractères. Ensuite, il ajoute cette chaîne à une liste appelée list_contenu.
Finalement, la fonction construit_liste_de_chaines() renvoie la liste complète de chaînes de caractères, contenant le contenu de tous les fichiers lus. En fait, cela renvoie le même résultat que exo2-r1 dans TP1.
A la fin de cet exercice, je lui ai ajouté la tag YL-s3-e1.

---

### 2023.02.20

**Yingzi :** 

TP2 exo1-r2 terminée. Pour réaliser cette partie, j'ai d'abord écrit un script bash pour enlever les retours à la ligne de tous les fichiers dans le répertoire “Corpus"(“Corpus” est copié à partir du corpus précédent créé par TP1).

Dans le script bash：
`cd Corpus`: change le répertoire de travail actuel en "Corpus".
`for file in *`: itère sur tous les fichiers dans le répertoire courant.
`tr -d '\n' < "$file" > "$file.tmp" `: supprime tous les retours à la ligne de chaque fichier et les redirige vers un fichier temporaire $file.tmp.
`echo >> "$file.tmp"`: ajoute une nouvelle ligne à la fin du fichier temporaire.
`mv "$file.tmp" "$file"`: renomme le fichier temporaire en écrasant le fichier d'origine.

Ainsi, tous les fichiers dans le répertoire “Corpus" auront été modifiés pour avoir une seule ligne sans aucun retour à la ligne, mais avec une nouvelle ligne à la fin.

J'ai ensuite fait une modification du script python de TP1 similaire à celui de TP2 r3, l'idée est de lire les lignes de chaque fichier du "Corpus" depuis l'entrée standard (`stdin`) et de les stocker dans une liste de chaînes de caractères.

---

### 2023.02.21

**Yingzi :** 

Après avoir fusionné r1 dans ma branche YL-s2, j'ai rajouté du code pour comibner les trois options r1, r2 et r3. En gros, le programme final que j'ai écrit peut être appelé avec des arguments de ligne de commande spécifiant les chemins des fichiers, ou il peut être utilisé en mode interactif, où les noms de fichiers sont fournis sur l'entrée standard.

La première partie du code définie un analyseur d'arguments de ligne de commande utilisant le module argparse pour récupérer les chemins des fichiers( Cette partie était réalisée par Xiaohua).

J'ai combiné le cas r2 et r3 dans la deuxième partie du code. Cette partie définit une fonction pour construire une liste de chaînes de caractères à partir des fichiers texte. Cette fonction prend en compte deux cas différents :

Cas r1 : si l'argument chemin est spécifié à partir de la ligne de commande, les fichiers texte sont lus à partir des chemins spécifiés.
Cas r2 et r3 : si aucun argument chemin n'est spécifié, les noms de fichiers sont lus à partir de l'entrée standard. Dans ce cas, la fonction vérifie si chaque nom de fichier se termine par l'extension ".txt". Si oui, elle lit le contenu du fichier correspondant. Sinon, elle considère que le nom de fichier est lui-même une chaîne de caractères à inclure dans la liste.

La partie suivante est ce que nous avons fait dans TP1.

Enfin, la dernière fonction construit le lexique final en imprimant les résultats dans un format de tableau lisible. Elle utilise les dictionnaires construits précédemment pour calculer la fréquence et la fréquence de document pour chaque mot, et les imprime dans un format tabulaire.

**Le problème que j'ai rencontré**: dans l'exo r1 le argument "chemin" est obligatoire et j'essaie de le rendre optionnel, mais finalement quand je lance le programme dans le terminal je dois ajouter un script bash pour traiter le fichier：
`python extraire_lexique.py --chemin Corpus/*.txt`
ce n'est pas la même command suggerée dans les consignes pour TP2 r1:
`python extraire_lexique.py --chemin Corpus/*.txt`
Je ne sais pas comment résoudre ce problème.

---