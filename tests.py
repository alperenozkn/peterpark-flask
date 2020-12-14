import unittest
import json
from app import create_app, db
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class SignupTest(unittest.TestCase):

    def setUp(self):
        self.app, self.client = create_app(TestConfig)
        self.client = self.app.test_client()
        self.db = db
        self.db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_valid_plate(self):
        # Given
        payload = json.dumps({
            "plate": "XXX-X2123"
        })

        # When
        response = self.client.post('/plate', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual("Plate is a valid German plate.", response.json['message'])
        self.assertEqual(200, response.status_code)

    def test_malformed_request(self):
        # Given
        payload = json.dumps({
            "pate": "Mx-PP2123"
        })

        # When
        response = self.client.post('/plate', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual("Request body must include plate field.", response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_invalid_plate(self):
        # Given
        payload = json.dumps({
            "plate": "Mx-PP0123"
        })

        # When
        response = self.client.post('/plate', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual("Plate is not a valid German plate.", response.json['message'])
        self.assertEqual(422, response.status_code)
