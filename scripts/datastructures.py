from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Analyse:
    form: str
    lemma: str
    pos: str


@dataclass
class Article:
    title: str
    desc: str
    date: str
    analyse: List[Analyse]


@dataclass
class Corpus:
    cat: List[str]
    start: str
    end: str
    path: Path
    content: List[Article]


