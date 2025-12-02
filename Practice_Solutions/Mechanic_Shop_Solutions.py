from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, select
from flask_marshmallow import Marshmallow
from typing import List

# ==========================================
# MOCK SETUP (For demonstration purposes)
# In a real app, these would be in models.py, extensions.py, etc.
# ==========================================

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
ma = Marshmallow()

# --- Models ---

class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    phone: Mapped[str] = mapped_column(String(20))
    
    tickets: Mapped[List["Ticket"]] = relationship("Ticket", back_populates="customer")

class Mechanic(Base):
    __tablename__ = 'mechanics'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    specialty: Mapped[str] = mapped_column(String(100))
    
    tickets: Mapped[List["Ticket"]] = relationship("Ticket", back_populates="mechanic")

class Ticket(Base):
    __tablename__ = 'tickets'
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(50)) # e.g., "Open", "Completed"
    
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    customer: Mapped["Customer"] = relationship("Customer", back_populates="tickets")
    
    mechanic_id: Mapped[int] = mapped_column(ForeignKey('mechanics.id'))
    mechanic: Mapped["Mechanic"] = relationship("Mechanic", back_populates="tickets")

# --- Schemas ---

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

class MechanicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic

class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket
        include_fk = True

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
mechanic_schema = MechanicSchema()
ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

# ==========================================
# ASSIGNMENT SOLUTIONS
# ==========================================

mechanic_shop_bp = Blueprint('mechanic_shop_bp', __name__)

# ---------------------------------------------------------
# Task 1.1: Route to search customer by their email
# ---------------------------------------------------------
@mechanic_shop_bp.route('/customers/search', methods=['GET'])
def search_customer_by_email():
    """
    Finds a single customer by email.
    Usage: GET /customers/search?email=john@example.com
    """
    email = request.args.get('email')
    
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    # Using SQLAlchemy 2.0 select syntax
    # .scalar_one_or_none() returns the object or None, raising error if multiple found (unlikely with unique=True)
    query = select(Customer).where(Customer.email == email)
    customer = db.session.execute(query).scalar_one_or_none()

    if customer:
        return customer_schema.jsonify(customer), 200
    else:
        return jsonify({"message": "Customer not found"}), 404


# ---------------------------------------------------------
# Task 1.2: Route to find which mechanic worked on the most tickets
# ---------------------------------------------------------
@mechanic_shop_bp.route('/mechanics/analytics/top-performer', methods=['GET'])
def get_top_mechanic():
    """
    Identifies the mechanic with the highest number of associated tickets.
    Uses Python-side sorting for logic clarity (as seen in Library API examples).
    """
    # 1. Get all mechanics
    mechanics = db.session.query(Mechanic).all()

    if not mechanics:
        return jsonify({"message": "No mechanics found"}), 404

    # 2. Sort based on the length of the 'tickets' relationship
    # reverse=True means descending order (highest first)
    mechanics.sort(key=lambda mech: len(mech.tickets), reverse=True)

    top_mechanic = mechanics[0]
    ticket_count = len(top_mechanic.tickets)

    # 3. Return the result with metadata
    return jsonify({
        "mechanic": mechanic_schema.dump(top_mechanic),
        "total_tickets_completed": ticket_count,
        "ranking": "Top Performer"
    }), 200


# ---------------------------------------------------------
# Task 1.3: Turn the get_tickets route into a paginated route
# ---------------------------------------------------------
@mechanic_shop_bp.route('/tickets', methods=['GET'])
def get_tickets_paginated():
    """
    Returns a paginated list of tickets.
    Usage: GET /tickets?page=1&per_page=10
    """
    try:
        # 1. Get parameters with defaults
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        # 2. Create the base query
        query = select(Ticket)
        
        # 3. Use Flask-SQLAlchemy's paginate method
        # This returns a Pagination object
        pagination = db.paginate(query, page=page, per_page=per_page, error_out=False)
        
        # 4. Extract the items (list of Ticket objects)
        tickets = pagination.items
        
        # 5. Construct a rich response with metadata
        return jsonify({
            "tickets": tickets_schema.dump(tickets),
            "meta": {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total_pages": pagination.pages,
                "total_items": pagination.total
            }
        }), 200

    except ValueError:
        return jsonify({"error": "Invalid pagination parameters"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
