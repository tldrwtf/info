from . import items_bp
from .schemas import item_schema, items_schema, item_descriptions_schema, item_description_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Items, db, ItemDescription

@items_bp.route('/description', methods=['POST'])
def create_item_description():
    try: 
        data = item_description_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_description = ItemDescription(**data)
    db.session.add(new_description)
    db.session.commit()
    return item_description_schema.jsonify(new_description), 201

@items_bp.route('/descriptions', methods=['GET'])
def get_item_descriptions():
    descriptions = db.session.query(ItemDescription).all()
    return item_descriptions_schema.jsonify(descriptions), 200


@items_bp.route('/<int:description_id>', methods=['POST'])
def create_item(description_id):
    
    try: 
        data = item_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_item = Items(description_id=description_id, **data)
    db.session.add(new_item)
    db.session.commit()
    return item_schema.jsonify(new_item), 201

@items_bp.route('', methods=['GET'])
def get_items():
    items = db.session.query(Items).all()
    return items_schema.jsonify(items), 200