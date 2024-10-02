import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations"

    def AuthenticateToken(self):
        API_KEY = "Ynlbe1XT2hIYigRqEsVEsxG2G8JpNNft"
        API_SECRET = "iBD3sBF8zctKb8BI"

        AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

        AUTH_DATA = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET,
        }

        H = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        auth = requests.post(url=AUTH_ENDPOINT, data=AUTH_DATA, headers=H)
        auth.raise_for_status()
        r = auth.json()
        bearer_token = r['access_token']
        return bearer_token

    def IataCodeSearch(self, city):
        self.header = {
            "Authorization": f"Bearer {self.AuthenticateToken()}"
        }

        # Try with just the required parameters
        self.parameters = {
            "subType": "AIRPORT",
            "keyword": city,
        }

        response = requests.get(url=self.AMADEUS_ENDPOINT, params=self.parameters, headers=self.header)

        # Debugging print statements
        print(response.url)  # This will print the full URL being requested
        print(response.status_code)
        print(response.text)  # Print response content for debugging

        response.raise_for_status()  # Raise an error if the status code is 4xx/5xx
        result = response.json()

        return result
