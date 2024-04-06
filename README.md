# Groww Stock Analysis App

This Flask application fetches data from an API endpoint and provides functionality to find the stock with the maximum net profit margin, market capitalization, volume etc.

## Prerequisites

- Python 3.x
- Flask
- Requests library (install via pip: `pip install requests`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-stock-analysis-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-stock-analysis-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set the appropriate URL in the Flask app to fetch data from the API. Update the `YOUR_URL_HERE` placeholder in the all the functions in `server.py` with the actual API endpoint URL.

2. Run the Flask app:

    ```bash
    python server.py
    ```

3. Access the application in your web browser at `http://localhost:5000/max_net_profit_margin_stock` to find the stock with the maximum net profit margin.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have any feature requests.
