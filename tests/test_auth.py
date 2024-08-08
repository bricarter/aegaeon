import unittest

from flask import get_flashed_messages

from app import create_app


class TestAuth(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        cls.test_data = {"register": {
                        "email": "register@email.com", 
                        "password": "register", 
                        "confirm_password": "register",
                        "first_name": "register", 
                        "last_name": "register"
                        },
                        "login": {
                        "email": "administration@gmail.com", 
                        "password": "10987654321",
                        "first_name": "Vulnerable"
                        }}

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        
        # valid registration
        response = self.client.post('/register', data= self.test_data["register"], follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.history), 1)
        self.assertEqual(response.request.path, f'/home/{self.test_data["register"]["first_name"]}')

        # invalid registration: 
        # passwords do not match
        self.test_data["register"]["email"] = "Register@gmail.com"
        self.test_data["register"]["confirm_password"] = "Register"
        with self.client:
            response = self.client.post('/register', data= self.test_data["register"])
            self.assertEqual(response.status_code, 200)
            flashed_messages = get_flashed_messages(with_categories=True)
            self.assertEqual(flashed_messages[0], ("error", "passwords do not match"))

        # invalid registration: 
        # account already exists
        self.test_data["register"]["email"] = "administration@gmail.com"
        with self.client:
            response = self.client.post('/register', data= self.test_data["register"], follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            flashed_messages = get_flashed_messages(with_categories=True)
            self.assertEqual(flashed_messages[0], ("error", "that email is already in use, please login."))
            self.assertEqual(len(response.history), 1)
            self.assertEqual(response.request.path, "/login")

    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        
        # valid registration
        response = self.client.post('/login', data= self.test_data["login"], follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.history), 1)
        self.assertEqual(response.request.path, f'/home/{self.test_data["login"]["first_name"]}')

        # invalid registration: 
        # password doesn't match account
        self.test_data["login"]["password"] = "12345678910"
        with self.client:
            response = self.client.post('/login', data= self.test_data["login"])
            self.assertEqual(response.status_code, 200)
            flashed_messages = get_flashed_messages(with_categories=True)
            self.assertEqual(flashed_messages[0], ("error", "email or password error"))

        # invalid registration: 
        # account doesn't exist
        self.test_data["login"]["email"] = "login@gmail.com"
        with self.client:
            response = self.client.post('/login', data= self.test_data["login"])
            self.assertEqual(response.status_code, 200)
            flashed_messages = get_flashed_messages(with_categories=True)
            self.assertEqual(flashed_messages[0], ("error", "email or password error"))

    def test_logout(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.history), 1)
        self.assertEqual(response.request.path, "/login")