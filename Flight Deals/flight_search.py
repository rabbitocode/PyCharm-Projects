import requests
from datetime import datetime, timedelta

import requests
from datetime import datetime, timedelta

# Keys are inactive
class FlightSearch:
    def __init__(self):
        self.AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.API_KEY = "Ynlbe1XT2hIYigRqEsVEsxG2G8JpNNft"
        self.API_SECRET = "iBD3sBF8zctKb8BI"
        self.access_token = self.AuthenticateToken()
        self.IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations"

    def AuthenticateToken(self):
        AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        AUTH_DATA = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET,
        }
        response = requests.post(url=AUTH_ENDPOINT, data=AUTH_DATA)
        response.raise_for_status()
        return response.json()['access_token']

    def GetDates(self):
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        six_months_later = today + timedelta(days=180)
        return tomorrow.date().strftime("%Y-%m-%d"), six_months_later.date().strftime("%Y-%m-%d")

    def IataCodeSearch(self, city):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "subType": "AIRPORT",
            "keyword": city,
        }
        response = requests.get(url=self.IATA_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        result = response.json()

        if not result['data']:
            print(f"No IATA code found for city: {city}")
            return None

        return result['data'][0]["iataCode"]

    def SearchFlights(self, origin, destination, departure_date, return_date, max_price):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "currencyCode": "EUR",  # Ensure currency code is correct
            "maxPrice": max_price,
            "nonStop": "true"  # Boolean value as string
        }
        try:
            response = requests.get(url=self.AMADEUS_ENDPOINT, headers=headers, params=params)
            response.raise_for_status()
            result = response.json()
            return result
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None

