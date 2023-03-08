def doc_freq(corpus):
    nb_doc = {}
    for doc in corpus:
        words = set(doc.split())
        for word in words:
            if word in nb_doc:
                nb_doc[word] += 1
            else:
                nb_doc[word] = 1
    return nb_doc
