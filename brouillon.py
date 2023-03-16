import re
import pathlib

fic = pathlib.Path("sample.xml")
xml = fic.read_text()


# re.findall(pattern,string,flags=0)


# re.findall()
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。






l = re.findall(r""_)
titre = re.findall(r"<title>.*?</title>",l[12])
for article in l :
    print(re.findall(r"<title>.*?</title>",article))



pathlib
etree
re
...






# etree

import xml.etree.ElementTree as ET
tree = ET.parse('sample.xml')
root = tree.getroot()

tree.

channel = root.find('channel')

item = channel.find('item')

