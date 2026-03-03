'''
This file contains all the functions that controls the database.
These functions are imported and then called by other files when needed.
'''
# Importing modules
import sqlite3
from pathlib import Path

# Importing date related function from another file
from helper.dateAndTime import tdy

# Database path
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "transactions"

class DBmanager:
    '''
    Class that contains all the functions that control the database.
    '''
    def __init__(self):
        '''
        Initialization function.
        '''
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row # row_factory for better data handling

    def Expense(self):
        '''
        Function that returns the total expense of the current month.
        '''
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
        '''
        Function that return the recent 5 transactions in the database.
        '''
        cursor = self.conn.execute('''
            SELECT category, amount, date, type
            FROM transactions
            ORDER BY date DESC
            LIMIT 5;''')
        rawRows = cursor.fetchall()
        rows = []
        data = []
        for i in rawRows:
            rows.append([dict(i)['category'],f"{dict(i)['amount']:.2f}",dict(i)['date'],dict(i)['type']])

        return rows

    def incomeExpense(self, month, tType):
        '''
        Function that returns the total income and expense of each month of an year as per demand.
        The function will take in the variable which will let it know which month's transaction and what type ("Income", "Expense")
        We will fetch the current year by using 'tdy' function and then extracting the year from it.
        Then according to the 'tType', "Income" or "Expense" the data will be fetched from the database and returned.
        '''
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
        '''
        Function to fetch the categories according to transaction type.
        '''
        cursor = self.conn.execute(f'SELECT * FROM CATEGORIES WHERE type = ?;', (type,))
        categoriesFetched = cursor.fetchall()
        categoryList = []
        for row in categoriesFetched:
            categoryList.append(row['name'])
        return categoryList

    def getType(self, selectedIDs):
        '''
        Function to fetch all the available types from the database.
        '''
        for i in selectedIDs:
            cursor = self.conn.execute(f'SELECT TYPE FROM TRANSACTIONS WHERE ID = {int(i)};')
            data = cursor.fetchall()
            for i in data:
                type = i['type']
                return type

    def addTransactionToDB(self, amount, IorE, category, date, description, account):
        '''
        Function to add a transaction into the database.
        '''
        self.cursor = self.conn.cursor()
        self.cursor.execute('INSERT INTO TRANSACTIONS (amount, type, category, date, description, account) VALUES (?,?,?,?,?,?)', (amount, IorE, category, date, description, account))
        self.conn.commit()
        print('DONE')

    def transactionHistory(self, sortedTo):
        '''
        Function to fetch all the transaction history according to sorting option selected or my deafult most recent.
        This function is used only by the history window.
        '''
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
        ''''
        Function that fetches all the transactions according to the window that is calling ("Edit Incomes Window", "Edit Expenses Window") and sort option selected.
        Default one being most recent.
        '''
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
        '''
        Function to delete the selected transaction(s) selected in the edit incomes or edit expenses windows.
        '''
        self.cursor = self.conn.cursor()
        for i in selectedIDs:
            code = self.cursor.execute(f'DELETE FROM TRANSACTIONS WHERE ID = {int(i)};')
            self.conn.commit()

    def changeAmount(self,selectedIDs, newAmount):
        '''
        Function to change the amount of the transaction(s) selected in the edit incomes or edit expenses windows.
        '''
        self.cursor = self.conn.cursor()
        for i in selectedIDs:
            code = self.cursor.execute(f'UPDATE TRANSACTIONS SET AMOUNT = {newAmount} WHERE ID = {int(i)};')
            self.conn.commit()

    def changeType(self, selectedIDs):
        '''
        Function to change the type of the transaction(s) selected in the edit incomes or edit expenses windows.
        '''
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

    def changeCategory(self, selectedIDs, newCategory):
        '''
        Function to change the category of the transaction(s) selected in the edit incomes or edit expenses windows.
        '''
        self.cursor = self.conn.cursor()
        for i in selectedIDs:
            code = self.cursor.execute(f'UPDATE TRANSACTIONS SET CATEGORY = "{newCategory}" WHERE ID = {int(i)};')
            self.conn.commit()

    def changeDate(self, selectedIDs, newDate):
        '''
        Function to change the date of the transaction(s) selected in the edit incomes or edit expenses windows.
        '''
        self.cursor = self.conn.cursor()
        for i in selectedIDs:
            code = self.cursor.execute(f'UPDATE TRANSACTIONS SET DATE = "{newDate}" WHERE ID = {int(i)};')
            self.conn.commit()

    def changeDecription(self, selectedIDs, newDecription):
        self.cursor = self.conn.cursor()
        for i in selectedIDs:
            code = self.cursor.execute(f'UPDATE TRANSACTIONS SET DESCRIPTION = "{newDecription}" WHERE ID = {int(i)};')
            self.conn.commit()

    def ReportData(self, year, month):
        '''
        Function that fetches the data from the database for the creation of the report
        '''
        self.cursor = self.conn.cursor()
        code = self.cursor.execute(f'''SELECT SUM(amount) AS total_income FROM transactions
        WHERE type = 'income'
        AND strftime('%Y-%m', date) = '{year}-{month}';''')
        data = code.fetchall()
        for i in data:
            total_income = i['total_income']

        code = self.cursor.execute('''SELECT category, SUM(amount) AS total_of_category FROM transactions
        WHERE type = 'expense'
        AND strftime('%Y-%m', date) = '2025-12'
        GROUP BY category;''')

        data = code.fetchall()
        categories = []
        for i in data:
            categories.append([i["category"], i['total_of_category']])
        return categories, total_income
    # Function to close SQLite
    def close(self):
        '''
        Function to close the connection to the database.
        '''
        self.conn.close()