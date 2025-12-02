from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Column, ForeignKey, Table, DateTime, Float
from datetime import date, datetime, timedelta

# Create a base class for our models
class Base(DeclarativeBase):
    pass
# you could add your own configuration

db = SQLAlchemy(model_class=Base)

# Association Table for Many-to-Many
loan_book = Table(
    "loan_book",
    Base.metadata,
    Column("loan_id", ForeignKey("loans.id")),
    Column("book_id", ForeignKey("books.id"))
)

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(350), unique=True)
    phone: Mapped[str] = mapped_column(String(15))
    password: Mapped[str] = mapped_column(String(150))
    role: Mapped[str] = mapped_column(String(50), default="User") # User or Admin

    # One-to-Many: One user can have many loans
    loans: Mapped[list['Loans']] = relationship('Loans', back_populates='user')

class Loans(Base):
    __tablename__ = 'loans'

    id: Mapped[int] = mapped_column(primary_key=True)
    return_date: Mapped[date] = mapped_column(Date)
    borrow_date: Mapped[date] = mapped_column(Date)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['Users'] = relationship('Users', back_populates='loans')

    # Many-to-Many: One loan can have many books
    books: Mapped[list['Books']] = relationship(secondary=loan_book, back_populates='loans')

class Books(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str] = mapped_column(String(200))
    isbn: Mapped[str] = mapped_column(String(20), unique=True)

    loans: Mapped[list['Loans']] = relationship(secondary=loan_book, back_populates='books')

class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[date] = mapped_column(Date, default=date.today())
    
    # Relationship to Items (One-to-Many: One order can have many items)
    items: Mapped[list['Items']] = relationship('Items', back_populates='order')

class Items(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    is_sold: Mapped[bool] = mapped_column(default=False)
    
    description_id: Mapped[int] = mapped_column(ForeignKey('item_description.id'))
    description: Mapped['ItemDescription'] = relationship('ItemDescription', back_populates='items')

    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'), nullable=True)
    order: Mapped['Orders'] = relationship('Orders', back_populates='items')

class ItemDescription(Base):
    __tablename__ = 'item_description'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String(500))

    items: Mapped[list['Items']] = relationship('Items', back_populates='description')