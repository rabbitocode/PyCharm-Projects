import requests

class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/fc9a5c59fc8b032b3b004335d733164b/copyOfFlightDeals/prices"
        self.SHEETY_EMAIL_LIST = "https://api.sheety.co/fc9a5c59fc8b032b3b004335d733164b/copyOfFlightDeals/email"
        self.SHEETY_HEADER = {
            "Authorization": "Bearer KIj3i21n3kSMEnase94"
        }
        self.destination_data = {}

    def Call(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.SHEETY_HEADER)
        response.raise_for_status()
        result = response.json()
        self.destination_data = result["prices"]
        return result

    def UpdateIata(self, row_id, iata_code):
        """Update a specific row in Sheety with a new IATA code."""
        new_data = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(
            url=f"{self.SHEETY_ENDPOINT}/{row_id}",
            json=new_data,
            headers=self.SHEETY_HEADER
        )
        response.raise_for_status()  # Check if request was successful
        print(response.json())  # Print the response for debugging

    def UpdateFlightPrice(self, row_id, flight_price):
        """Update a specific row in Sheety with flight price information."""
        new_data = {
            "price": {
                "flightPrice": flight_price
            }
        }
        response = requests.put(
            url=f"{self.SHEETY_ENDPOINT}/{row_id}",
            json=new_data,
            headers=self.SHEETY_HEADER
        )
        response.raise_for_status()  # Check if request was successful
        print(response.json())  # Print the response for debugging