import requests
import os
from dotenv import load_dotenv
load_dotenv()
SHEET_API_KEY = os.environ.get("sheet_api_key")
SHEET_ENDPOINT = os.environ.get("sheet_endpoint")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_sheet_data(self):
        header = {
            "Authorization": SHEET_API_KEY
        }
        get_sheet_data = requests.get(url=SHEET_ENDPOINT, headers=header).json()["prices"]
        return get_sheet_data
    
    def add_iata_code_to_sheet(self, iata_code, row_id):
        header = {
            "Authorization": SHEET_API_KEY
        }
        prices = {
            "price": 
            {
                "iataCode": iata_code
            }
        }
        requests.put(url=f"{SHEET_ENDPOINT}/{row_id}", headers=header, json=prices)