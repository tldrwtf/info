from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Column, ForeignKey, Table
from datetime import date, datetime, timedelta

# Create a base class for our models
class Base(DeclarativeBase):
  pass
  # you could add your own configuration

db = SQLAlchemy(model_class = Base)

loan_books = Table(
    'loan_books',
    Base.metadata,
    Column('loan_id', ForeignKey('loans.id')),
    Column('book_id', ForeignKey('books.id'))
)

class Users(Base):
  __tablename__ = 'users'

  id: Mapped[int] = mapped_column(primary_key=True)
  first_name: Mapped[str] = mapped_column(String(250), nullable=False)
  last_name: Mapped[str] = mapped_column(String(250), nullable=False)
  email: Mapped[str] = mapped_column(String(350), nullable=False, unique=True)
  password: Mapped[str] = mapped_column(String(150), nullable=False)
  DOB: Mapped[date] = mapped_column(Date, nullable=True)
  address: Mapped[str] = mapped_column(String(500), nullable=True)
  role: Mapped[str] = mapped_column(String(30), nullable=False)

  loans: Mapped[list['Loans']] = relationship('Loans', back_populates='user')

class Loans(Base):
    __tablename__ = 'loans'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    loan_date: Mapped[date] = mapped_column(Date, default=datetime.now())
    deadline: Mapped[date] = mapped_column(Date, default=datetime.now() + timedelta(days=14))
    return_date: Mapped[date] = mapped_column(Date, nullable=True)

    user: Mapped['Users'] = relationship('Users', back_populates='loans')
    books: Mapped[list['Books']] = relationship("Books",secondary=loan_books, back_populates='loans')
   
class Books(Base):
  __tablename__ = 'books'

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
  genre: Mapped[str] = mapped_column(String(360), nullable=False)
  age_category: Mapped[str] = mapped_column(String(120), nullable=False)
  publish_date: Mapped[date] = mapped_column(Date, nullable=False)
  author: Mapped[str] = mapped_column(String(500), nullable=False)

  loans: Mapped[list['Loans']] = relationship("Loans",secondary=loan_books, back_populates='books')