
# Code de Sébastien
import csv
from typing import Iterator


class AccountReader():
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self) -> Iterator[dict[str,object]]:
        with open(self.file_path, newline='', encoding='utf-8') as f:
            reader= csv.DictReader(f)
            required_fields = {'id', 'name', 'type'}
            if not reader.fieldnames:
                raise ValueError (f"Erreur: le fichier est vide ou sans en-tête (fichier: {self.file_path})")
            if not required_fields.issubset(reader.fieldnames):
                raise ValueError (f"Erreur: colonnes manquantes dans accounts.csv (attendues: {required_fields}).Trouvé: {reader.fieldnames} (fichier: {self.file_path})")
            for line in reader:
                   yield{"id": line["id"], "name": line["name"], "type": line["type"].strip()}

reader = AccountReader("path/to/accounts.csv")

for account in reader:
    pass