from app.extensions import ma
from app.models import Books

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Books

book_schema = BookSchema()
books_schema = BookSchema(many=True)