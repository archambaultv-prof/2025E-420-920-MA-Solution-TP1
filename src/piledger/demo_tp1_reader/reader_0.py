import csv
from typing import Iterator

# Marina
VALID_TYPES = {"actif", "passif", "revenu", "dépense", "capitaux propres"}

def iter_accounts(path: str) -> Iterator[tuple[str, str]]:
    """Itérateur qui retourne (nom_compte, type) ligne par ligne"""
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"].strip()
            typ = row["type"].strip()
            if typ not in VALID_TYPES:
                 raise ValueError(f"Type invalide pour le compte {row['name']}: {row['type']}. "
                                  f"Types valides: {', '.join(VALID_TYPES)}")
            yield name, typ