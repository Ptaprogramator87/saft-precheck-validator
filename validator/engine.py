from validator.loader import load_xml
from validator.rules import ALL_RULES

def run_validator(xml_path):
    tree = load_xml(xml_path)
    results = []

    for rule in ALL_RULES:
        res = rule(tree)
        if res:
            results.append(res)

    return results
