# Forex-Conveter

This is a Flask web application that allows users to convert currency using real-time exchange rates from an API.

Features:
- Convert currency from one currency to another.
- Validates user inputs for base currency, target currency, and amount.
- Retrieves exchange rates from an external API.
- Renders the conversion results on a results page.

Installation:
1. Clone the repository or download the source code.
2. Install the required dependencies 

Endpoints:
- GET /: Renders the home page of the application.
- GET /exchange_rate: Converts the specified amount from the base currency to the target currency and displays the results.

Testing:
1. The application includes unit tests implemented in the `test.py` file.
2. To run the tests, execute the following command: 'python test.py'

API Endpoint:
- The application uses the ExchangeRate API to fetch real-time exchange rates.
- The API endpoint URL is set to 'https://api.exchangerate.host/latest'.

