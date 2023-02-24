# Exo1-s1-r2
def count_words(corpus_list):
    dictionnaire_freq = {}
    for sing_contenu in corpus_list:
        mots = sing_contenu.split()
        for mot in mots:
            if mot in dictionnaire_freq:
                dictionnaire_freq[mot] += 1
            else:
                dictionnaire_freq[mot] = 1
    return dictionnaire_freq
