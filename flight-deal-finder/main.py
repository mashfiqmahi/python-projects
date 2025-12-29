import time
from datetime import datetime, timedelta
from data_manager import DataManager, SHEETY_PRICES_ENDPOINT
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
import requests
# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for direct flights  ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination}['city]")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)
    # ==================== Search for indirect flight if N/A ====================
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: ${cheapest_flight.price}")

    # ==================== Send Notifications and Emails  ====================

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        if cheapest_flight.stops == 0:
            route_text = (
                f"🟢 Direct flight from {ORIGIN_CITY_IATA} "
                f"to {destination['city']} ({destination['iataCode']})"
            )
        else:
            route_text = (
                f"🟡 Flight from {ORIGIN_CITY_IATA} "
                f"to {destination['city']} ({destination['iataCode']}) "
                f"with {cheapest_flight.stops} stop(s)"
            )


    # Update Google Sheet
    new_data = {
        "price": {
            "lowestPrice": cheapest_flight.price
        }
    }
    response = requests.put(
        url=f"{SHEETY_PRICES_ENDPOINT}/{destination['id']}",
        json=new_data
    )
    print('Google Sheet updated ', response.text)

    price_drop = destination["lowestPrice"] - cheapest_flight.price
    alert = "🔥 HUGE DROP!" if price_drop > 200 else "📉 Price Drop"
    email_list = data_manager.get_customer_emails()
    notification_manager.send_email(email_list=email_list, subject="️✈️Cheapest Flight Alert!!",
                                    message_body=(
                                        f"💰 Only $ {cheapest_flight.price:,.2f}\n"
                                        f"{route_text}\n\n"
                                        f"📅 Departure: {cheapest_flight.out_date}\n"
                                        f"🔁 Return: {cheapest_flight.return_date}\n"
                                        f"📉 Previous lowest price: USD {destination['lowestPrice']}"
                                    )
    )
    notification_manager.send_whatsapp(
        message_body=(
            "✈️ Low Price Alert!\n\n"
            f"💰 Only $ {cheapest_flight.price:,.2f}\n"
            f"{route_text}\n\n"
            f"📅 Departure: {cheapest_flight.out_date}\n"
            f"🔁 Return: {cheapest_flight.return_date}\n"
            f"📉 Previous lowest price: USD {destination['lowestPrice']}"
        )
    )