from . import orders_bp
from .schemas import order_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Orders, db, Items

#CREATE ORDER
@orders_bp.route('', methods=['POST'])
def create_order():
    try:
        data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_order = Orders(**data)
    db.session.add(new_order)
    db.session.commit()
    return order_schema.jsonify(new_order), 201

# Add item to order
@orders_bp.route('/<int:order_id>/add_item/<int:item_id>', methods=['GET'])
def add_item(order_id, description_id):
    order = db.session.get(Orders, order_id)
    item = db.session.get(Items, description_id)

    if not order or not item:
        return jsonify({"message": "Invalid Order or Item ID"}), 400
    
    if item.order_id:
        return jsonify({"message": "Item already part of an order"}), 400

    order.items.append(item)
    db.session.commit()
    return jsonify({"message": "Item added to order"}), 200

# Checkout an order
@orders_bp.route('/checkout/<int:order_id>', methods=['GET'])
def checkout(order_id):
    order = db.session.get(Orders, order_id)
    
    #loop through the items in the order
    for item in order.items:
        #check if the item is sold
        if item.is_sold:
            return jsonify({"message": "Item is already sold"}), 400
        # mark as sold
        item.is_sold = True
    
    db.session.commit()
    return jsonify({"message": "Order has been placed"}), 200