# Real-Time Web Guide: WebSockets & Flask-SocketIO

This guide covers the fundamental concepts of real-time web communication using WebSockets and demonstrates how to implement them using Python (Flask) and JavaScript.

## Table of Contents
1. [Concepts: HTTP vs WebSockets](#concepts-http-vs-websockets)
2. [The WebSocket Protocol](#the-websocket-protocol)
3. [Server-Side Implementation (Flask-SocketIO)](#server-side-implementation-flask-socketio)
4. [Client-Side Implementation (JavaScript)](#client-side-implementation-javascript)
5. [Project: Real-Time Chat Room](#project-real-time-chat-room)

---

## Concepts: HTTP vs WebSockets

### Traditional HTTP (Request-Response)
*   **Model:** Client requests -> Server responds.
*   **Limitation:** The server cannot "push" data to the client. The client must ask for updates (polling), which is inefficient and high-latency.
*   **Analogy:** sending a letter and waiting for a reply.

### WebSockets (Full-Duplex)
*   **Model:** A persistent, open connection between client and server.
*   **Advantage:** Both parties can send data at *any time*. Extremely low latency.
*   **Analogy:** A phone call.

| Feature | HTTP | WebSocket |
| :--- | :--- | :--- |
| **Connection** | Short-lived (per request) | Persistent (long-lived) |
| **Communication** | One-way (Client initiates) | Two-way (Bidirectional) |
| **Overhead** | High (Headers per request) | Low (Initial handshake only) |
| **Use Cases** | REST APIs, Websites | Chat, Games, Live Feeds |

---

## The WebSocket Protocol

1.  **Handshake:** The client sends a standard HTTP request with an `Upgrade: websocket` header. The server responds with `101 Switching Protocols`.
2.  **Frames:** Data is exchanged in "frames" (binary packets).
3.  **Events:** The protocol is event-driven (`onopen`, `onmessage`, `onclose`).

---

## Server-Side Implementation (Flask-SocketIO)

We use `flask-socketio` to handle WebSocket connections in a Flask app.

### Installation
```bash
pip install flask flask-socketio eventlet
```
*Note: `eventlet` or `gevent` is recommended for production performance.*

### Basic Server Structure (`app.py`)

```python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# cors_allowed_origins='*' allows connections from any domain (dev only)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

# --- Event Handlers ---

@socketio.on('connect')
def handle_connect():
    print('Client Connected')
    # Optional: Send a welcome message just to this client
    emit('message', {'data': 'Welcome to the server!'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client Disconnected')

@socketio.on('message') # Custom event name 'message'
def handle_custom_message(data):
    print(f"Received: {data}")
    # Broadcast to ALL clients
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    # Use socketio.run instead of app.run
    socketio.run(app, debug=True)
```

---

## Client-Side Implementation (JavaScript)

Modern browsers support the native `WebSocket` API, but the `Socket.IO` client library is preferred when using Flask-SocketIO because it handles reconnection and fallbacks automatically.

### HTML Setup
Include the Socket.IO client library (CDN):
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
```

### JavaScript Logic
```javascript
// Connect to the server
const socket = io();

// Listen for connection
socket.on('connect', () => {
    console.log("Connected to server!");
    socket.emit('message', 'Hello from Client!');
});

// Listen for incoming messages
socket.on('message', (data) => {
    console.log("Server says:", data);
    // Update UI here
});

// Send a message
function sendMessage(text) {
    socket.emit('message', text);
}
```

---

## Project: Real-Time Chat Room

This simple project demonstrates a chat interface where multiple users can talk in real-time.

### 1. Backend (`app.py`)
```python
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route("/")
def home():
    return render_template('base.html')

@socketio.on('message')
def handle_message(msg):
    print(f'Message: {msg}')
    # Broadcast the message back to all clients so they see it
    socketio.emit('message', msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)
```

### 2. Frontend (`templates/base.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WebSocket Chat</title>
</head>
<body>
    <h1>Chat Room</h1>
    <div id="chat-box" style="border:1px solid #ccc; height:300px; overflow-y:scroll; padding:10px;">
        <!-- Messages appear here -->
    </div>
    
    <form id="message-form">
        <input type="text" id="message-input" autocomplete="off" placeholder="Type a message...">
        <button type="submit">Send</button>
    </form>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script>
        const socket = io();
        const chatBox = document.getElementById('chat-box');
        const form = document.getElementById('message-form');
        const input = document.getElementById('message-input');

        // 1. Handle Form Submit
        form.onsubmit = (e) => {
            e.preventDefault();
            const msg = input.value;
            if (msg) {
                socket.emit('message', msg); // Send to server
                input.value = ''; // Clear input
            }
        };

        // 2. Handle Incoming Messages
        socket.on('message', (msg) => {
            const p = document.createElement('p');
            p.textContent = msg;
            chatBox.appendChild(p);
            // Auto-scroll to bottom
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    </script>
</body>
</html>
```
