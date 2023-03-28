import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv("./.env")
TEQUILA_API_KEY = os.environ.get("tequila_api_key")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
LOCATIONS_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, city_name):
        header = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}

        response = requests.get(url=LOCATIONS_ENDPOINT, headers=header, params=query).json()
        iata_code = response["locations"][0]["code"]
        return iata_code

    def search_flights(self, origin_city, destination_city, stop_overs):
        tomorrow = datetime.now() + timedelta(1)
        six_months = tomorrow + timedelta(180)

        header = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "flight_type": "round",
            "max_stopovers": stop_overs,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 14,
            "curr": "EUR"
        }
        response = requests.get(url=TEQUILA_ENDPOINT, headers=header, params=query).json()["data"]
        return response