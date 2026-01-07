# API Authentication Guide

## Quick Reference Card

| Auth Method | Use Case | Implementation | Example |
|-------------|----------|----------------|---------|
| API Key | Simple public APIs | Header/query param | `headers={'X-API-Key': 'key'}` |
| Bearer Token | Modern APIs | Authorization header | `Authorization: Bearer token` |
| Basic Auth | Legacy/simple | Username:password Base64 | `auth=('user', 'pass')` |
| OAuth 2.0 | Third-party access | Complex flow | Spotify, Google, GitHub |
| JWT | Stateless auth | Encoded token | Login returns JWT |
| Session Auth | Web apps | Cookies/sessions | Flask-Login |

**Common Headers:**
- `Authorization: Bearer <token>` - Most common
- `X-API-Key: <key>` - API keys
- `Cookie: session=<id>` - Session auth

## Table of Contents
1. [Authentication Basics](#authentication-basics)
2. [API Keys](#api-keys)
3. [Bearer Tokens](#bearer-tokens)
4. [Basic Authentication](#basic-authentication)
5. [OAuth 2.0](#oauth-20)
6. [JWT (JSON Web Tokens)](#jwt-json-web-tokens)
7. [Session-Based Authentication](#session-based-authentication)
8. [Best Practices](#best-practices)
9. [Complete Examples](#complete-examples)

---

## Authentication Basics

### What is Authentication?
```python
# Authentication - Verifying who you are
# "Are you really John Doe?"

# Authorization - What you're allowed to do
# "John Doe can view this resource"

# Together they secure APIs
```

### Why Authenticate APIs?
```python
# 1. Identify users
user = get_user_from_token(token)

# 2. Rate limiting
if user.requests_today > 1000:
    return "Rate limit exceeded", 429

# 3. Access control
if not user.has_permission('delete_users'):
    return "Forbidden", 403

# 4. Track usage
log_api_usage(user, endpoint)
```

---

## API Keys

### Simple API Key
```python
import requests

API_KEY = 'your-api-key-here'

# Method 1: Header
response = requests.get(
    'https://api.example.com/data',
    headers={'X-API-Key': API_KEY}
)

# Method 2: Query parameter
response = requests.get(
    'https://api.example.com/data',
    params={'api_key': API_KEY}
)

print(response.json())
```

### Implementing API Key Auth in Flask
```python
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Store API keys (in production, use database)
VALID_API_KEYS = {
    'key123': 'user1',
    'key456': 'user2'
}

def require_api_key(f):
    """Decorator to require API key"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')

        if not api_key:
            return jsonify({'error': 'API key missing'}), 401

        if api_key not in VALID_API_KEYS:
            return jsonify({'error': 'Invalid API key'}), 401

        # Store user in request context
        request.user = VALID_API_KEYS[api_key]

        return f(*args, **kwargs)

    return decorated_function

@app.route('/api/data')
@require_api_key
def get_data():
    """Protected endpoint"""
    return jsonify({
        'message': f'Hello {request.user}!',
        'data': [1, 2, 3]
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Using Environment Variables
```python
import os
from dotenv import load_dotenv
import requests

# Load from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

response = requests.get(
    'https://api.example.com/data',
    headers={'X-API-Key': API_KEY}
)
```

---

## Bearer Tokens

### Using Bearer Tokens
```python
import requests

ACCESS_TOKEN = 'your-access-token'

# Bearer token in Authorization header
response = requests.get(
    'https://api.example.com/user/profile',
    headers={'Authorization': f'Bearer {ACCESS_TOKEN}'}
)

print(response.json())
```

### Implementing Bearer Token Auth
```python
from flask import Flask, request, jsonify
from functools import wraps
import secrets

app = Flask(__name__)

# Token storage (use database in production)
TOKENS = {}

def generate_token():
    """Generate secure random token"""
    return secrets.token_urlsafe(32)

def require_token(f):
    """Decorator to require bearer token"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return jsonify({'error': 'Authorization header missing'}), 401

        try:
            scheme, token = auth_header.split()

            if scheme.lower() != 'bearer':
                return jsonify({'error': 'Invalid authentication scheme'}), 401

            if token not in TOKENS:
                return jsonify({'error': 'Invalid token'}), 401

            request.user = TOKENS[token]
            return f(*args, **kwargs)

        except ValueError:
            return jsonify({'error': 'Invalid authorization header'}), 401

    return decorated_function

@app.route('/api/login', methods=['POST'])
def login():
    """Login and get token"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate credentials (simplified)
    if username == 'admin' and password == 'password':
        token = generate_token()
        TOKENS[token] = username

        return jsonify({'access_token': token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/protected')
@require_token
def protected():
    """Protected endpoint"""
    return jsonify({'message': f'Hello {request.user}!'})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Basic Authentication

### Using Basic Auth
```python
import requests

# Method 1: Using auth parameter
response = requests.get(
    'https://api.example.com/data',
    auth=('username', 'password')
)

# Method 2: Manual base64 encoding
import base64

credentials = base64.b64encode(b'username:password').decode('ascii')
response = requests.get(
    'https://api.example.com/data',
    headers={'Authorization': f'Basic {credentials}'}
)

print(response.json())
```

### Implementing Basic Auth in Flask
```python
from flask import Flask, request, jsonify
from functools import wraps
import base64

app = Flask(__name__)

# User database (simplified)
USERS = {
    'admin': 'password123',
    'user': 'pass456'
}

def check_auth(username, password):
    """Check if username/password is valid"""
    return USERS.get(username) == password

def require_basic_auth(f):
    """Decorator for basic auth"""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({'error': 'Authentication required'}), 401, {
                'WWW-Authenticate': 'Basic realm="Login Required"'
            }

        return f(*args, **kwargs)

    return decorated

@app.route('/api/data')
@require_basic_auth
def get_data():
    """Protected with basic auth"""
    return jsonify({'message': 'Success', 'data': [1, 2, 3]})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## OAuth 2.0

### OAuth 2.0 Flow
```python
"""
OAuth 2.0 Authorization Code Flow:

1. User clicks "Login with Spotify/Google/GitHub"
2. Redirect to provider's authorization URL
3. User grants permission
4. Provider redirects back with authorization code
5. Exchange code for access token
6. Use access token to make API calls
"""
```

### Spotify OAuth Example
```python
import requests
from flask import Flask, redirect, request, session
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Spotify credentials
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000/callback'

# Spotify URLs
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1'

@app.route('/')
def index():
    """Home page with login button"""
    return '''
        <h1>Spotify OAuth Demo</h1>
        <a href="/login">Login with Spotify</a>
    '''

@app.route('/login')
def login():
    """Redirect to Spotify authorization"""
    scope = 'user-read-private user-read-email'

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': scope
    }

    auth_url = f"{AUTH_URL}?{requests.compat.urlencode(params)}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    """Handle callback from Spotify"""
    code = request.args.get('code')

    # Exchange authorization code for access token
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(TOKEN_URL, data=token_data)
    token_info = response.json()

    # Store token in session
    session['access_token'] = token_info['access_token']

    return redirect('/profile')

@app.route('/profile')
def profile():
    """Get user profile from Spotify"""
    access_token = session.get('access_token')

    if not access_token:
        return redirect('/login')

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f'{API_BASE_URL}/me', headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return f'''
            <h1>Profile</h1>
            <p>Name: {user_data.get('display_name')}</p>
            <p>Email: {user_data.get('email')}</p>
            <p>Country: {user_data.get('country')}</p>
        '''

    return 'Error fetching profile', 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Spotify PKCE in practice (API-Authentication-Spotify- repo)
- Use PKCE when you cannot safely store a client secret (SPA/mobile). The repo `API-Authentication-Spotify-` follows this pattern:
  - Generate `code_verifier` (random 43-128 chars) and `code_challenge` (`base64url(sha256(verifier))`) client-side.
  - Redirect users to Spotify `authorize` with `response_type=code`, `code_challenge`, `code_challenge_method=S256`, scopes (playlists/profile), and `redirect_uri`.
  - On callback, exchange `code` for tokens by sending `grant_type=authorization_code`, `code_verifier`, and `redirect_uri` to the token endpoint. No client secret is sent from the browser.
  - Store `access_token` + `refresh_token`; refresh by POSTing `grant_type=refresh_token` with the original `code_verifier`.
- Tie-in: map this flow to the playlist/profile calls demonstrated in the repo and log token expiry so the UI can refresh before 401s. See also [OAuth2_and_Token_Management_Guide.md](OAuth2_and_Token_Management_Guide.md) for refresh and rotation tactics.

### GitHub OAuth Example
```python
import requests
from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# GitHub credentials
GITHUB_CLIENT_ID = 'your-client-id'
GITHUB_CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://localhost:5000/callback'

@app.route('/login')
def github_login():
    """Redirect to GitHub authorization"""
    params = {
        'client_id': GITHUB_CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': 'user:email'
    }

    url = f"https://github.com/login/oauth/authorize?{requests.compat.urlencode(params)}"
    return redirect(url)

@app.route('/callback')
def github_callback():
    """Handle GitHub callback"""
    code = request.args.get('code')

    # Exchange code for token
    token_data = {
        'client_id': GITHUB_CLIENT_ID,
        'client_secret': GITHUB_CLIENT_SECRET,
        'code': code
    }

    headers = {'Accept': 'application/json'}
    response = requests.post(
        'https://github.com/login/oauth/access_token',
        data=token_data,
        headers=headers
    )

    token_info = response.json()
    access_token = token_info['access_token']

    # Get user info
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get('https://api.github.com/user', headers=headers)

    user_data = user_response.json()
    return f"Hello, {user_data['login']}!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Real-World Example: Spotify Client Credentials Flow

This example demonstrates OAuth 2.0 Client Credentials Grant - used for server-to-server authentication without user login.

```python
import requests
import base64
from datetime import datetime, timedelta

class SpotifyAPI:
    """
    Spotify API Client using OAuth 2.0 Client Credentials Flow

    This flow is used when:
    - Your app needs to access Spotify catalog data
    - No user-specific data is needed (no playlists, saved tracks, etc.)
    - Server-to-server authentication
    """

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires_at = None
        self.token_url = "https://accounts.spotify.com/api/token"
        self.api_base_url = "https://api.spotify.com/v1"

    def get_token(self):
        """
        Get access token using Client Credentials Flow

        Steps:
        1. Base64 encode client_id:client_secret
        2. Send POST request with grant_type=client_credentials
        3. Receive access token (no refresh token in this flow)
        """

        # Step 1: Create authorization string
        # Format: client_id:client_secret -> Base64 encode
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

        # Step 2: Prepare request
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials"
        }

        # Step 3: Request token
        response = requests.post(self.token_url, headers=headers, data=data)

        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data['access_token']

            # Calculate expiration time (tokens typically last 1 hour)
            expires_in = token_data.get('expires_in', 3600)
            self.token_expires_at = datetime.now() + timedelta(seconds=expires_in)

            print(f"Token acquired successfully")
            print(f"  Expires at: {self.token_expires_at.strftime('%H:%M:%S')}")
            return self.access_token
        else:
            print(f"Failed to get token: {response.status_code}")
            print(f"  Response: {response.json()}")
            return None

    def is_token_valid(self):
        """Check if current token is still valid"""
        if not self.access_token or not self.token_expires_at:
            return False

        # Token is valid if it hasn't expired (with 5 min buffer)
        return datetime.now() < (self.token_expires_at - timedelta(minutes=5))

    def ensure_token(self):
        """Ensure we have a valid token, refresh if needed"""
        if not self.is_token_valid():
            print("Token expired or missing, getting new token...")
            return self.get_token()
        return self.access_token

    def search_track(self, query):
        """
        Search for a track on Spotify

        Args:
            query: Search query (artist and/or song name)

        Returns:
            dict: First matching track or None
        """
        self.ensure_token()

        url = f"{self.api_base_url}/search"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "q": query,
            "type": "track",
            "limit": 1
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            tracks = data.get('tracks', {}).get('items', [])

            if tracks:
                track = tracks[0]
                return {
                    "name": track['name'],
                    "artist": track['artists'][0]['name'],
                    "album": track['album']['name'],
                    "preview_url": track.get('preview_url'),
                    "spotify_url": track['external_urls']['spotify']
                }
        elif response.status_code == 401:
            # Token expired, try one more time
            print("Token unauthorized, refreshing...")
            self.get_token()
            return self.search_track(query)  # Retry once

        return None

    def get_artist_top_tracks(self, artist_id, country='US'):
        """Get artist's top tracks"""
        self.ensure_token()

        url = f"{self.api_base_url}/artists/{artist_id}/top-tracks"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "country": country
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            tracks = []

            for track in data.get('tracks', [])[:5]:  # Top 5
                tracks.append({
                    "name": track['name'],
                    "popularity": track['popularity'],
                    "preview_url": track.get('preview_url')
                })

            return tracks

        return None


# Usage Example
if __name__ == "__main__":
    # Initialize with credentials (store these in environment variables!)
    from creds import client_id, client_secret

    spotify = SpotifyAPI(client_id, client_secret)

    # Get token
    spotify.get_token()

    # Search for a track
    print("\nSearching for 'Bohemian Rhapsody'...")
    track = spotify.search_track("Bohemian Rhapsody Queen")

    if track:
        print(f"\nFound: {track['name']}")
        print(f"   Artist: {track['artist']}")
        print(f"   Album: {track['album']}")
        print(f"   Spotify: {track['spotify_url']}")

    # Token is automatically reused for subsequent requests
    print("\nSearching for another track...")
    track2 = spotify.search_track("Stairway to Heaven Led Zeppelin")

    if track2:
        print(f"\nFound: {track2['name']}")
        print(f"   Artist: {track2['artist']}")
```

**Key Differences from Authorization Code Flow:**

| Client Credentials | Authorization Code |
|-------------------|-------------------|
| Server-to-server | User authentication |
| No user login required | Requires user to log in |
| No user-specific data | Access user playlists, profile, etc. |
| Token lasts ~1 hour | Has refresh token |
| Base64 encoded credentials | Authorization code exchange |
| `grant_type=client_credentials` | `grant_type=authorization_code` |

**Why This Example is Valuable:**

- **Production-ready:** Includes token expiration handling and auto-refresh
- **Base64 encoding:** Shows how to properly encode credentials
- **Bearer token usage:** Demonstrates Authorization header pattern
- **Error handling:** Handles 401 errors and token expiration
- **OOP design:** Clean class-based API client
- **Real API:** Students can test with actual Spotify API
- **Token lifecycle:** Shows checking validity and refreshing when needed
- **Multiple endpoints:** Demonstrates reusing token across requests

---

## JWT (JSON Web Tokens)

### Understanding JWT
```python
"""
JWT Structure: header.payload.signature

Header: Algorithm and token type
Payload: Claims (user data)
Signature: Verification
"""
```

### Using PyJWT
```python
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your-secret-key'

def create_token(user_id, username):
    """Create JWT token"""
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=24),  # Expires in 24 hours
        'iat': datetime.utcnow()  # Issued at
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token):
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

# Usage
token = create_token(1, 'alice')
print(f"Token: {token}")

payload = verify_token(token)
if payload:
    print(f"User: {payload['username']}")
else:
    print("Invalid token")

# Install: pip install pyjwt
```

### Flask JWT Authentication
```python
from flask import Flask, request, jsonify
from functools import wraps
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# User database (simplified)
USERS = {
    'alice': {'id': 1, 'password': 'password123'},
    'bob': {'id': 2, 'password': 'pass456'}
}

def create_token(user_id, username):
    """Create JWT token"""
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

def token_required(f):
    """Decorator to require JWT token"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'error': 'Token missing'}), 401

        try:
            # Remove 'Bearer ' prefix if present
            if token.startswith('Bearer '):
                token = token[7:]

            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            request.user = data

        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/api/login', methods=['POST'])
def login():
    """Login and get JWT"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = USERS.get(username)

    if user and user['password'] == password:
        token = create_token(user['id'], username)
        return jsonify({'access_token': token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/profile')
@token_required
def profile():
    """Get user profile (protected)"""
    return jsonify({
        'user_id': request.user['user_id'],
        'username': request.user['username']
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Using JWT in Requests
```python
import requests

# Login to get token
response = requests.post(
    'http://localhost:5000/api/login',
    json={'username': 'alice', 'password': 'password123'}
)

token = response.json()['access_token']

# Use token for protected endpoints
headers = {'Authorization': f'Bearer {token}'}
response = requests.get(
    'http://localhost:5000/api/profile',
    headers=headers
)

print(response.json())
```

---

## Session-Based Authentication

### Flask-Login Example
```python
from flask import Flask, request, jsonify, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    """User model"""
    def __init__(self, id, username):
        self.id = id
        self.username = username

# User database
USERS = {
    '1': User('1', 'alice'),
    '2': User('2', 'bob')
}

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID"""
    return USERS.get(user_id)

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint"""
    data = request.get_json()
    username = data.get('username')

    # Find user (simplified)
    for user in USERS.values():
        if user.username == username:
            login_user(user)
            return jsonify({'message': 'Logged in successfully'})

    return jsonify({'error': 'User not found'}), 404

@app.route('/logout')
@login_required
def logout():
    """Logout endpoint"""
    logout_user()
    return jsonify({'message': 'Logged out'})

@app.route('/profile')
@login_required
def profile():
    """Protected endpoint"""
    from flask_login import current_user
    return jsonify({'username': current_user.username})

# Install: pip install flask-login
```

---

## Best Practices

### 1. Never Hardcode Credentials
```python
# Bad
API_KEY = 'sk-1234567890abcdef'

# Good
import os
API_KEY = os.getenv('API_KEY')
```

### 2. Use HTTPS
```python
# All authentication should use HTTPS
# HTTP sends credentials in plain text!

# Good
BASE_URL = 'https://api.example.com'

# Bad (for production)
BASE_URL = 'http://api.example.com'
```

### 3. Set Token Expiration
```python
# Tokens should expire
payload = {
    'user_id': 1,
    'exp': datetime.utcnow() + timedelta(hours=24)  # Expires in 24h
}
```

### 4. Store Tokens Securely
```python
# Client-side: Use httpOnly cookies or secure storage
# Server-side: Hash/encrypt sensitive data
# Never store in localStorage for sensitive apps
```

### 5. Implement Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.headers.get('X-API-Key'))

@app.route('/api/data')
@limiter.limit("100 per day")
def get_data():
    return jsonify({'data': [1, 2, 3]})

# Install: pip install Flask-Limiter
```

### 6. Validate Tokens Properly
```python
def verify_token(token):
    """Always validate tokens"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        # Check expiration
        if datetime.utcnow() > datetime.fromtimestamp(payload['exp']):
            return None

        return payload

    except jwt.InvalidTokenError:
        return None
```

---

## Complete Examples

### Complete JWT API
```python
#!/usr/bin/env python3
"""
Complete JWT Authentication API
"""

from flask import Flask, request, jsonify
from functools import wraps
import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'

# User database (use real database in production)
USERS = {}

def create_token(user_id):
    """Create JWT token"""
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

def token_required(f):
    """Decorator for protected routes"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'error': 'Bearer token malformed'}), 401

        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = USERS.get(data['user_id'])

            if not current_user:
                return jsonify({'error': 'User not found'}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/api/register', methods=['POST'])
def register():
    """Register new user"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    if username in [u['username'] for u in USERS.values()]:
        return jsonify({'error': 'Username already exists'}), 400

    user_id = len(USERS) + 1
    USERS[user_id] = {
        'id': user_id,
        'username': username,
        'password': generate_password_hash(password)
    }

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    """Login and get token"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    for user in USERS.values():
        if user['username'] == username:
            if check_password_hash(user['password'], password):
                token = create_token(user['id'])
                return jsonify({'access_token': token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/profile')
@token_required
def profile(current_user):
    """Get user profile"""
    return jsonify({
        'id': current_user['id'],
        'username': current_user['username']
    })

@app.route('/api/protected')
@token_required
def protected(current_user):
    """Protected endpoint"""
    return jsonify({'message': f'Hello, {current_user["username"]}!'})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## See Also

- **[APIs and Requests Cheat Sheet](../cheatsheets/APIs_and_Requests_Cheat_Sheet.md)** - HTTP requests basics
- **[Flask REST API Development Guide](Flask_REST_API_Development_Guide.md)** - Building Flask APIs
- **[Error Handling Cheat Sheet](../cheatsheets/Error_Handling_Cheat_Sheet.md)** - Exception handling
- **[Python Basics Cheat Sheet](../cheatsheets/Python_Basics_Cheat_Sheet.md)** - Python fundamentals

---
