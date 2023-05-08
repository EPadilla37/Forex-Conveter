import unittest
from app import app


class AppTestCase(unittest.TestCase):
    
    # test if the home page is rendered correctly
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Exchange Rate Converter", response.data)
    
    # test if the exchange_rate page is rendered correctly with valid inputs
    def test_exchange_rate_valid_inputs(self):
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=USD&target=EUR&amount=100")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Conversion Results", response.data)
        self.assertIn(b"100.00 USD = 83.70 EUR", response.data)
    
    # test if the exchange_rate page is rendered correctly with invalid currency
    def test_exchange_rate_invalid_currency(self):
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=USD&target=invalid&amount=100")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a valid currency", response.data)
    
    # test if the exchange_rate page is rendered correctly with empty fields
    def test_exchange_rate_empty_fields(self):
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=&target=&amount=")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please fill in all fields", response.data)
    
    # test if the exchange_rate page is rendered correctly with non-numeric amount
    def test_exchange_rate_non_numeric_amount(self):
        tester = app.test_client(self)
        response = tester.get("/exchange_rate?base=USD&target=EUR&amount=invalid")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a valid number", response.data)


if __name__ == "__main__":
    unittest.main()
