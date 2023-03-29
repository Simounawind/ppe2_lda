def gen():
    for i in [1, 2, 3, 4, 5]:
        yield i
    yield "fin"
    return


gen()


time python pluri_extraire_xml.py 2022 - -date Dec/25 - -cat sport+culture+societe | wc - l
