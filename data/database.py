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

    def transactionHistory(self, sortedTo):
        self.cursor = self.conn.cursor()
        if sortedTo == 'Date ASC':
            code = self.cursor.execute('SELECT * FROM TRANSACTIONS ORDER BY DATE ASC;')

        elif sortedTo == 'Date DESC':
            code = self.cursor.execute('SELECT * FROM TRANSACTIONS ORDER BY DATE DESC;')

        elif sortedTo == 'Created ASC':
            code = self.cursor.execute('SELECT * FROM TRANSACTIONS ORDER BY CREATED_AT ASC;')

        elif sortedTo == 'Created DESC':
            code = self.cursor.execute('SELECT * FROM TRANSACTIONS ORDER BY CREATED_AT DESC;')

        elif sortedTo == 'Amount H->L':
            code = self.cursor.execute('SELECT * FROM TRANSACTIONS ORDER BY AMOUNT DESC;')

        elif sortedTo == 'Amount L->H':
            code = self.cursor.execute('SELECT * FROM TRANSACTIONS ORDER BY AMOUNT ASC;')

        elif sortedTo == 'Income -> Expense':
            code = self.cursor.execute('SELECT * FROM TRANSACTIONS ORDER BY TYPE DESC;')

        elif sortedTo == 'Expense -> Income':
            code = self.cursor.execute('SELECT * FROM TRANSACTIONS ORDER BY TYPE ASC;')

        self.data = code.fetchall()
        return self.data

    def editingTransactionHistory(self, sortedTo, transactionType):
        self.cursor = self.conn.cursor()
        if sortedTo == 'Date ASC':
            code = self.cursor.execute(f'SELECT * FROM TRANSACTIONS WHERE TYPE = "{transactionType}" ORDER BY DATE ASC;')

        elif sortedTo == 'Date DESC':
            code = self.cursor.execute(f'SELECT * FROM TRANSACTIONS WHERE TYPE = "{transactionType}" ORDER BY DATE DESC;')

        elif sortedTo == 'Created ASC':
            code = self.cursor.execute(f'SELECT * FROM TRANSACTIONS WHERE TYPE = "{transactionType}" ORDER BY CREATED_AT ASC;')

        elif sortedTo == 'Created DESC':
            code = self.cursor.execute(f'SELECT * FROM TRANSACTIONS WHERE TYPE = "{transactionType}" ORDER BY CREATED_AT DESC;')

        elif sortedTo == 'Amount H->L':
            code = self.cursor.execute(f'SELECT * FROM TRANSACTIONS WHERE TYPE = "{transactionType}" ORDER BY AMOUNT DESC;')

        elif sortedTo == 'Amount L->H':
            code = self.cursor.execute(f'SELECT * FROM TRANSACTIONS WHERE TYPE = "{transactionType}" ORDER BY AMOUNT ASC;')

        self.data = code.fetchall()
        return self.data

    def deleteSelected(self, selectedIDs):
        self.cursor = self.conn.cursor()
        for i in selectedIDs:
            code = self.cursor.execute(f'DELETE FROM TRANSACTIONS WHERE ID = {int(i)};')
            self.conn.commit()

    def changeAmount(self,selectedIDs, newAmount):
        self.cursor = self.conn.cursor()
        for i in selectedIDs:
            code = self.cursor.execute(f'UPDATE TRANSACTIONS SET AMOUNT = {newAmount} WHERE ID = {int(i)};')
            self.conn.commit()

    def changeType(self, selectedIDs):
        self.cursor = self.conn.cursor()
        for i in selectedIDs:
            code = self.cursor.execute(f'SELECT TYPE FROM TRANSACTIONS WHERE ID = {int(i)};')
            data = code.fetchall()
            for j in data:
                oldType = j['type']

            if oldType == 'income':
                newType = 'expense'
            else:
                newType = 'income'
            code = self.cursor.execute(f'UPDATE TRANSACTIONS SET TYPE = "{newType}" WHERE ID = {int(i)};')
            self.conn.commit()

    # Function to close SQLite
    def close(self):
        self.conn.close()