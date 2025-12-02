from app import create_app
from app.models import Users, db
import unittest
from werkzeug.security import check_password_hash, generate_password_hash
from app.util.auth import encode_token

# Ren Script: python -m unittest discover tests

class TestUsers(unittest.TestCase):
    
    #Runs before each test_method
    def setUp(self):
        self.app = create_app('TestingConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    #test creating a user (IMPORTANT all test functions need to start with test)
    def test_create_user(self):
        payload = {
            "first_name": "test",
            "last_name": "user",
            "email": "test@user.com",
            "phone": "1234567890",
            "password": "password"
        }

        response = self.client.post('/users', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['email'], "test@user.com")

        #verify user is in database
        user = db.session.query(Users).filter_by(email="test@user.com").first()
        self.assertIsNotNone(user)
        self.assertTrue(check_password_hash(user.password, "password"))

    #Negative check: See what happens when we intentionally try and break our endpoint
    def test_invalid_create(self):
        payload = {
            "first_name": "test",
            "email": "test@user.com",
            #Missing required fields
        }

        response = self.client.post('/users', json=payload)
        self.assertEqual(response.status_code, 400)

    def test_get_users(self):
        # Create a dummy user
        user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password="password")
        db.session.add(user)
        db.session.commit()

        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_login(self):
        user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password=generate_password_hash("password"))
        db.session.add(user)
        db.session.commit()

        payload = {
            "email": "test@user.com",
            "password": "password"
        }

        response = self.client.post('/users/login', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

    def test_delete(self):
        user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password="password")
        db.session.add(user)
        db.session.commit()

        token = encode_token(user.id)
        headers = {'Authorization': f'Bearer {token}'}

        response = self.client.delete('/users', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(db.session.get(Users, user.id))

    def test_unauthorized_delete(self):
        response = self.client.delete('/users')
        self.assertEqual(response.status_code, 401) #Unauthorized

    def test_update(self):
        user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password="password")
        db.session.add(user)
        db.session.commit()

        token = encode_token(user.id)
        headers = {'Authorization': f'Bearer {token}'}

        payload = {
            "first_name": "Updated"
        }

        response = self.client.put('/users', json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        
        updated_user = db.session.get(Users, user.id)
        self.assertEqual(updated_user.first_name, "Updated")

    def test_nonunique_email(self):
        user = Users(first_name="test", last_name="user", email="test@user.com", phone="123456", password="password")
        db.session.add(user)
        db.session.commit()

        payload = {
            "first_name": "test2",
            "last_name": "user2",
            "email": "test@user.com", #Same email
            "phone": "1234567890",
            "password": "password"
        }

        response = self.client.post('/users', json=payload)
        self.assertEqual(response.status_code, 400)