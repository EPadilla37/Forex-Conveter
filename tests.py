
import unittest
from unittest.mock import patch
from app import app


class AppTestCase(unittest.TestCase):
    
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Exchange Rate Converter", response.data)
    
    def test_exchange_rate_valid_inputs(self):
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=USD&target=EUR&amount=100")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Results", response.data)
        self.assertIn(b"Converted Value:", response.data)
        self.assertIn(b"Exchange Rate:", response.data)
    
    def test_exchange_rate_invalid_currency(self):
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=USD&target=invalid&amount=100")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a valid currency", response.data)
    
    def test_exchange_rate_empty_fields(self):
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=&target=&amount=")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please fill in all fields", response.data)
    
    def test_exchange_rate_non_numeric_amount(self):
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=USD&target=EUR&amount=invalid")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a valid number", response.data)
    
    @patch("app.requests.get")
    def test_exchange_rate_api_failure(self, mock_get):
        mock_get.return_value.status_code = 500
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=USD&target=EUR&amount=100")
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"Internal Server Error", response.data)


if __name__ == "__main__":
    unittest.main()
