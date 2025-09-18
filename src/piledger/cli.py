# Command Line Interface

from pathlib import Path
import sys
from piledger.models.journal import Journal

def main():
    # Asma
    """Point d'entrée du programme PiLedger."""
    if "--help" in sys.argv or len(sys.argv) < 3:
        print("Usage : piledger [check|balancesheet|incomestatement] path/to/journal.json")
        print("\nExemples :")
        print("  piledger check data/journal.json")
        print("  piledger balancesheet data/journal.json")
        print("  piledger incomestatement data/journal.json")
        sys.exit(0)

    cmd = sys.argv[1]
    journal = Journal.load(Path(sys.argv[2]))

    if cmd == "check":
        print("Vérification des transactions...")
    else:
        print(f"Commande inconnue : {cmd}")
        sys.exit(1)