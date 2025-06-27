from datetime import datetime
import sqlite3


class Purchase:
    def __init__(self, type_of_purchase, name, price_per_unit, quantity, date=None):
        self.type_of_purchase = type_of_purchase
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.total_amount = price_per_unit * quantity
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")


class PurchaseDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("purchase.db")
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_of_purchase TEXT NOT NULL,
                name TEXT NOT NULL,
                price_per_unit REAL NOT NULL,
                quantity REAL NOT NULL,
                total_amount REAL NOT NULL,
                date TEXT NOT NULL)
        ''')
        self.conn.commit()

    def add_purchase(self, purchase):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO purchases
            (type_of_purchase, name, price_per_unit, quantity, total_amount, date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''',(
            purchase.type_of_purchase,
            purchase.name,
            purchase.price_per_unit,
            purchase.quantity,
            purchase.total_amount,
            purchase.date
            ))
        self.conn.commit()

    def get_all_purchases(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM purchases")
        return cursor.fetchall()
    
    def search_purchases(self, criteria, value):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM purchases WHERE {criteria} LIKE ?", (f"%{value}%", ))
        return cursor.fetchall()
    
    def update_purchase(self, id, purchase):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE purchases
            SET type_of_purchase=?, name=?, price_per_unit=?, quantity=?, total_amount=?, date=?
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

    def delete_purchases(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM purchases WHERE id=?", (id,))
        self.conn.commit()

