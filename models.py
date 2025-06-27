import datetime

class Purchase:
    def __init__(self, type_of_purchase, name, price_per_unit, quantity, date=None):
        self.type_of_purchase = type_of_purchase
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")



