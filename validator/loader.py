from lxml import etree

def load_xml(path: str):
    """
    Încarcă fișierul XML SAF-T și returnează arborele XML
    """
    return etree.parse(path)
