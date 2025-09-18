from pathlib import Path

from piledger.csv_utils import csv_generator
from piledger.models.account import Account

def accounts_generator(path: Path):
    """
    Générateur qui lit un fichier CSV de comptes.
    """
    for row in csv_generator(path):
        id = int(row["id"])
        name = row["name"].strip()
        account_type = row["type"].strip()
        yield Account(id, name, account_type)