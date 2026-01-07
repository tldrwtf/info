# APIs & HTTP Requests - Complete Reference Guide

## Quick Reference Card

| Component | Syntax | Example |
|-----------|--------|---------|
| GET request | `requests.get(url)` | `requests.get('https://api.example.com/data')` |
| POST request | `requests.post(url, json=data)` | `requests.post(url, json={'key': 'value'})` |
| PUT request | `requests.put(url, json=data)` | `requests.put(url, json={'key': 'value'})` |
| DELETE request | `requests.delete(url)` | `requests.delete('https://api.example.com/item/1')` |
| Query params | `params={'key': 'value'}` | `requests.get(url, params={'page': 1})` |
| Headers | `headers={'key': 'value'}` | `headers={'Authorization': 'Bearer token'}` |
| JSON response | `response.json()` | `data = response.json()` |
| Status code | `response.status_code` | `if response.status_code == 200:` |
| Check success | `response.ok` | `if response.ok:` |
| Timeout | `timeout=seconds` | `requests.get(url, timeout=5)` |

**Common Status Codes:** 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error)

## Table of Contents
- [API Basics](#api-basics)
- [HTTP Methods](#http-methods)
- [Python Requests Library](#python-requests-library)
- [Request Components](#request-components)
- [Response Handling](#response-handling)
- [Authentication](#authentication)
- [Error Handling](#error-handling)
- [Best Practices](#best-practices)

---

## API Basics

### What is an API?
```python
# API - Application Programming Interface
# Allows different software applications to communicate

# REST API - Representational State Transfer
# Uses HTTP methods to perform CRUD operations:
# - Create (POST)
# - Read (GET)
# - Update (PUT/PATCH)
# - Delete (DELETE)
```

### JSON Format
```python
# JSON - JavaScript Object Notation
# Lightweight data interchange format

# Python dict ←→ JSON
import json

# Python to JSON
python_dict = {"name": "Wilson", "age": 30}
json_string = json.dumps(python_dict)
# '{"name": "Wilson", "age": 30}'

# JSON to Python
json_data = '{"name": "Bob", "age": 25}'
python_obj = json.loads(json_data)
# {'name': 'Bob', 'age': 25}
```

### HTTP Status Codes
```python
# 2xx - Success
200  # OK - Request successful
201  # Created - Resource created successfully
204  # No Content - Successful but no data returned

# 3xx - Redirection
301  # Moved Permanently
302  # Found (temporary redirect)

# 4xx - Client Errors (Your mistake)
400  # Bad Request - Malformed request
401  # Unauthorized - Authentication required
403  # Forbidden - No permission
404  # Not Found - Resource doesn't exist
429  # Too Many Requests - Rate limit exceeded

# 5xx - Server Errors (Their problem)
500  # Internal Server Error
502  # Bad Gateway
503  # Service Unavailable
```

---

## HTTP Methods

### GET - Retrieve Data
```python
import requests

# GET request
response = requests.get("https://api.example.com/users")

# GET with parameters
params = {"page": 1, "limit": 10}
response = requests.get("https://api.example.com/users", params=params)
# Actual URL: https://api.example.com/users?page=1&limit=10
```

### POST - Create Data
```python
import requests

# POST request with JSON body
data = {
    "name": "Wilson",
    "email": "Wilson@example.com",
    "age": 30
}

response = requests.post(
    "https://api.example.com/users",
    json=data  # Automatically sets Content-Type: application/json
)

# Alternative: send as form data
response = requests.post(
    "https://api.example.com/users",
    data=data  # Content-Type: application/x-www-form-urlencoded
)
```

### PUT - Update (Replace) Data
```python
import requests

# PUT request - replaces entire resource
updated_data = {
    "name": "Wilson Johnson",
    "email": "Wilson.j@example.com",
    "age": 31
}

response = requests.put(
    "https://api.example.com/users/123",
    json=updated_data
)
```

### PATCH - Partial Update
```python
import requests

# PATCH request - updates specific fields
partial_update = {
    "age": 31  # Only update age
}

response = requests.patch(
    "https://api.example.com/users/123",
    json=partial_update
)
```

### DELETE - Remove Data
```python
import requests

# DELETE request
response = requests.delete("https://api.example.com/users/123")

# Check if successful
if response.status_code == 204:
    print("User deleted successfully")
```

---

## Python Requests Library

### Installation
```bash
pip install requests
```

### Basic GET Request
```python
import requests

# Make a GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check status
print(response.status_code)  # 200

# Get JSON data
data = response.json()
print(data)  # Python dictionary

# Get raw text
print(response.text)  # String
```

### Request with Timeout
```python
import requests

# Timeout in seconds
try:
    response = requests.get(
        "https://api.example.com/data",
        timeout=5  # Wait max 5 seconds
    )
except requests.Timeout:
    print("Request timed out")
```

### Request with Retries
```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Configure retry strategy
retry_strategy = Retry(
    total=3,  # Total number of retries
    backoff_factor=1,  # Wait 1, 2, 4 seconds between retries
    status_forcelist=[429, 500, 502, 503, 504]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)

# Make request with retries
response = session.get("https://api.example.com/data")
```

---

## Request Components

### Headers
```python
import requests

# Add custom headers
headers = {
    "User-Agent": "MyApp/1.0",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)

# View request headers
print(response.request.headers)
```

### Query Parameters
```python
import requests

# Method 1: In URL
response = requests.get("https://api.example.com/search?q=python&page=1")

# Method 2: Using params (recommended)
params = {
    "q": "python",
    "page": 1,
    "limit": 10
}

response = requests.get("https://api.example.com/search", params=params)

# With list values
params = {
    "tags": ["python", "api", "tutorial"]
}
# Becomes: ?tags=python&tags=api&tags=tutorial
```

### Request Body
```python
import requests

# JSON body (most common for APIs)
data = {
    "username": "Wilson",
    "email": "Wilson@example.com"
}

response = requests.post(
    "https://api.example.com/users",
    json=data  # Automatically serializes and sets Content-Type
)

# Form data
form_data = {
    "username": "Wilson",
    "password": "secret123"
}

response = requests.post(
    "https://api.example.com/login",
    data=form_data  # Sent as form-encoded
)

# Raw string body
response = requests.post(
    "https://api.example.com/webhook",
    data="raw string data"
)
```

### Cookies
```python
import requests

# Send cookies
cookies = {"session_id": "abc123"}
response = requests.get(
    "https://api.example.com/profile",
    cookies=cookies
)

# Get cookies from response
print(response.cookies)
```

---

## Response Handling

### Accessing Response Data
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Status code
status = response.status_code  # 200

# JSON data (raises error if not JSON)
data = response.json()

# Raw text
text = response.text

# Raw bytes
content = response.content

# Headers
headers = response.headers
content_type = response.headers['Content-Type']

# URL (useful after redirects)
url = response.url

# Check if successful (2xx status code)
is_success = response.ok  # True for 200-299
```

### Checking Response Status
```python
import requests

response = requests.get("https://api.example.com/data")

# Method 1: Check status code
if response.status_code == 200:
    data = response.json()
    print("Success:", data)
elif response.status_code == 404:
    print("Resource not found")
else:
    print(f"Error: {response.status_code}")

# Method 2: Use ok property
if response.ok:
    data = response.json()
else:
    print(f"Request failed: {response.status_code}")

# Method 3: Raise exception for error status
try:
    response.raise_for_status()  # Raises HTTPError for 4xx/5xx
    data = response.json()
except requests.HTTPError as e:
    print(f"HTTP Error: {e}")
```

### Parsing JSON Safely
```python
import requests

response = requests.get("https://api.example.com/data")

# Check if response is JSON
if response.headers.get('Content-Type') == 'application/json':
    try:
        data = response.json()
    except ValueError:
        print("Invalid JSON response")
else:
    print("Response is not JSON")

# Or use try-except
try:
    data = response.json()
except requests.JSONDecodeError:
    print("Failed to parse JSON")
```

---

## Authentication

### API Key Authentication
```python
import requests

# Method 1: In query parameters
api_key = "your_api_key_here"
response = requests.get(
    "https://api.example.com/data",
    params={"api_key": api_key}
)

# Method 2: In headers (more common)
headers = {
    "X-API-Key": api_key
}
response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

### Bearer Token Authentication
```python
import requests

# Common for OAuth 2.0
token = "your_access_token_here"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    "https://api.example.com/protected",
    headers=headers
)
```

### Basic Authentication
```python
import requests

# Method 1: Using auth parameter (recommended)
response = requests.get(
    "https://api.example.com/data",
    auth=("username", "password")
)

# Method 2: Manual header
import base64

credentials = "username:password"
encoded = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded}"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

### OAuth 2.0 Example (Spotify)
```python
import requests
import base64

# Step 1: Get access token
client_id = "your_client_id"
client_secret = "your_client_secret"

# Encode credentials
credentials = f"{client_id}:{client_secret}"
encoded_creds = base64.b64encode(credentials.encode()).decode()

# Request token
token_url = "https://accounts.spotify.com/api/token"

headers = {
    "Authorization": f"Basic {encoded_creds}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials"
}

response = requests.post(token_url, headers=headers, data=data)
token_data = response.json()
access_token = token_data["access_token"]

# Step 2: Use token for API requests
api_headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(
    "https://api.spotify.com/v1/search",
    headers=api_headers,
    params={"q": "Beatles", "type": "artist"}
)

data = response.json()
```

---

## Error Handling

### Comprehensive Error Handling
```python
import requests
from requests.exceptions import (
    Timeout,
    ConnectionError,
    HTTPError,
    RequestException
)

def make_api_request(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad status
        return response.json()

    except Timeout:
        print("Request timed out")
        return None

    except ConnectionError:
        print("Failed to connect to server")
        return None

    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        print(f"Status code: {e.response.status_code}")
        return None

    except RequestException as e:
        # Catch all other requests exceptions
        print(f"An error occurred: {e}")
        return None

    except ValueError:
        # JSON decode error
        print("Invalid JSON in response")
        return None

# Use the function
data = make_api_request("https://api.example.com/data")
if data:
    print("Success:", data)
```

### Handling Rate Limits
```python
import requests
import time

def api_call_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 429:  # Rate limited
            retry_after = int(response.headers.get('Retry-After', 60))
            print(f"Rate limited. Waiting {retry_after} seconds...")
            time.sleep(retry_after)

        else:
            print(f"Error: {response.status_code}")
            break

    return None
```

---

## Best Practices

### Using Sessions
```python
import requests

# Session persists cookies and connection pooling
session = requests.Session()

# Set default headers for all requests
session.headers.update({
    "User-Agent": "MyApp/1.0",
    "Authorization": "Bearer token123"
})

# All requests use the session
response1 = session.get("https://api.example.com/users")
response2 = session.get("https://api.example.com/posts")

# Close session when done
session.close()

# Or use context manager
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer token123"})
    response = session.get("https://api.example.com/data")
```

### Environment Variables for Secrets
```python
import os
import requests

# Store API keys in environment variables, not in code!

# Set environment variable (in terminal):
# export API_KEY="your_api_key_here"

# Or use .env file with python-dotenv
# pip install python-dotenv

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in environment variables")

headers = {"X-API-Key": api_key}
response = requests.get("https://api.example.com/data", headers=headers)
```

### Response Caching
```python
import requests
from datetime import datetime, timedelta

class SimpleCache:
    def __init__(self, ttl_seconds=300):
        self.cache = {}
        self.ttl = ttl_seconds

    def get(self, key):
        if key in self.cache:
            data, timestamp = self.cache[key]
            if datetime.now() - timestamp < timedelta(seconds=self.ttl):
                return data
            else:
                del self.cache[key]
        return None

    def set(self, key, value):
        self.cache[key] = (value, datetime.now())

# Usage
cache = SimpleCache(ttl_seconds=300)  # 5 minute cache

def get_data(url):
    # Check cache first
    cached = cache.get(url)
    if cached:
        print("Using cached data")
        return cached

    # Make request
    response = requests.get(url)
    data = response.json()

    # Cache the result
    cache.set(url, data)
    return data
```

---

## Practical Examples

### Weather API
```python
import requests

def get_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
    else:
        return None

# weather = get_weather("London", "your_api_key")
```

### Pokemon API - Complete Example

This real-world example demonstrates proper API integration with error handling and nested JSON parsing.

```python
import requests

def get_pokemon_data(pokemon_identifier):
    """
    Get Pokemon data from PokeAPI and extract game-relevant information.

    Args:
        pokemon_identifier: Pokemon name (str) or ID (int)
            Examples: "pikachu", "charizard", 25, 6

    Returns:
        dict: Pokemon information with keys: name, id, hp, attack, sprite_url, type
        None: if Pokemon not found or error occurred

    Example:
        >>> pikachu = get_pokemon_data("pikachu")
        >>> print(f"{pikachu['name']} has {pikachu['hp']} HP")
        pikachu has 35 HP
    """

    # Step 1: Construct URL with identifier (can be name or ID)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"

    # Step 2: Make GET request
    response = requests.get(url)

    # Step 3: Check if request was successful
    if response.status_code == 200:
        data = response.json()  # Convert JSON to Python dictionary

        # Step 4: Extract relevant data from nested JSON structure
        pokemon = {
            "name": data['name'],
            "id": data['id'],
            "hp": data["stats"][0]["base_stat"],  # HP is first stat
            "attack": data["stats"][1]["base_stat"],  # Attack is second stat
            "sprite_url": data["sprites"]["front_default"],
            "type": data["types"][0]["type"]["name"]  # Primary type
        }
        return pokemon

    elif response.status_code == 404:
        # Pokemon not found
        print(f"Pokemon '{pokemon_identifier}' not found")
        return None

    else:
        # Other errors
        print(f"Failed to catch {pokemon_identifier}: Status {response.status_code}")
        return None


# Usage Examples:
if __name__ == "__main__":
    # Example 1: Get Pokemon by name
    pikachu = get_pokemon_data("pikachu")
    if pikachu:
        print(f"\n{pikachu['name'].title()}")
        print(f"   Type: {pikachu['type']}")
        print(f"   HP: {pikachu['hp']}")
        print(f"   Attack: {pikachu['attack']}")

    # Example 2: Get Pokemon by ID
    charizard = get_pokemon_data(6)
    if charizard:
        print(f"\n{charizard['name'].title()}")
        print(f"   Type: {charizard['type']}")
        print(f"   HP: {charizard['hp']}")
        print(f"   Attack: {charizard['attack']}")

    # Example 3: Handle invalid Pokemon
    invalid = get_pokemon_data("invalidpokemon")
    if not invalid:
        print("\nPokemon not found!")
```

**Key Features of This Example:**

- **Flexible input:** Works with both string names and integer IDs
- **Error handling:** Checks status codes and returns `None` on failure
- **Nested JSON parsing:** Extracts data from complex JSON structure
- **Type safety:** Returns consistent dictionary structure or `None`
- **Documentation:** Clear docstring with examples
- **Real API:** Free API with no authentication required
- **Relatable:** Pokemon are familiar to students

**Understanding the JSON Structure:**

```python
# PokeAPI returns deeply nested JSON:
{
    "name": "pikachu",
    "id": 25,
    "stats": [
        {"base_stat": 35, "stat": {"name": "hp"}},      # Index 0
        {"base_stat": 55, "stat": {"name": "attack"}},   # Index 1
        # ... more stats
    ],
    "sprites": {
        "front_default": "https://...pikachu.png"
    },
    "types": [
        {"type": {"name": "electric"}}  # Primary type at index 0
    ]
}

# We navigate this structure to extract just what we need
```

### Fetch to UI (js-api-in-class / Poke-API-Game)
```javascript
// Fetch → map → render cards; cache for fast reloads
const cacheKey = 'pokemon-cache';
const root = document.querySelector('#cards');

const renderCard = (p) => `
  <article class="card">
    <h3>${p.name}</h3>
    <img src="${p.sprite}" alt="${p.name}">
    <p>Type: ${p.type}</p>
  </article>`;

const paint = (list) => {
  root.innerHTML = list.map(renderCard).join('');
};

const load = async () => {
  const cached = localStorage.getItem(cacheKey);
  if (cached) paint(JSON.parse(cached)); // fast path from cache

  const res = await fetch('/api/pokemon');
  if (!res.ok) throw new Error('Fetch failed');
  const data = await res.json();
  paint(data);
  localStorage.setItem(cacheKey, JSON.stringify(data)); // refresh cache
};

load().catch(err => console.error(err));
```
- Patterns: cache-first then refresh, pure render helper, single DOM write (`innerHTML`) to avoid many reflows.
- Applies to the class repos `js-api-in-class` and `Poke-API-Game`; pair with DOM delegation from the DOM guide for interactive controls.

### RESTful CRUD Operations
```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Create
def create_post(title, body, user_id):
    url = f"{BASE_URL}/posts"
    data = {"title": title, "body": body, "userId": user_id}
    response = requests.post(url, json=data)
    return response.json()

# Read
def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url)
    return response.json() if response.ok else None

# Update
def update_post(post_id, title, body):
    url = f"{BASE_URL}/posts/{post_id}"
    data = {"title": title, "body": body}
    response = requests.put(url, json=data)
    return response.json()

# Delete
def delete_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.delete(url)
    return response.status_code == 200

# Usage
# new_post = create_post("My Title", "My content", 1)
# post = get_post(1)
# update_post(1, "Updated Title", "Updated content")
# delete_post(1)
```

---

## See Also

- **[Error Handling Cheat Sheet](Error_Handling_Cheat_Sheet.md)** - Exception handling for API calls
- **[File Operations Cheat Sheet](File_Operations_Cheat_Sheet.md)** - JSON file operations
- **[Standard Library Essentials Cheat Sheet](Standard_Library_Essentials_Cheat_Sheet.md)** - json module
- **[Testing and Debugging Cheat Sheet](Testing_and_Debugging_Cheat_Sheet.md)** - Mocking API calls

---
