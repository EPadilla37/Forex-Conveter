
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

#Set exchange rate API endpoint URL
API_ENDPOINT = 'https://api.exchangerate.host/latest'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/exchange_rate", methods=['GET'])
def exchange_rate():
    base_currency = request.args.get('base')
    target_currency = request.args.get('target')
    amount = request.args.get('amount')

    # Check if input fields are not empty
    if base_currency == '' or target_currency == '' or amount == '':
        error = 'Please fill in all fields'
        return render_template('index.html', error=error)

    # Make request to API
    params = {'base': base_currency, 'symbols': target_currency}
    response = requests.get(API_ENDPOINT, params=params)

    # Check if API request was successful
    if response.status_code == 200:
        data = response.json()

        # Check if given currencies exist in the API
        if not data.get('rates') or not data['rates'].get(target_currency):
            error = 'Please enter a valid currency'
            return render_template('index.html', error=error)

        exchange_rate = data['rates'][target_currency]

        converted_value = float(amount) * exchange_rate

        results = {'converted_value': converted_value,
                   'exchange_rate': exchange_rate}
        return render_template('results.html', results=results)
    else:
        return jsonify({'error', 'failed to get exchange rate'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

