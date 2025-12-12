# Building AI-Ready APIs with Flask

As AI agents (like Gemini, ChatGPT, and Claude) become more capable, building APIs that these agents can autonomously consume is a critical skill. This guide covers how to design your Flask APIs so they can serve as "Tools" for AI models.

## What makes an API "AI-Ready"?

An AI-ready API isn't just about serving JSON to a frontend. It focuses on:
1.  **Discoverability:** The AI must understand *what* endpoints exist and *how* to use them.
2.  **Clarity:** Parameters and return values must be self-explanatory.
3.  **Error Handling:** Errors should be descriptive enough for an AI to correct its mistake.
4.  **Efficiency:** Endpoints should be atomic and focused (doing one thing well).

## The Golden Rule: OpenAPI (Swagger)

The standard way AI agents "learn" your API is through an **OpenAPI Specification (OAS)**.

### 1. Generating Swagger Docs in Flask

In your `Library-Api`, you are already using `flask-swagger-ui`. To make it AI-ready, ensure your docstrings are descriptive.

**Bad Docstring:**
```python
@books_bp.route('/books', methods=['POST'])
def create_book():
    """Create a book."""
    # ...
```

**AI-Friendly Docstring:**
```python
@books_bp.route('/books', methods=['POST'])
def create_book():
    """
    Adds a new book to the library catalog.
    
    Requires a JSON body with 'title' (string), 'author' (string), and 'isbn' (string).
    Returns the created book object with its assigned unique ID.
    Useful for populating the database with new inventory.
    """
    # ...
```

### 2. Serving the Spec

AI Tools (like OpenAI GPTs or Gemini Function Calling) often ingest a `swagger.yaml` or `openapi.json` file. Ensure your `static/swagger.yaml` is up-to-date and accessible.

## Designing "Tools" for Agents

When building endpoints intended for AI consumption (Function Calling), think of them as standalone functions.

### Example: A "Search" Tool

Instead of just `GET /books`, an agent might prefer a dedicated search endpoint that accepts natural language queries or specific filters.

```python
@books_bp.route('/search', methods=['GET'])
def search_books():
    """
    Search for books by natural query or filters.
    
    Query Parameters:
    - q: General search text (title or author)
    - available: Boolean (true/false) to filter by availability
    
    Example: /api/books/search?q=Harry+Potter&available=true
    """
    query = request.args.get('q')
    available = request.args.get('available')
    
    # Logic to filter books...
    results = Book.query.filter(Book.title.ilike(f'%{query}%')).all()
    
    return jsonify(books_schema.dump(results))
```

## Context & State

AI agents are often stateless between sessions. Your API should provide enough context in the response for the agent to decide the next step.

**Response Design:**
Include links or IDs for related actions.

```json
{
  "id": 1,
  "title": "The Hobbit",
  "status": "borrowed",
  "actions": {
    "return": "/api/loans/1/return",
    "details": "/api/books/1"
  }
}
```
*This is known as HATEOAS (Hypermedia as the Engine of Application State), and it helps agents navigate your API.*

## Security for Agents

If you are allowing an AI agent to perform actions (like booking appointments or deleting users), security is paramount.

1.  **API Keys:** Issue unique API keys for the AI agent integration.
2.  **Scopes:** Limit the AI's permission. Maybe it can `read` books but not `delete` users.
3.  **Rate Limiting:** AI agents can loop rapidly. Use `Flask-Limiter` to prevent accidental DOS attacks.

```python
# app/extensions.py
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

# In your route
@books_bp.route('/search')
@limiter.limit("60 per minute")
def search_books():
    # ...
```

## Checklist for AI Integration

- [ ] **Documentation:** Is `swagger.yaml` accessible and valid?
- [ ] **Descriptions:** Do all endpoints have clear, verbose docstrings explaining *why* and *how* to use them?
- [ ] **Validation:** Do you return clear 400 errors (e.g., "Field 'email' is missing") so the AI can self-correct?
- [ ] **Predictability:** Do responses follow a consistent JSON structure?

## Future-Proofing

As you build the "Intro to AI Tools" project, consider adding an endpoint specifically for the AI to "inspect" the database schema or available tools, enabling dynamic tool selection.

```python
@app.route('/api/tools', methods=['GET'])
def get_tools():
    """Returns a list of available actions this API supports."""
    return jsonify([
        {"name": "search_books", "description": "Finds books by title/author"},
        {"name": "check_availability", "description": "Checks if a book is in stock"}
    ])
```

---

## See Also

- **[Flask REST API Development Guide](Flask_REST_API_Development_Guide.md)** - Building scalable web APIs
- **[APIs and Requests Cheat Sheet](../cheatsheets/APIs_and_Requests_Cheat_Sheet.md)** - HTTP requests and methods
- **[Library-Api Production Workflow Guide](Library-Api_Production_Workflow_Guide.md)** - Production considerations