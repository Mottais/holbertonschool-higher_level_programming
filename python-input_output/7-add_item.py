#!/usr/bin/python3
"""function that load list from file then add args in list and save it"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        liste_tampon = load_from_json_file("add_item.json")
    except Exception:
        liste_tampon = []
    for i in range(1, len(argv)):
        liste_tampon.append(argv[i])
    save_to_json_file(liste_tampon, "add_item.json")
