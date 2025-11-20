
from . import books_bp
from .schemas import book_schema, books_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Books, db
from app.extensions import limiter, cache
from sqlalchemy import select

#Create Book Endpoint
@books_bp.route('', methods=['POST'])
def create_book():
    try:
        data = book_schema.load(request.json) #validates data and translates json object to python dictionary
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_book = Books(**data)
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book), 201


#READ BOOKS
@books_bp.route('', methods=['GET'])
# @cache.cached(timeout=90) #If you cache paginated routes it will cache a single page
def get_books():
    try: 
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        query = select(Books)
        books = db.paginate(query, page=page, per_page=per_page) #Handles our pagination so we don't have to track how many items to be sending
        return books_schema.jsonify(books), 200
    except:
        books = db.session.query(Books).all()
        return books_schema.jsonify(books), 200


#UPDATE BOOK
@books_bp.route('/<int:book_id>', methods=['PUT'])
@limiter.limit("30 per hour")
def update_book(book_id):
    book = db.session.get(Books, book_id)

    if not book:
        return jsonify("Invalid book_id"), 404
    
    try:
        data = book_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    for key, value in data.items():
        setattr(book, key, value) #setting my new attributes

    db.session.commit()
    return book_schema.jsonify(book), 200


#DELETE BOOK
@books_bp.route('/<int:book_id>', methods=['DELETE'])
@limiter.limit("8 per day")
def delete_book(book_id):
    book = db.session.get(Books,book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(f"Successfully deleted book {book_id}")


@books_bp.route('/popularity', methods=['GET'])
def get_popular_books():

    books = db.session.query(Books).all() #Grabbing all books

    # popular_books = db.session.query(Books).order_by(Books.times_borrowed.desc()).limit(10).all()

    # Sort books list based off of how many loans the've been apart of
    books.sort(key = lambda book: len(book.loans), reverse=True) 

    output = []
    for book in books[:5]:
        book_format = {
            "book": book_schema.dump(book),
            "readers": len(book.loans)
        }
        output.append(book_format)

    return jsonify(output), 200

    # lambda num1, num2: num1 + num2

@books_bp.route('/search', methods=['GET'])
def search_books():
    title = request.args.get('title') #Accessing the qery parameters from my URL

    books = db.session.query(Books).where(Books.title.ilike(f"%{title}%")).all()

    return books_schema.jsonify(books), 200

# Tasks for Mechanic Shop API
# - Route to search customer by their email
# - Route to find which mechanic worked on the most tickets
# - Turn the get_tickets route into a paginated route

# Please do at least one, would love to see all three