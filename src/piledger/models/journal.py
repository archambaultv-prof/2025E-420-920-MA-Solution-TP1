import json
from pathlib import Path


class Journal:
    def __init__(self, account_path: Path, txn_path: Path):
        self.account_path = account_path
        self.txn_path = txn_path

    @classmethod
    def load(cls, journal_path: Path) -> "Journal":
        """Lit le fichier journal.json et retourne un objet Journal"""
        with open(journal_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Si les chemins sont relatifs, les convertir en absolus
        account_path = _to_absolute_path(journal_path.parent, Path(data['accounts']))
        txn_path = _to_absolute_path(journal_path.parent, Path(data['transactions']))
        return cls(
            account_path=account_path,
            txn_path=txn_path
        )
    
def _to_absolute_path(base_path: Path, user_path: Path) -> Path:
    """
    Convertit un chemin relatif en chemin absolu basé sur base_path.
    """
    if user_path.is_absolute():
        return user_path
    else:
        return (base_path / user_path).resolve()