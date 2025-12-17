# GraphQL Integration Guide

This guide covers the fundamentals of GraphQL and how to implement a GraphQL API using Python, Flask, Graphene, and SQLAlchemy.

## 1. What is GraphQL?

GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. Unlike REST, where you hit specific endpoints for specific data (e.g., `/users/1`), GraphQL allows clients to ask for exactly what they need in a single request.

### Key Benefits
*   **No Over-fetching:** Clients receive only the data they request.
*   **Single Endpoint:** All requests go to `/graphql` (usually via POST).
*   **Strongly Typed:** The schema defines exactly what data is available.

## 2. Core Concepts

### 2.1. The Schema
The schema defines the structure of your data. It supports:
*   **Scalars:** Basic types (`String`, `Int`, `Float`, `Boolean`, `ID`).
*   **Objects:** Complex types with fields (e.g., `User`, `Product`).

### 2.2. Operations
*   **Query:** Reading data (equivalent to GET).
*   **Mutation:** Writing/Modifying data (equivalent to POST, PUT, DELETE).

**Example Query:**
```graphql
query {
  user(id: "1") {
    name
    email
  }
}
```

**Example Mutation:**
```graphql
mutation {
  addUser(name: "Alice", email: "alice@example.com") {
    id
    name
  }
}
```

## 3. Python Implementation (Flask + Graphene)

We will use `graphene` (Python GraphQL library), `Flask-GraphQL` (Flask integration), and `graphene-sqlalchemy` (ORM integration).

### 3.1. Setup & Installation

```bash
pip install Flask Flask-GraphQL graphene graphene-sqlalchemy Flask-SQLAlchemy
```

### 3.2. Database Models (`models.py`)

Define your SQLAlchemy models as usual.

```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255))
    director: Mapped[str] = mapped_column(db.String(255))
    year: Mapped[int] = mapped_column(db.Integer)
```

### 3.3. GraphQL Schema & Resolvers (`schema.py`)

This is where the magic happens. We map SQLAlchemy models to GraphQL types and define our Queries and Mutations.

```python
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Movie as MovieModel, db

# 1. Map SQLAlchemy Model to GraphQL Object
class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

# 2. Define Queries (Read)
class Query(graphene.ObjectType):
    movies = graphene.List(Movie)
    search_movies = graphene.List(Movie, title=graphene.String())

    def resolve_movies(self, info):
        return db.session.execute(db.select(MovieModel)).scalars()
    
    def resolve_search_movies(self, info, title=None):
        query = db.select(MovieModel)
        if title:
            query = query.where(MovieModel.title.ilike(f'%{title}%'))
        return db.session.execute(query).scalars().all()

# 3. Define Mutations (Write)
class AddMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        director = graphene.String(required=True)
        year = graphene.Int(required=True)
    
    movie = graphene.Field(Movie)

    def mutate(self, info, title, director, year):
        movie = MovieModel(title=title, director=director, year=year)
        db.session.add(movie)
        db.session.commit()
        return AddMovie(movie=movie)

class Mutation(graphene.ObjectType):
    create_movie = AddMovie.Field()
    # Add UpdateMovie/DeleteMovie here similarly

# 4. Final Schema
schema = graphene.Schema(query=Query, mutation=Mutation)
```

### 3.4. Application Entry Point (`app.py`)

Connect the schema to a Flask route using `GraphQLView`.

```python
from flask import Flask
from models import db
from schema import schema
from flask_graphql import GraphQLView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)

# The GraphQL endpoint
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # Enables the interactive GraphiQL interface
    )
)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

## 4. Testing with GraphiQL

1.  Run the app: `python app.py`
2.  Navigate to `http://localhost:5000/graphql`
3.  Try a query:

```graphql
{
  movies {
    title
    director
  }
}
```
