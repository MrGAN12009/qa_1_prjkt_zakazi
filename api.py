from flask import Flask, request, jsonify
from db import Purchase, PurchaseDatabase

app = Flask(__name__)
db = PurchaseDatabase()

def purchase_to_dict(p):
    return {
        'id': p.id,
        'type_of_purchase': p.type_of_purchase,
        'name': p.name,
        'price_per_unit': p.price_per_unit,
        'quantity': p.quantity,
        'total_amount': p.total_amount,
        'date': p.date
    }

@app.route('/api/purchases', methods=['GET'])
def get_purchases():
    purchases = db.get_all_purchases()
    return jsonify([purchase_to_dict(p) for p in purchases])

@app.route('/api/purchases/<int:id>', methods=['GET'])
def get_purchase(id):
    p = db.get_purchase(id)
    if not p:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(purchase_to_dict(p))

@app.route('/api/purchases', methods=['POST'])
def add_purchase():
    data = request.json
    required = ['type_of_purchase', 'name', 'price_per_unit', 'quantity', 'date']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing fields'}), 400
    purchase = Purchase(
        data['type_of_purchase'],
        data['name'],
        data['price_per_unit'],
        data['quantity'],
        data['date']
    )
    new_id = db.add_purchase(purchase)
    return jsonify({'id': new_id}), 201

@app.route('/api/purchases/<int:id>', methods=['PUT'])
def update_purchase(id):
    p = db.get_purchase(id)
    if not p:
        return jsonify({'error': 'Not found'}), 404
    data = request.json
    for field in ['type_of_purchase', 'name', 'price_per_unit', 'quantity', 'date']:
        if field in data:
            setattr(p, field, data[field])
    db.update_purchase(id, p)
    return jsonify({'result': 'updated'})

@app.route('/api/purchases/<int:id>', methods=['DELETE'])
def delete_purchase(id):
    p = db.get_purchase(id)
    if not p:
        return jsonify({'error': 'Not found'}), 404
    db.delete_purchase(id)
    return jsonify({'result': 'deleted'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888) 