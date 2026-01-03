# Importing libraries
import sqlite3
from pathlib import Path
from helper.dateAndTime import tdy

# Database path
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "transactions"

class DBmanager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row # row_factory for better data handling

    def Expense(self):
        today = tdy()
        month = today.strftime('%m')
        year = today.strftime('%Y')

        cursor = self.conn.execute(f'''
            SELECT SUM(amount) AS total_expense
            FROM transactions
            WHERE type = 'expense'
            AND strftime('%Y', date) = '{year}'
            AND strftime('%m', date) = '{month}';''')
        rows = cursor.fetchall()
        if dict(rows[0])['total_expense'] == None:
            totalExpense = 0.00
        else:
            totalExpense = float(f"{dict(rows[0])['total_expense']:.2f}")
        return totalExpense

    # Function for fetching transaction history
    def history(self):
        cursor = self.conn.execute('''
            SELECT category, amount, date, type
            FROM transactions
            ORDER BY date DESC
            LIMIT 10;''')
        rawRows = cursor.fetchall()
        rows = []
        data = []
        for i in rawRows:
            rows.append([dict(i)['category'],f"{dict(i)['amount']:.2f}",dict(i)['date'],dict(i)['type']])

        return rows

    def incomeExpense(self, month, tType):
        today = tdy()
        year = int(today.strftime('%Y'))

        if tType == 'I':
            cursor = self.conn.execute(f'''
                        SELECT SUM(amount) AS total_income
                        FROM transactions
                        WHERE type = 'income'
                        AND strftime('%Y', date) = '{year}'
                        AND strftime('%m', date) = '{month}';''')
            rows = cursor.fetchall()
            if dict(rows[0])['total_income'] == None:
                totalIncome = 0.00
            else:
                totalIncome = float(f"{dict(rows[0])['total_income']}")
            return int(totalIncome)

        elif tType == 'E':
            cursor = self.conn.execute(f'''
                        SELECT SUM(amount) AS total_expense
                        FROM transactions
                        WHERE type = 'expense'
                        AND strftime('%Y', date) = '{year}'
                        AND strftime('%m', date) = '{month}';''')
            rows = cursor.fetchall()
            if dict(rows[0])['total_expense'] == None:
                totalExpense = 0.00
            else:
                totalExpense = float(f"{dict(rows[0])['total_expense']}")
            return int(totalExpense)

    def categories(self, type):
        cursor = self.conn.execute(f'SELECT * FROM CATEGORIES WHERE type = ?;', (type,))
        categoriesFetched = cursor.fetchall()
        categorieList = []
        for row in categoriesFetched:
            categorieList.append(row['name'])
        return categorieList

    def addTransactionToDB(self, amount, IorE, category, date, description, account):
        self.cursor = self.conn.cursor()
        self.cursor.execute('INSERT INTO TRANSACTIONS (amount, type, category, date, description, account) VALUES (?,?,?,?,?,?)', (amount, IorE, category, date, description, account))
        self.conn.commit()
        print('DONE')

    # Function to close SQLite
    def close(self):
        self.conn.close()