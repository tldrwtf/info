# Real-Time Web with Flask-SocketIO

This guide covers building real-time applications using Flask-SocketIO, enabling bidirectional communication between clients and servers.

## Quick Reference

| Feature | Concept | Implementation |
| :--- | :--- | :--- |
| **Protocol** | WebSocket | Persistent TCP connection |
| **Event** | Custom Signal | `socketio.emit('event_name', data)` |
| **Namespace** | Channel | `@socketio.on('event', namespace='/chat')` |
| **Room** | Group | `join_room(room_id)` / `to=room_id` |

---

## 1. Setup and Initialization

### Installation
```bash
pip install flask-socketio
```

### Application Factory Pattern
```python
from flask import Flask, render_template
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    
    # Initialize SocketIO with the app
    socketio.init_app(app, cors_allowed_origins="*")
    
    # Register blueprints/routes
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

# In run.py
if __name__ == '__main__':
    app = create_app()
    socketio.run(app, debug=True)
```

---

## 2. Handling Events

### Server-Side
```python
from flask_socketio import emit

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('server_message', {'data': 'Connected successfully'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('chat_message')
def handle_chat(data):
    # Broadcast to all connected clients
    emit('new_message', data, broadcast=True)
```

### Client-Side (JavaScript)
Include the Socket.IO client library:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
```

```javascript
const socket = io();

// Listen for connection
socket.on('connect', () => {
    console.log("Connected to server");
    socket.emit('chat_message', { user: "User1", text: "Hello!" });
});

// Listen for custom events
socket.on('new_message', (data) => {
    console.log("New message:", data.text);
    // Update DOM here
});
```

---

## 3. Rooms and Namespaces

### Rooms
Rooms allow you to target messages to a subset of connected clients (e.g., a specific chat room).

```python
from flask_socketio import join_room, leave_room

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('status', {'msg': f'{username} has entered the room.'}, to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('status', {'msg': f'{username} has left the room.'}, to=room)
```

### Sending to a Room
```python
@socketio.on('message')
def handle_room_message(data):
    room = data['room']
    emit('message', data, to=room)
```

---

## 4. Context & Authentication

### Accessing Request Context
SocketIO events run within a request context, so you can access `request`, `session`, and `current_user` (if using Flask-Login).

```python
from flask import request
from flask_login import current_user

@socketio.on('connect')
def connect_handler():
    if current_user.is_authenticated:
        print(f"User {current_user.id} connected")
    else:
        return False  # Reject connection
```

---

## 5. Deployment Considerations

*   **Async Mode:** Flask-SocketIO supports Eventlet, Gevent, and Werkzeug (dev only). Install `eventlet` or `gevent` for production.
*   **Gunicorn:** Use a worker class compatible with your async mode (e.g., `gunicorn -k eventlet -w 1 module:app`).
*   **Sticky Sessions:** If using multiple workers/nodes, sticky sessions (IP affinity) are required for the polling transport.

---

## See Also

- **[Flask REST API Development Guide](Flask_REST_API_Development_Guide.md)** - Traditional HTTP APIs.
- **[Intro to WebSockets Repo](../library_api_code/)** - (Reference implementation details).