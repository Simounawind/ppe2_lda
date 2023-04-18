import pickle

from datastructures import Corpus, Article

def write_pickle(corpus:Corpus, destination:str):
    with open(destination, "w") as f:
        pickle.dump(corpus, f)
