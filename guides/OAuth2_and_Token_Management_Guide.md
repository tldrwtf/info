# OAuth2 and Token Management Guide

---

## Table of Contents

1. [Introduction to OAuth2](#introduction-to-oauth2)
2. [Client Credentials Flow](#client-credentials-flow)
3. [PKCE Authorization Code Flow](#pkce-authorization-code-flow)
4. [Base64 Encoding for Credentials](#base64-encoding-for-credentials)
5. [Token Acquisition and Storage](#token-acquisition-and-storage)
6. [Bearer Token Usage](#bearer-token-usage)
7. [Token Lifecycle Management](#token-lifecycle-management)
8. [Error Handling](#error-handling)
9. [Security Best Practices](#security-best-practices)
10. [Complete Implementation Example](#complete-implementation-example)
11. [Common Pitfalls and Solutions](#common-pitfalls-and-solutions)

---

## Introduction to OAuth2

OAuth2 is an authorization framework that enables applications to obtain limited access to user accounts or services. It works by delegating user authentication to the service that hosts the user account.

### OAuth2 vs API Keys

**API Key Authentication:**
```python
headers = {
    "X-API-Key": "your_api_key_here"
}
response = requests.get(url, headers=headers)
```

**OAuth2 Token Authentication:**
```python
# Step 1: Obtain token
token = get_access_token()

# Step 2: Use token in requests
headers = {
    "Authorization": f"Bearer {token}"
}
response = requests.get(url, headers=headers)
```

### When to Use OAuth2

- Server-to-server authentication
- Third-party service integration
- Delegated access (user doesn't share password)
- Short-lived, revocable access tokens
- Multiple permission scopes

---

## Client Credentials Flow

The Client Credentials flow is used for machine-to-machine authentication without user interaction.

### Flow Diagram

```
Your Application
      |
      | 1. POST credentials
      v
Token Endpoint (e.g., https://accounts.spotify.com/api/token)
      |
      | 2. Validate credentials
      | 3. Generate token
      |
      | 4. Return access token
      v
Your Application
      |
      | 5. Use token for API requests
      v
API Endpoint
```

### Complete Implementation

```python
import requests
import base64
from datetime import datetime, timedelta

def get_access_token(client_id, client_secret):
    """
    Obtain OAuth2 access token using client credentials flow.

    Args:
        client_id: Your application's client ID
        client_secret: Your application's client secret

    Returns:
        str: Access token, or None if request fails
    """
    # Token endpoint URL
    url = "https://accounts.spotify.com/api/token"

    # Combine credentials
    cred_string = f"{client_id}:{client_secret}"

    # Encode to base64
    byte_creds = cred_string.encode('utf-8')
    b64_string = base64.b64encode(byte_creds).decode('utf-8')

    # Prepare request
    headers = {
        "Authorization": f"Basic {b64_string}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    # Make request
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)

        if response.status_code == 200:
            token_data = response.json()
            return token_data['access_token']
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
```

### Understanding Each Component

**1. Credential String:**
```python
cred_string = f"{client_id}:{client_secret}"
# Example: "my_client_id:my_client_secret"
```

**2. Authorization Header:**
```python
headers = {
    "Authorization": f"Basic {b64_string}"
}
# Example: "Basic bXlfY2xpZW50X2lkOm15X2NsaWVudF9zZWNyZXQ="
```

**3. Grant Type:**
```python
data = {
    "grant_type": "client_credentials"  # Specifies the OAuth2 flow
}
```

**4. Response Structure:**
```json
{
    "access_token": "BQC8K3Xr...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "scope": "user-read-private user-read-email"
}
```

## PKCE Authorization Code Flow

Use PKCE when you cannot keep a client secret (SPAs/mobile). The `API-Authentication-Spotify-` repo demonstrates this flow for Spotify. Core steps:

1. Generate a high-entropy `code_verifier` on the client and derive `code_challenge = base64url(sha256(verifier))` (no padding).
2. Redirect to the provider's authorize URL with `response_type=code`, `code_challenge`, `code_challenge_method=S256`, requested scopes, and `redirect_uri`.
3. On callback, send `grant_type=authorization_code`, the `code`, the original `code_verifier`, and `redirect_uri` to the token endpoint. No client secret is sent from the browser.
4. Persist `access_token` and `refresh_token`; refresh with `grant_type=refresh_token` plus the same `code_verifier` when `expires_in` is near zero.

Minimal generator (JavaScript) for verifier/challenge:

```javascript
// Generate verifier and challenge for PKCE (client-side)
const generateVerifier = () =>
  [...crypto.getRandomValues(new Uint8Array(64))]
    .map(v => ("0" + v.toString(16)).slice(-2))
    .join("");

const generateChallenge = async (verifier) => {
  const data = new TextEncoder().encode(verifier);
  const digest = await crypto.subtle.digest("SHA-256", data);
  // base64url encode without padding
  return btoa(String.fromCharCode(...new Uint8Array(digest)))
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
};
```

Operational tips:

- Store tokens securely (session storage for browser, secure storage for mobile) and track expiry timestamps to refresh before a 401 occurs.
- Keep scopes minimal; for Spotify, profile scopes differ from playlist scopes. Match your redirect URI to the registered app entry exactly.
- Cross-link with [API_Authentication_Guide.md](API_Authentication_Guide.md) for end-to-end examples and error handling patterns.

---

## Base64 Encoding for Credentials

Base64 encoding converts binary data into ASCII text format, making it safe to transmit over HTTP.

### Why Base64?

- Makes credentials web-safe for HTTP headers
- Handles special characters in client ID/secret
- Standard encoding for Basic authentication
- **NOT encryption** - just encoding for transport

### Implementation

```python
import base64

def encode_credentials(client_id, client_secret):
    """Encode credentials in Base64 format for OAuth2."""

    # Step 1: Combine with colon separator
    cred_string = f"{client_id}:{client_secret}"

    # Step 2: Convert to bytes
    byte_creds = cred_string.encode('utf-8')

    # Step 3: Encode to base64
    b64_bytes = base64.b64encode(byte_creds)

    # Step 4: Convert back to string
    b64_string = b64_bytes.decode('utf-8')

    return b64_string

# Usage
encoded = encode_credentials("my_id", "my_secret")
print(encoded)  # "bXlfaWQ6bXlfc2VjcmV0"
```

### Decoding (for demonstration only)

```python
def decode_credentials(b64_string):
    """Decode base64 credentials (demonstration only)."""
    decoded_bytes = base64.b64decode(b64_string)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

# This shows Base64 is NOT secure encryption
decoded = decode_credentials("bXlfaWQ6bXlfc2VjcmV0")
print(decoded)  # "my_id:my_secret"
```

**Security Note:** Always use HTTPS. Base64 encoding provides NO security on its own.

---

## Token Acquisition and Storage

### Basic Token Storage

```python
class TokenManager:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expiry = None

    def get_token(self):
        """Get valid access token (fetch new if needed)."""
        if self._is_token_valid():
            return self.access_token

        return self._fetch_new_token()

    def _is_token_valid(self):
        """Check if current token is still valid."""
        if not self.access_token or not self.token_expiry:
            return False

        import time
        return time.time() < self.token_expiry

    def _fetch_new_token(self):
        """Fetch a new access token from the server."""
        url = "https://accounts.spotify.com/api/token"

        # Encode credentials
        cred_string = f"{self.client_id}:{self.client_secret}"
        b64_string = base64.b64encode(
            cred_string.encode('utf-8')
        ).decode('utf-8')

        headers = {
            "Authorization": f"Basic {b64_string}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}

        response = requests.post(url, headers=headers, data=data, timeout=10)

        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data['access_token']

            # Set expiry (subtract 60 seconds for safety margin)
            import time
            self.token_expiry = time.time() + token_data['expires_in'] - 60

            return self.access_token
        else:
            raise Exception(f"Token fetch failed: {response.status_code}")
```

### Usage

```python
# Initialize once
token_manager = TokenManager(
    client_id="your_client_id",
    client_secret="your_client_secret"
)

# Use throughout application
token = token_manager.get_token()  # Fetches new token
token = token_manager.get_token()  # Returns cached token
```

---

## Bearer Token Usage

Bearer tokens are included in the Authorization header of API requests.

### Basic Usage

```python
def make_authenticated_request(url, token):
    """Make API request with Bearer token."""
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed: {response.status_code}")
```

### Complete API Client

```python
class SpotifyClient:
    def __init__(self, client_id, client_secret):
        self.token_manager = TokenManager(client_id, client_secret)
        self.base_url = "https://api.spotify.com/v1"

    def _get_headers(self):
        """Get headers with current access token."""
        token = self.token_manager.get_token()
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def search_track(self, query, limit=1):
        """Search for a track."""
        url = f"{self.base_url}/search"
        params = {
            "q": query,
            "type": "track",
            "limit": limit
        }

        response = requests.get(
            url,
            headers=self._get_headers(),
            params=params
        )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            # Token expired, retry once with new token
            self.token_manager.access_token = None
            response = requests.get(
                url,
                headers=self._get_headers(),
                params=params
            )
            return response.json() if response.status_code == 200 else None
        else:
            raise Exception(f"Search failed: {response.status_code}")

    def get_artist(self, artist_id):
        """Get artist information."""
        url = f"{self.base_url}/artists/{artist_id}"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            return None
```

### Usage Example

```python
# Initialize client
client = SpotifyClient("your_id", "your_secret")

# Search for tracks
results = client.search_track("Bohemian Rhapsody")
track = results['tracks']['items'][0]
print(f"Found: {track['name']} by {track['artists'][0]['name']}")

# Get artist details
artist = client.get_artist(track['artists'][0]['id'])
print(f"Followers: {artist['followers']['total']}")
```

---

## Token Lifecycle Management

### Token Expiry Handling

```python
import time
from datetime import datetime, timedelta

class AdvancedTokenManager:
    def __init__(self, client_id, client_secret, token_endpoint):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_endpoint = token_endpoint

        self.access_token = None
        self.token_type = None
        self.expires_at = None
        self.scope = None

    def get_token(self):
        """Get valid token, refreshing if necessary."""
        if self._needs_refresh():
            self._refresh_token()

        return self.access_token

    def _needs_refresh(self):
        """Check if token needs refresh."""
        if not self.access_token:
            return True

        if not self.expires_at:
            return True

        # Refresh if less than 5 minutes remaining
        buffer_seconds = 300
        return time.time() >= (self.expires_at - buffer_seconds)

    def _refresh_token(self):
        """Fetch new access token."""
        cred_string = f"{self.client_id}:{self.client_secret}"
        b64_creds = base64.b64encode(cred_string.encode()).decode()

        headers = {
            "Authorization": f"Basic {b64_creds}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}

        response = requests.post(
            self.token_endpoint,
            headers=headers,
            data=data,
            timeout=10
        )

        if response.status_code == 200:
            token_data = response.json()
            self._store_token(token_data)
        else:
            raise Exception(f"Token refresh failed: {response.status_code}")

    def _store_token(self, token_data):
        """Store token and metadata."""
        self.access_token = token_data['access_token']
        self.token_type = token_data.get('token_type', 'Bearer')
        self.scope = token_data.get('scope', '')

        # Calculate expiry time
        expires_in = token_data.get('expires_in', 3600)
        self.expires_at = time.time() + expires_in

    def get_token_info(self):
        """Get information about current token."""
        if not self.access_token:
            return "No token available"

        remaining = self.expires_at - time.time() if self.expires_at else 0

        return {
            "token_type": self.token_type,
            "scope": self.scope,
            "expires_in": int(remaining),
            "expires_at": datetime.fromtimestamp(self.expires_at).isoformat()
        }
```

---

## Error Handling

### HTTP Status Codes

```python
def handle_auth_response(response):
    """Handle authentication response with proper error handling."""

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 400:
        # Bad Request - Invalid grant_type or malformed request
        error_data = response.json()
        raise ValueError(f"Bad Request: {error_data.get('error_description', 'Invalid request')}")

    elif response.status_code == 401:
        # Unauthorized - Invalid credentials
        raise PermissionError("Authentication failed: Invalid client ID or secret")

    elif response.status_code == 403:
        # Forbidden - Valid credentials but insufficient permissions
        raise PermissionError("Access forbidden: Insufficient permissions")

    elif response.status_code == 429:
        # Too Many Requests - Rate limited
        retry_after = response.headers.get('Retry-After', 60)
        raise Exception(f"Rate limited. Retry after {retry_after} seconds")

    elif response.status_code >= 500:
        # Server Error
        raise Exception(f"Server error: {response.status_code}")

    else:
        raise Exception(f"Unexpected error: {response.status_code} - {response.text}")
```

### Comprehensive Error Handling

```python
import requests
from requests.exceptions import Timeout, ConnectionError, RequestException

def safe_token_request(client_id, client_secret, token_url):
    """Make token request with comprehensive error handling."""

    try:
        # Prepare request
        cred_string = f"{client_id}:{client_secret}"
        b64_creds = base64.b64encode(cred_string.encode()).decode()

        headers = {
            "Authorization": f"Basic {b64_creds}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}

        # Make request with timeout
        response = requests.post(
            token_url,
            headers=headers,
            data=data,
            timeout=10
        )

        # Handle response
        return handle_auth_response(response)

    except Timeout:
        raise Exception("Request timed out - check network connection")

    except ConnectionError:
        raise Exception("Connection failed - check network or endpoint URL")

    except ValueError as e:
        raise Exception(f"Invalid credentials or request: {e}")

    except PermissionError as e:
        raise Exception(f"Authorization error: {e}")

    except RequestException as e:
        raise Exception(f"Request failed: {e}")
```

### Retry Logic with Exponential Backoff

```python
import time
from functools import wraps

def retry_with_backoff(max_retries=3, backoff_factor=2):
    """Decorator for retry logic with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise

                    wait_time = backoff_factor ** attempt
                    print(f"Attempt {attempt + 1} failed: {e}")
                    print(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)

        return wrapper
    return decorator

@retry_with_backoff(max_retries=3, backoff_factor=2)
def fetch_token(client_id, client_secret, token_url):
    """Fetch token with automatic retry."""
    return safe_token_request(client_id, client_secret, token_url)
```

---

## Security Best Practices

### 1. Credential Storage

**Bad Practice:**
```python
# NEVER hardcode credentials
client_id = "abc123"
client_secret = "secret456"
```

**Good Practice:**
```python
import os
from dotenv import load_dotenv

# Load from environment variables
load_dotenv()
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

if not client_id or not client_secret:
    raise ValueError("Missing required credentials")
```

**.env file:**
```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_secret_here
```

**.gitignore:**
```
.env
credentials.json
config/secrets.py
```

### 2. HTTPS Only

```python
def validate_token_url(url):
    """Ensure token endpoint uses HTTPS."""
    if not url.startswith('https://'):
        raise ValueError("Token endpoint must use HTTPS")
    return url

# Usage
token_url = validate_token_url("https://accounts.spotify.com/api/token")
```

### 3. Token Storage Security

```python
# Don't log tokens
logger.info(f"Token: {token}")  # BAD

# Don't store tokens in plain text files
with open('token.txt', 'w') as f:
    f.write(token)  # BAD

# Use secure storage (keyring example)
import keyring

# Store token securely
keyring.set_password("my_app", "access_token", token)

# Retrieve token
token = keyring.get_password("my_app", "access_token")
```

### 4. Input Validation

```python
def validate_credentials(client_id, client_secret):
    """Validate credential format."""
    if not isinstance(client_id, str) or not client_id:
        raise ValueError("Client ID must be a non-empty string")

    if not isinstance(client_secret, str) or not client_secret:
        raise ValueError("Client secret must be a non-empty string")

    if len(client_id) < 10:
        raise ValueError("Client ID appears invalid (too short)")

    return True
```

### 5. Request Timeout

```python
# Always set timeouts
response = requests.post(url, headers=headers, data=data, timeout=10)

# Or use session with default timeout
class TimeoutHTTPAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, timeout=10, *args, **kwargs):
        self.timeout = timeout
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        kwargs['timeout'] = kwargs.get('timeout') or self.timeout
        return super().send(request, **kwargs)

# Usage
session = requests.Session()
session.mount('https://', TimeoutHTTPAdapter(timeout=10))
```

### 6. Token Scoping

```python
# Request minimal scopes needed
data = {
    "grant_type": "client_credentials",
    "scope": "user-read-email user-read-private"  # Only what you need
}
```

---

## Complete Implementation Example

```python
import os
import base64
import time
import requests
from dotenv import load_dotenv
from typing import Optional, Dict, Any

class OAuth2Client:
    """Complete OAuth2 client with best practices."""

    def __init__(self, token_endpoint: str):
        # Load credentials from environment
        load_dotenv()
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')

        if not self.client_id or not self.client_secret:
            raise ValueError("Missing CLIENT_ID or CLIENT_SECRET")

        self.token_endpoint = self._validate_url(token_endpoint)

        # Token state
        self.access_token: Optional[str] = None
        self.token_type: str = "Bearer"
        self.expires_at: Optional[float] = None
        self.scope: Optional[str] = None

    @staticmethod
    def _validate_url(url: str) -> str:
        """Ensure URL uses HTTPS."""
        if not url.startswith('https://'):
            raise ValueError("Endpoint must use HTTPS")
        return url

    def get_token(self) -> str:
        """Get valid access token."""
        if self._is_token_valid():
            return self.access_token

        return self._fetch_new_token()

    def _is_token_valid(self) -> bool:
        """Check if current token is valid."""
        if not self.access_token or not self.expires_at:
            return False

        # Refresh if less than 5 minutes remaining
        buffer = 300
        return time.time() < (self.expires_at - buffer)

    def _fetch_new_token(self) -> str:
        """Fetch new access token."""
        # Encode credentials
        cred_string = f"{self.client_id}:{self.client_secret}"
        b64_creds = base64.b64encode(cred_string.encode()).decode()

        # Prepare request
        headers = {
            "Authorization": f"Basic {b64_creds}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}

        # Make request
        try:
            response = requests.post(
                self.token_endpoint,
                headers=headers,
                data=data,
                timeout=10
            )

            if response.status_code == 200:
                token_data = response.json()
                self._store_token(token_data)
                return self.access_token
            else:
                self._handle_error(response)

        except requests.exceptions.Timeout:
            raise Exception("Token request timed out")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection failed")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")

    def _store_token(self, token_data: Dict[str, Any]):
        """Store token and metadata."""
        self.access_token = token_data['access_token']
        self.token_type = token_data.get('token_type', 'Bearer')
        self.scope = token_data.get('scope', '')

        expires_in = token_data.get('expires_in', 3600)
        self.expires_at = time.time() + expires_in

    def _handle_error(self, response: requests.Response):
        """Handle error responses."""
        if response.status_code == 401:
            raise PermissionError("Invalid credentials")
        elif response.status_code == 429:
            retry_after = response.headers.get('Retry-After', 60)
            raise Exception(f"Rate limited. Retry after {retry_after}s")
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def make_request(self, url: str, method: str = 'GET', **kwargs) -> Dict[str, Any]:
        """Make authenticated API request."""
        token = self.get_token()

        headers = kwargs.get('headers', {})
        headers['Authorization'] = f"{self.token_type} {token}"
        kwargs['headers'] = headers

        response = requests.request(method, url, **kwargs)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            # Token might be expired, retry once
            self.access_token = None
            return self.make_request(url, method, **kwargs)
        else:
            raise Exception(f"Request failed: {response.status_code}")


# Usage Example
if __name__ == "__main__":
    # Initialize client
    client = OAuth2Client("https://accounts.spotify.com/api/token")

    # Make authenticated requests
    search_results = client.make_request(
        "https://api.spotify.com/v1/search",
        params={"q": "Thriller", "type": "track", "limit": 1}
    )

    track = search_results['tracks']['items'][0]
    print(f"Found: {track['name']} by {track['artists'][0]['name']}")
```

---

## Common Pitfalls and Solutions

### Pitfall 1: Fetching Token on Every Request

**Problem:**
```python
def search_song(query):
    token = get_token()  # Fetches new token every time!
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
```

**Solution:**
```python
# Use token manager that caches tokens
token_manager = TokenManager(client_id, client_secret)

def search_song(query):
    token = token_manager.get_token()  # Returns cached if valid
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
```

### Pitfall 2: No Error Handling

**Problem:**
```python
response = requests.post(url, headers=headers, data=data)
token = response.json()['access_token']  # Crashes if request fails!
```

**Solution:**
```python
try:
    response = requests.post(url, headers=headers, data=data, timeout=10)
    if response.status_code == 200:
        token = response.json()['access_token']
    else:
        raise Exception(f"Failed: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    token = None
```

### Pitfall 3: Hardcoded Credentials

**Problem:**
```python
client_id = "abc123"  # Committed to Git!
client_secret = "secret456"
```

**Solution:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
```

### Pitfall 4: No Request Timeout

**Problem:**
```python
response = requests.post(url, headers=headers, data=data)  # Hangs forever
```

**Solution:**
```python
response = requests.post(url, headers=headers, data=data, timeout=10)
```

### Pitfall 5: Ignoring Token Expiry

**Problem:**
```python
token = get_token()
# Use token for hours without checking expiry
```

**Solution:**
```python
class TokenManager:
    def get_token(self):
        if self._is_expired():
            self._refresh()
        return self.access_token
```

### Pitfall 6: Using HTTP Instead of HTTPS

**Problem:**
```python
url = "http://api.example.com/token"  # Insecure!
```

**Solution:**
```python
url = "https://api.example.com/token"  # Always HTTPS
```

---

### Related Resources

- [APIs & HTTP Requests](../cheatsheets/APIs_and_Requests_Cheat_Sheet.md)
- [API Authentication](API_Authentication_Guide.md)
- [Error Handling](../cheatsheets/Error_Handling_Cheat_Sheet.md)
- [Flask REST API Development](Flask_REST_API_Development_Guide.md)

[Back to Main](../README.md)
