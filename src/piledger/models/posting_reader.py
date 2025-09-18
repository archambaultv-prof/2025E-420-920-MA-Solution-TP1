from pathlib import Path
from datetime import date

from piledger.csv_utils import csv_generator
from piledger.models.account import Account
from piledger.models.posting import Posting

def postings_generator(path: Path, accounts: dict[str, Account]):
    """
    Générateur qui lit un fichier CSV de postes comptables.
    """
    # id,date,compte,montant
    for row in csv_generator(path):
        id = int(row["id"])
        dt = date.fromisoformat(row["date"])
        account_name = row["compte"]
        try:
            account = accounts[account_name]
        except KeyError:
            raise ValueError(f"Compte inconnu: {account_name}")
        amount = float(row["montant"])
        yield Posting(id, dt, account, amount)