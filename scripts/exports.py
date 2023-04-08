import json
from dataclasses import asdict
from xml.etree import ElementTree as ET
from datastructures import Corpus, Article, Analyse


# fonction pour sortir les données de dataclasses en json
def write_json(corpus: Corpus, destination: str):
    with open(destination, "w", encoding='utf-8') as fout:
        json.dump(asdict(corpus), fout, ensure_ascii=False, indent=2)

# fonction pour sortir les données de dataclasses en xml


def article_to_xml(article: Article) -> ET.Element:
    xml_article = ET.Element("article")
    xml_article.attrib['date'] = article.date
    title = ET.SubElement(xml_article, "title")
    description = ET.SubElement(xml_article, "description")
    analyses = ET.SubElement(xml_article, "analyse")
    for analyse in article.analyse:
        token = ET.SubElement(analyses, "token")
        token.attrib['form'] = analyse.form
        if analyse.pos and analyse.lemma is not None:
            token.attrib['lemma'] = analyse.lemma
            token.attrib['pos'] = analyse.pos
        else:
            token.attrib['lemma'] = "null"
            token.attrib['pos'] = "null"
            print(
                f"Attention: l'analyse pos du mot '{analyse.form}' renvoie null, skipping...")
    title.text = article.title
    description.text = article.desc
    return xml_article


# fonction pour sortir les données de dataclasses en xml


def write_xml(corpus: Corpus, destination: str):
    root = ET.Element("corpus")
    root.attrib['start'] = corpus.start
    root.attrib['end'] = corpus.end
    root.attrib['categorie'] = corpus.cat
    # content = ET.SubElement(root, "content")
    for article in corpus.content:
        art_xml = article_to_xml(article)
        root.append(art_xml)
        # content.append(art_xml)
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write(destination, encoding='utf-8', xml_declaration=True)


# <corpus> <article> <title> </title> <description> </description> </article> <article> <title> </title> <description> </description> </article> </corpus>
