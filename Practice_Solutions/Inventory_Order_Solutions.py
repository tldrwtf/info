from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, select, Table, Column

# ==========================================
# MOCK SETUP
# ==========================================

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# --- Models ---

class ItemDescription(Base):
    """Represents the Catalog Entry (e.g., 'The Great Gatsby')"""
    __tablename__ = 'item_descriptions'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(500))
    
    items: Mapped[list["Items"]] = relationship("Items", back_populates="description")

class Items(Base):
    """Represents a Physical Instance (e.g., Copy #42)"""
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(primary_key=True)
    condition: Mapped[str] = mapped_column(String(50))
    
    description_id: Mapped[int] = mapped_column(ForeignKey('item_descriptions.id'))
    description: Mapped["ItemDescription"] = relationship("ItemDescription", back_populates="items")
    
    # For Order Flow
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'), nullable=True)
    order: Mapped["Orders"] = relationship("Orders", back_populates="items")

class Orders(Base):
    """Represents a User's Cart/Transaction"""
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20), default="Pending") # Pending, Completed, Cancelled
    user_id: Mapped[int] = mapped_column(Integer) # Assuming user ID linkage
    
    items: Mapped[list["Items"]] = relationship("Items", back_populates="order")

# ==========================================
# SOLUTION: ADVANCED PATTERNS
# ==========================================

advanced_patterns_bp = Blueprint('advanced_patterns_bp', __name__)

# ---------------------------------------------------------
# Task 2.1: Inventory Tracking (Description vs Instance)
# ---------------------------------------------------------

@advanced_patterns_bp.route('/inventory/catalog', methods=['POST'])
def create_catalog_entry():
    """Creates the generic product definition"""
    data = request.json
    new_desc = ItemDescription(
        title=data['title'],
        description=data.get('description', '')
    )
    db.session.add(new_desc)
    db.session.commit()
    return jsonify({"message": "Catalog entry created", "id": new_desc.id}), 201

@advanced_patterns_bp.route('/inventory/<int:desc_id>/add-stock', methods=['POST'])
def add_stock(desc_id):
    """Adds a physical unit to the inventory for a specific product"""
    data = request.json
    
    # 1. Verify catalog entry exists
    desc = db.session.get(ItemDescription, desc_id)
    if not desc:
        return jsonify({"error": "Catalog entry not found"}), 404
        
    # 2. Create the physical item
    new_item = Items(
        description_id=desc_id,
        condition=data.get('condition', 'New')
    )
    
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify({
        "message": "Stock added", 
        "item_id": new_item.id,
        "product": desc.title
    }), 201


# ---------------------------------------------------------
# Task 2.2: Order Flow Implementation
# ---------------------------------------------------------

@advanced_patterns_bp.route('/orders', methods=['POST'])
def create_order():
    """Step 1: Initialize a new Order (Cart)"""
    user_id = request.json.get('user_id') # In real app, get from token
    
    new_order = Orders(user_id=user_id, status="Pending")
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({"message": "Order started", "order_id": new_order.id}), 201

@advanced_patterns_bp.route('/orders/<int:order_id>/add/<int:item_id>', methods=['POST'])
def add_item_to_order(order_id, item_id):
    """Step 2: Add a specific physical item to the order"""
    
    # 1. Fetch Order and Item
    order = db.session.get(Orders, order_id)
    item = db.session.get(Items, item_id)
    
    if not order or not item:
        return jsonify({"error": "Order or Item not found"}), 404
        
    # 2. Logic Checks
    if order.status != "Pending":
        return jsonify({"error": "Cannot add items to a finalized order"}), 400
        
    if item.order_id is not None:
        return jsonify({"error": "Item is already part of another order"}), 400
        
    # 3. Add to Order
    item.order_id = order.id
    db.session.commit()
    
    return jsonify({"message": "Item added to order"}), 200

@advanced_patterns_bp.route('/orders/<int:order_id>/checkout', methods=['POST'])
def checkout(order_id):
    """Step 3: Finalize the transaction"""
    order = db.session.get(Orders, order_id)
    
    if not order:
        return jsonify({"error": "Order not found"}), 404
        
    if not order.items:
        return jsonify({"error": "Order is empty"}), 400
        
    # 1. Process Payment (Mock)
    payment_successful = True 
    
    if payment_successful:
        # 2. Update Status
        order.status = "Completed"
        db.session.commit()
        return jsonify({"message": "Checkout successful", "status": "Completed"}), 200
    else:
        return jsonify({"error": "Payment failed"}), 402
