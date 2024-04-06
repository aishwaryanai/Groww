import requests
from flask import render_template, request, Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('groww.html')

@app.route('/max_net_profit_margin_stock', methods=['GET'])
def max_net_profit_margin_stock():
    try:
        url = "YOUR_STOCK_DATA_API_URL_HERE"
        params = {
            "page": "0",
            "size": "10"
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'x-device-type': 'desktop',
            'x-platform': 'web'
        }
        
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        stocks = data.get('stocks')

        if not stocks:
            return jsonify({'message': 'No stocks found'}), 404

        max_net_profit_margin_stock = max(stocks, key=lambda x: x.get('stats', {}).get('netProfitMargin', float('-inf')))

        return jsonify(max_net_profit_margin_stock)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_company_info')
def get_company_info():
    try:
        url = "YOUR_STOCK_DATA_API_URL_HERE"
        params = {
            "page": "0",
            "size": "10"
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'x-device-type': 'desktop',
            'x-platform': 'web'
        }
        
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to fetch company info'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_stocks_data')
def get_stocks_data():
    url = "YOUR_STOCK_DATA_API_URL_HERE"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-app-id': 'growwWeb'
    }
    data = {
        "listFilters": {"INDUSTRY": [], "INDEX": []},
        "objFilters": {"CLOSE_PRICE": {"max": 100000, "min": 0}, "MARKET_CAP": {"min": 0, "max": 2000000000000000}},
        "page": "1",
        "size": "100",
        "sortBy": "NA",
        "sortType": "ASC"
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data'}), response.status_code
def fetch_stock_data():
    url = "YOUR_STOCK_DATA_API_URL_HERE"
    response = requests.get(url)
    data = response.json()
    return data['stocks']

# Function to sort stocks based on volume
def sort_stocks_by_volume(stocks):
    return sorted(stocks, key=lambda x: x['volume'], reverse=True)

@app.route('/sorted_stocks_by_volume', methods=['GET'])
def sorted_stocks_by_volume():
    stocks = fetch_stock_data()
    sorted_stocks = sort_stocks_by_volume(stocks)
    return jsonify(sorted_stocks)

def fetch_stock_data():
    url = "YOUR_STOCK_DATA_API_URL_HERE"
    response = requests.get(url)
    data = response.json()
    return data['stocks']

# Function to sort stocks based on market capitalization
def sort_stocks_by_market_cap(stocks):
    return sorted(stocks, key=lambda x: x['market_cap'], reverse=True)

@app.route('/sorted_stocks_by_market_cap', methods=['GET'])
def sorted_stocks_by_market_cap():
    stocks = fetch_stock_data()
    sorted_stocks = sort_stocks_by_market_cap(stocks)
    return jsonify(sorted_stocks)

def fetch_stock_data():
    url = "YOUR_STOCK_DATA_API_URL_HERE"
    response = requests.get(url)
    data = response.json()
    return data['stocks']

# Function to sort stocks based on market capitalization
def sort_stocks_by_market_cap(stocks):
    return sorted(stocks, key=lambda x: x['market_cap'], reverse=True)

if __name__ == '__main__':
    app.run(debug=True)