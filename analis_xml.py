"""
"""

import argparse
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ParseError

xml_tag_count = 0

def analysis_xml(file = None, str_xml = None):
    root = None
    if file != "" and str_xml == "":
        if os.path.isfile(file):
            try:
                passtree = ET.parse(file)
            except ParseError as ex:
                print('File is empty or corupted')
            tree = ET.parse(file)
            root = tree.getroot()
        else:
            print(f"file {file} does not exist")
            return
    elif str_xml != "" and file == "":
        root = ET.fromstring(str_xml)
    else:
        print("""
Set the file using: python analis_xml.py -f {file name}
or set String using:  python analis_xml.py -s {string}
""")
        return

    perf_func(root, max_level)

    print(f"Max depth of xml {file}{str_xml} is {xml_tag_count}")
    

def perf_func(elem, func, level=0):
    func(elem,level)
    for child in elem:
        perf_func(child, func, level+1)

def max_level(elem,level):
    global xml_tag_count
    xml_tag_count = max([level, xml_tag_count])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This application is necessary for analyzing xml files in depth")
    parser.add_argument('-f', '--file', action='store', dest='file', default="")
    parser.add_argument('-s', '--string', action='store', dest='str_xml', default="")
    res = parser.parse_args()
    analysis_xml(res.file,res.str_xml)