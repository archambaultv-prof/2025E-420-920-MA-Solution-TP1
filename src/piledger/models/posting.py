from datetime import date

from piledger.models.account import Account

class Posting:
    def __init__(self, posting_id: int, date: date, account: Account, amount: float):
        self.posting_id = posting_id
        self.date = date
        self.account = account
        self.amount = amount