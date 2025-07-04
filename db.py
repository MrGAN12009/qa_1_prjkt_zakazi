import sqlite3
from datetime import datetime

class Purchase:
    def __init__(self, type_of_purchase, name, price_per_unit, quantity, date=None, id=None):
        self.id = id
        self.type_of_purchase = type_of_purchase
        self.name = name
        self.price_per_unit = float(price_per_unit)
        self.quantity = float(quantity)
        self.total_amount = self.price_per_unit * self.quantity
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')

class PurchaseDatabase:
    def __init__(self, db_path='purchases.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_of_purchase TEXT NOT NULL,
                name TEXT NOT NULL,
                price_per_unit REAL NOT NULL,
                quantity REAL NOT NULL,
                total_amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_purchase(self, purchase):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO purchases 
            (type_of_purchase, name, price_per_unit, quantity, total_amount, date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            purchase.type_of_purchase,
            purchase.name,
            purchase.price_per_unit,
            purchase.quantity,
            purchase.total_amount,
            purchase.date
        ))
        self.conn.commit()
        return cursor.lastrowid

    def get_all_purchases(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM purchases')
        rows = cursor.fetchall()
        # row = (id, type_of_purchase, name, price_per_unit, quantity, total_amount, date)
        return [Purchase(row[1], row[2], row[3], row[4], row[6], id=row[0]) for row in rows]

    def get_purchase(self, id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM purchases WHERE id=?', (id,))
        row = cursor.fetchone()
        if row:
            return Purchase(row[1], row[2], row[3], row[4], row[6], id=row[0])
        return None

    def search_purchases(self, criteria, value):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT * FROM purchases WHERE {criteria} LIKE ?', (f'%{value}%',))
        rows = cursor.fetchall()
        return [Purchase(row[1], row[2], row[3], row[4], row[6], id=row[0]) for row in rows]

    def update_purchase(self, id, purchase):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE purchases 
            SET type_of_purchase=?, name=?, price_per_unit=?, 
                quantity=?, total_amount=?, date=?
            WHERE id=?
        ''', (
            purchase.type_of_purchase,
            purchase.name,
            purchase.price_per_unit,
            purchase.quantity,
            purchase.total_amount,
            purchase.date,
            id
        ))
        self.conn.commit()

    def delete_purchase(self, id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM purchases WHERE id=?', (id,))
        self.conn.commit() 