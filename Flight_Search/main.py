from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime

ORIGIN_CITY = "HEL"

data_manager = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

def check_flight_price(i, stop_overs):
    price = data["price"]
    city = data["cityTo"]
    date = data["local_departure"]
    if price <= lowest_prices[i]:
        date_string = str(data["local_departure"])
        date_object = datetime.fromisoformat(date_string)
        date = str(date_object).split("+")[0]
        link = data["deep_link"]
        notification.send_email(price, city, date, link, stop_overs)
    print(f"{city}: €{price}")

sheet_data = data_manager.get_sheet_data()
iata_codes = [element["iataCode"] for element in sheet_data]
lowest_prices = [element["lowestPrice"] for element in sheet_data]
i = 0
for code in iata_codes:
    try:
        data = flight_search.search_flights(ORIGIN_CITY, code, stop_overs=0)[0]
    except IndexError:
        print(f"No flights found for {code}.")
        try:
            data == flight_search.search_flights(ORIGIN_CITY, code, stop_overs=1)[0]
        except IndexError:
            print(f"Still no flights found for {code} even with 1 stop over.")
        else:
            print(f"Found flight for {code} with 1 stop over.")
            check_flight_price(i, stop_overs=1)
    else:
        check_flight_price(i, stop_overs=0)
    i += 1