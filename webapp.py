from flask import Flask, render_template, request, redirect, url_for
from db import Purchase, PurchaseDatabase
import os

app = Flask(__name__)
db = PurchaseDatabase()


@app.route('/')
def index():
    purchases = db.get_all_purchases()
    return render_template('index.html', purchases=purchases)

@app.route('/add', methods=['GET', 'POST'])
def add_purchase():
    if request.method == 'POST':
        type_of_purchase = request.form['type_of_purchase']
        name = request.form['name']
        price_per_unit = request.form['price_per_unit']
        quantity = request.form['quantity']
        date = request.form['date']
        purchase = Purchase(type_of_purchase, name, price_per_unit, quantity, date)
        db.add_purchase(purchase)
        return redirect(url_for('index'))
    return render_template('form.html', action='add', purchase=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_purchase(id):
    purchase = db.get_purchase(id)
    if not purchase:
        return 'Закупка не найдена', 404
    if request.method == 'POST':
        purchase.type_of_purchase = request.form['type_of_purchase']
        purchase.name = request.form['name']
        purchase.price_per_unit = request.form['price_per_unit']
        purchase.quantity = request.form['quantity']
        purchase.date = request.form['date']
        db.update_purchase(id, purchase)
        return redirect(url_for('index'))
    return render_template('form.html', action='edit', purchase=purchase)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_purchase(id):
    db.delete_purchase(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888) 