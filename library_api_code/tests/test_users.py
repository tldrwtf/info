from app.models import Users, db
from werkzeug.security import check_password_hash, generate_password_hash
from app.util.auth import encode_token

def test_create_user(client):
    payload = {
        "first_name": "test",
        "last_name": "user",
        "email": "test@user.com",
        "phone": "1234567890",
        "password": "password"
    }

    response = client.post('/users', json=payload)
    assert response.status_code == 201
    assert response.json['email'] == "test@user.com"

    # verify user is in database
    user = db.session.query(Users).filter_by(email="test@user.com").first()
    assert user is not None
    assert check_password_hash(user.password, "password")


def test_invalid_create(client):
    payload = {
        "first_name": "test",
        "email": "test@user.com",
        # Missing required fields
    }

    response = client.post('/users', json=payload)
    assert response.status_code == 400


def test_get_users(client):
    # Create a dummy user
    user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password="password")
    db.session.add(user)
    db.session.commit()

    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) == 1


def test_login(client):
    user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password=generate_password_hash("password"))
    db.session.add(user)
    db.session.commit()

    payload = {
        "email": "test@user.com",
        "password": "password"
    }

    response = client.post('/users/login', json=payload)
    assert response.status_code == 200
    assert 'token' in response.json


def test_delete(client):
    user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password="password")
    db.session.add(user)
    db.session.commit()

    token = encode_token(user.id)
    headers = {'Authorization': f'Bearer {token}'}

    response = client.delete('/users', headers=headers)
    assert response.status_code == 200
    assert db.session.get(Users, user.id) is None


def test_unauthorized_delete(client):
    response = client.delete('/users')
    assert response.status_code == 401  # Unauthorized


def test_update(client):
    user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password="password")
    db.session.add(user)
    db.session.commit()

    token = encode_token(user.id)
    headers = {'Authorization': f'Bearer {token}'}

    payload = {
        "first_name": "Updated"
    }

    response = client.put('/users', json=payload, headers=headers)
    assert response.status_code == 200

    updated_user = db.session.get(Users, user.id)
    assert updated_user.first_name == "Updated"


def test_nonunique_email(client):
    user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password="password")
    db.session.add(user)
    db.session.commit()

    payload = {
        "first_name": "test2",
        "last_name": "user2",
        "email": "test@user.com",  # Same email
        "phone": "1234567890",
        "password": "password"
    }

    response = client.post('/users', json=payload)
    assert response.status_code == 400