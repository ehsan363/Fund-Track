# Importing libraries
import sqlite3
from pathlib import Path

# Database path
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "transactions"

class DBmanager:
    def __init__(self,DB_path):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row # row_factory for better data handling

    # Function for fetching transaction history
    def history(self):
        cursor

    # Function to close SQLite
    def close(self):
        conn.close()