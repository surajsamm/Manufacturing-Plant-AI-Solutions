import os
import requests

# ======================
# Stock Price (Alpha Vantage)
# ======================
def get_stock_price(ticker: str) -> str:
    """
    Fetch latest stock price for a given ticker using Alpha Vantage API.

    Args:
        ticker (str): Stock symbol (e.g., "TSLA", "AAPL").

    Returns:
        str: Latest stock price or error message.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

    if not api_key:
        # Mocked response if no API key
        return f"[Mocked] Stock price for {ticker}: $250.00"

    url = (
        f"https://www.alphavantage.co/query"
        f"?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            price = data["Global Quote"]["05. price"]
            return f"Stock price for {ticker}: ${float(price):,.2f}"
        else:
            return f"Error: No stock data found for {ticker}."

    except Exception as e:
        return f"Error fetching stock data: {e}"


# ======================
# Weather (OpenWeather)
# ======================
def get_weather(city: str) -> str:
    """
    Fetch current weather for a given city using OpenWeather API.

    Args:
        city (str): City name (e.g., "Berlin", "New York").

    Returns:
        str: Current weather description or error message.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        # Mocked response if no API key
        return f"[Mocked] Weather in {city}: Sunny, 25°C"

    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "weather" in data and "main" in data:
            desc = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            return f"Weather in {city}: {desc}, {temp:.1f}°C"
        else:
            return f"Error: No weather data found for {city}."

    except Exception as e:
        return f"Error fetching weather data: {e}"
