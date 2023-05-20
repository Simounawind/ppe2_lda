import pickle
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Analyse:
    forme: str
    lemme: str
    pos: str


@dataclass
class Article:
    titre: str
    description: str
    analyse: List[Token]


@dataclass
class Corpus:
    categories: list[str]
    begin: str
    end: str
    chemin: Path
    articles: list[Article]


a = Article('Breaking News',
            'Donald Trump is now president of the United States')
c = Corpus(['news', 'politics', 'trending'], '2022-01-01',
           '2022-12-31', '../../BDD nanterre', [a])
# 在其他文件中导入这两个数据类，可以用该方法：
# from datastructures import Article
# from datastructures import Corpus

# 通过字典的方式访问数据类的属性
print(asdict(c))
# 产生结果如下：
# {'categories': ['news', 'politics', 'trending'], 'begin': '2022-01-01', 'end': '2022-12-31', 'chemin': '../../BDD nanterre', 'articles': [{'titre': 'Breaking News', 'description': 'Donald Trump is now president of the United States'}]}

# 后续继续向corpus类中添加新文章
a = Article('What a Moment',
            'Joe Biden is now president of the United States')
c.articles.append(a)
c.articles.append(a)
c.articles.append(a)
c.articles.append(a)


def corpus_to_xml(corpus: Corpus, chemin: Path):
    """Convertit un corpus en un fichier XML"""


def corpus_to_json(corpus: Corpus, chemin: Path):
    """Convertit un corpus en un fichier JSON"""


with open('test.pickle', 'wb') as fout:
    pickle.dump(c, fout)

with open('test.pickle', 'rb') as fout:
    c2 = pickle.load(fout)
    print(c2)


# bash指令
