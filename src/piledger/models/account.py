ACCOUNT_TYPES = ["actif", "passif", "capitaux propres", "revenu", "dépense"]


class Account:
    def __init__(self, account_id: int, name: str, account_type: str):
        self.account_id = account_id
        self.name = name
        self.account_type = account_type
        if account_type not in ACCOUNT_TYPES:
            raise ValueError(f"Type de compte invalide: {account_type}")
