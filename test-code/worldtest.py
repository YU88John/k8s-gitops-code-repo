import unittest
import sys
import os

# Get the absolute path to the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the paths to match your project structure
sys.path.append(os.path.join(current_dir, '../hello_world_service'))
sys.path.append(os.path.join(current_dir, '../happy_world_service'))

from hello_world_service.app import app_hello
from happy_world_service.app import app_happy


class TestHappyApp(TestCase):
    def create_app(self):
        app_happy.config['TESTING'] = True
        return app_happy

    def test_happy_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Happy World! This is the Happy microservice.')

    def test_get_happy_endpoint(self):
        response = self.client.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn('And Happy from the Happy microservice!', response.json['message'])

class TestHelloApp(TestCase):
    def create_app(self):
        app_hello.config['TESTING'] = True
        return app_hello

    def test_hello_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World! This is the Hello microservice.')

    def test_get_hello_endpoint(self):
        response = self.client.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello from the Hello microservice!', response.json['message'])

if __name__ == '__main__':
    unittest.main()
