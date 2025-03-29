import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetch_coindesk_info():
    url = "https://data-api.coindesk.com/info/v1/openapi"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print("CoinDesk API response:")
        print(data)
    except requests.RequestException as e:
        print(f"Error fetching CoinDesk data: {e}")

if __name__ == "__main__":
    fetch_coindesk_info()
