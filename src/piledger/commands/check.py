from pathlib import Path
from piledger.models.account import Account
from piledger.models.journal import Journal
from piledger.models.account_reader import accounts_generator
from piledger.models.posting_reader import postings_generator

def check_command(journal: Journal) -> None:
    """
    Vérifie l'intégrité des comptes et des transactions dans le journal.
    """

    # Puisque les comptes doivent être chargés avant les transactions,
    # on transforme le générateur en liste. Toutefois, cette transformation
    # vérifie quand même les comptes un par un de manière paresseuse.
    accounts = list(check_accounts_generator(journal))
    accounts_dict = {acc.name: acc for acc in accounts}
    check_transactions_generator(journal, accounts_dict)

    # Si on arrive ici, tout est valide
    print("Vérification réussie : toutes les transactions et comptes sont valides.")

def check_accounts_generator(journal: Journal):
    """
    Générateur qui vérifie les comptes un par un et l'unicité des IDs.
    """
    seen_ids = set()
    for account in accounts_generator(journal.account_path):
        if account.account_id in seen_ids:
            raise ValueError(f"ID de compte dupliqué: {account.account_id}")
        seen_ids.add(account.account_id)
        yield account

def check_transactions_generator(journal: Journal, accounts: dict[str, Account]) -> None:
    """
    Vérifie les transactions une par une.
    """
    for txn in group_postings_by_transaction(journal.txn_path, accounts):
        total = sum(posting.amount for posting in txn)
        if abs(total) > 0.001:
            raise ValueError(f"Transaction {txn[0].posting_id} non équilibrée. Le total est {total}")

def group_postings_by_transaction(txn_path: Path, accounts: dict[str, Account]):
    """
    Générateur qui regroupe les postings par transaction.
    Suppose que les postings sont triés par ID de transaction.
    """
    current_txn_id = None
    current_transaction = []
    seen_txn_ids = set()

    for posting in postings_generator(txn_path, accounts):
        # Vérification si on change de transaction
        if posting.posting_id != current_txn_id:
            # On peut émettre la transaction courante avant de commencer une nouvelle.
            if current_txn_id is not None:
                yield current_transaction
            
            current_txn_id = posting.posting_id
            current_transaction = [posting]

            if current_txn_id in seen_txn_ids:
                raise ValueError(f"ID de transaction dupliqué: {current_txn_id}")
            seen_txn_ids.add(current_txn_id)
        else:
            # Même transaction, on ajoute le posting courant
            current_transaction.append(posting)

    # Il est possible qu'il reste une transaction à émettre
    if current_txn_id is not None:
        yield current_transaction