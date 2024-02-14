#!/usr/bin/python3
"""Definition of read_file function"""


def read_file(filename=""):
    """
    Cette fonction lit un fichier texte spécifié
    et imprime son contenu sur stdout.
    Args:
        filename (str): Le nom du fichier à lire. Par défaut, vide.
    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
        # ou
        # print(file.read(), end="")
