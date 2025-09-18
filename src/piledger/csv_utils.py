import csv
from pathlib import Path


def csv_generator(file_path: Path):
    """
    Générateur qui lit un fichier CSV et retourne chaque ligne sous forme de dictionnaire.
    """
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row