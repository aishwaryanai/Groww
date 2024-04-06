# Groww Stock Screener App

We have developed a web application using Flask wherein the web application fetches data from an API endpoint and provides functionality to find the stock with the maximum net profit margin, market capitalization, volume etc. We've enhanced the user experience in the Groww app by transitioning filters from a vertical layout to a more intuitive horizontal format at the top. This adjustment ensures users easily recall their selected filters. Additionally, we've introduced new filters such as maximum net profit margin, market capitalization, and volume, enriching the stock screening capabilities beyond what was previously available in the Groww platform.  Furthermore, we've introduced a new feature allowing users to save their filters, a functionality not present in the current Groww app. This addition enables users to store and quickly access their preferred filter configurations, enhancing the overall user experience and streamlining the stock screening process.

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
