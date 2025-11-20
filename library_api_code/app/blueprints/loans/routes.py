from . import loans_bp
from .schemas import loan_schema, loans_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Loans, Books, db
from app.blueprints.books.schemas import books_schema
from app.extensions import limiter

#CREATE LOAN
@loans_bp.route('', methods=['POST'])
def create_loan():
    try:
        data = loan_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_loan = Loans(**data)
    db.session.add(new_loan)
    db.session.commit()
    return loan_schema.jsonify(new_loan) #use jsonify when the schema is return the whole message


#Add book to loan
@loans_bp.route('/<int:loan_id>/add-book/<int:book_id>', methods=['PUT'])
@limiter.limit("600 per day", override_defaults=True)
def add_book(loan_id, book_id):
    loan = db.session.get(Loans, loan_id)
    book = db.session.get(Books, book_id)

    if book not in loan.books: #checking to see if a relationship already exist between loan and book
        loan.books.append(book) #creating a relationship between loan and book
        db.session.commit()
        return jsonify({
            'message': f'successfully add {book.title} to loan',
            'loan': loan_schema.dump(loan),  #use dump when the schema is adding just a piece of the return message
            'books': books_schema.dump(loan.books) #using the books_schema to serialize the list of books related to the loan
        }), 200
    
    return jsonify("This book is already on the loan"), 400

#Remove book from loan
@loans_bp.route('/<int:loan_id>/remove-book/<int:book_id>', methods=['PUT'])
def remove_book(loan_id, book_id):
    loan = db.session.get(Loans, loan_id)
    book = db.session.get(Books, book_id)

    if book in loan.books: #checking to see if a relationship already exist between loan and book
        loan.books.remove(book) #removing the relationship between loan and book
        db.session.commit()
        return jsonify({
            'message': f'successfully removed {book.title} from loan',
            'loan': loan_schema.dump(loan),  #use dump when the schema is adding just a piece of the return message
            'books': books_schema.dump(loan.books) #using the books_schema to serialize the list of books related to the loan
        }), 200
    
    return jsonify("This book is no on the loan"), 400


@loans_bp.route('', methods=['GET'])
def get_loans():
    loans = db.session.query(Loans).all()
    return loans_schema.jsonify(loans), 200