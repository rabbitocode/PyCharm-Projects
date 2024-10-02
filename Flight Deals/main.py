from pprint import pprint
import time
from data_manager import DataManager
from flight_search import *
from notification_manager import *

ORIGIN_CITY = "Copenhagen"
ORIGIN = "CPH"

# Initialize DataManager, FlightSearch, and NotificationManager
dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()

# Retrieve sheet data
sheet_data = dm.Call()

# Get dates for search
departure_date, return_date = fs.GetDates()

# Prepare list of destinations with their max price and city name
destinations = [
    {
        'iataCode': price_entry['iataCode'],
        'maxPrice': price_entry.get('lowestPrice', None),  # Use 'lowestPrice' as max price
        'city': price_entry.get('city', '')  # Include city name
    }
    for price_entry in sheet_data["prices"] if price_entry.get('iataCode')
]

# Update missing IATA codes in Sheety
for price_entry in sheet_data["prices"]:
    iata_code = price_entry.get('iataCode', '')

    # Skip if IATA code is already present
    if iata_code:
        continue

    try:
        # Get the IATA code using the city name
        iata_code = fs.IataCodeSearch(price_entry['city'])

        if not iata_code:
            print(f"No IATA code found for city: {price_entry['city']}")
            continue

        price_entry['iataCode'] = iata_code
        row_id = price_entry.get('id')

        if not row_id:
            print(f"Row ID missing for city: {price_entry['city']}")
            continue

        dm.UpdateIata(row_id, iata_code)

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 429:
            print("Slowing down search speed.")
            time.sleep(3)
    except Exception as e:
        print(f"An error occurred: {e}")

# Initialize a list to accumulate all email contents
email_list = []

# Search for flights
try:
    for destination in destinations:
        iata_code = destination['iataCode']
        max_price = destination['maxPrice']
        city_destination = destination['city']

        # Search flights for each destination
        flight_results = fs.SearchFlights(ORIGIN, iata_code, departure_date, return_date, max_price)

        if not flight_results:
            print(f"No flights found for {iata_code} within the max price.")
            continue

        print(f"Flights to {iata_code}:")

        if not flight_results.get('data'):
            print(f"No flight data returned for {iata_code}.")
            continue

        for flight in flight_results['data']:
            try:
                # Adjust the following line based on the actual response structure
                flight_price = float(flight['price']['total'].replace('EUR', '').strip())

                if flight_price > max_price:
                    print(f"Flight price for {iata_code} exceeds max price.")
                    continue

                print(f"Flight Price: €{flight_price}")

                # Extract specific details for the email
                departure_airport_iata = flight['itineraries'][0]['segments'][0]['departure']['iataCode']
                departure_datetime = flight['itineraries'][0]['segments'][0]['departure']['at']
                arrival_airport_iata = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']

                # Inbound flight details (assuming it's a return flight)
                return_departure_airport_iata = flight['itineraries'][1]['segments'][0]['departure']['iataCode']
                return_arrival_datetime = flight['itineraries'][1]['segments'][0]['arrival']['at']

                # Add the flight details to the email list
                email_content = f"""
                Flight Offer Details:

                Price: €{flight_price}

                Outbound Flight:
                - From {ORIGIN_CITY} To {city_destination}
                - Departure Airport: {departure_airport_iata}
                - Departure Date and Time: {departure_datetime}
                - Arrival Airport: {arrival_airport_iata}

                Return Flight:
                - From {city_destination} To {ORIGIN_CITY}
                - Departure Airport: {return_departure_airport_iata}
                - Arrival Date and Time: {return_arrival_datetime}
                """
                email_list.append(email_content)

                pprint(flight)  # Print the full response for debugging

            except KeyError as e:
                print(f"Price information missing in the result: {e}")
            except ValueError as e:
                print(f"Error converting price to float: {e}")

except requests.exceptions.HTTPError as err:
    if err.response.status_code == 429:
        print("Slowing down search speed.")
        time.sleep(3)
except Exception as e:
    print(f"An error occurred: {e}")

# After the loop, send a single email with all the alerts bundled
if email_list:
    full_email_content = "\n\n".join(email_list)
    nm.SendEmail("davidbengtsson321@gmail.com", "Low Price Alerts!", full_email_content)
    print("Email sent with bundled alerts.")

# Print the updated sheet_data for verification
pprint(sheet_data)
