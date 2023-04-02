import xml.etree.ElementTree as ET
import argparse

def extract_mes_titres_et_desc(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    channel = root.find('channel')

    if channel is not None:
        items = channel.findall('item')

        if items is not None:
            for item in items: 
                title = item.find('title')
                description = item.find('description')
                print(' ------  TITRE ------:', title.text)
                print(' ------   DESCRIPTION--------:', description.text)
                print('----------------------------------------')
                
            return [item.find('title').text for item in items], [item.find('description').text for item in items]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extraction des titres et des descriptions de chaque article dans un fichier XML')
    parser.add_argument('xml_file', type=str, help='Chemin vers le fichier XML')

    args = parser.parse_args()
    xml_file_path = args.xml_file


    extract_mes_titres_et_desc(xml_file_path)
