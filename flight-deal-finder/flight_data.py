class FlightData:

    def __init__(self,
        price,
        currency,
        origin_airport,
        origin_country,
        destination_airport,
        destination_country,
        out_date,
        return_date,
        airline,
                 stops):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.currency = currency
        self.origin_airport = origin_airport
        self.origin_country = origin_country
        self.destination_airport = destination_airport
        self.destination_country = destination_country
        self.out_date = out_date
        self.return_date = return_date
        self.airline = airline
        self.stops = stops

def find_cheapest_flight(data):
    """
    Parses flight data received from the Amadeus API to identify the cheapest flight option among
    multiple entries.
    Args:
        data (dict): The JSON data containing flight information returned by the API.
    Returns:
        FlightData: An instance of the FlightData class representing the cheapest flight found,
        or a FlightData instance where all fields are 'NA' if no valid flight data is available.
    This function initially checks if the data contains valid flight entries. If no valid data is found,
    it returns a FlightData object containing "N/A" for all fields. Otherwise, it starts by assuming the first
    flight in the list is the cheapest. It then iterates through all available flights in the data, updating
     the cheapest flight details whenever a lower-priced flight is encountered. The result is a populated
     FlightData object with the details of the most affordable flight.
    """
    # COUNTRIES = {
    #     "BD": "Bangladesh",
    #     "HK": "Hong Kong",
    # }
    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A","N/A", "N/A", "N/A", "N/A")

    cheapest_offer = data["data"][0]

    def extract_flight_info(flight):
        price = float(flight["price"]["grandTotal"])
        currency = flight["price"]["currency"]

        segment_out = flight["itineraries"][0]["segments"][0]
        segment_return = flight["itineraries"][1]["segments"][0]
        # A flight with 2 segments will have 1 stop
        nr_stops = len(flight["itineraries"][0]["segments"]) - 1

        origin_code = segment_out["departure"]["iataCode"]
        destination_code = segment_out["arrival"]["iataCode"]

        out_date = segment_out["departure"]["at"].split("T")[0]
        return_date = segment_return["departure"]["at"].split("T")[0]

        airline_code = flight["validatingAirlineCodes"][0]
        airline = data["dictionaries"]["carriers"].get(airline_code, airline_code)

        locations = data["dictionaries"]["locations"]

        origin_country = locations[origin_code]["countryCode"]
        destination_country = locations[destination_code]["countryCode"]

        return (
            price, currency,
            origin_code, origin_country,
            destination_code, destination_country,
            out_date, return_date,
            airline,
            nr_stops
        )

    lowest_price = float(cheapest_offer["price"]["grandTotal"])

    cheapest_flight = FlightData(*extract_flight_info(cheapest_offer))

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            cheapest_flight = FlightData(*extract_flight_info(flight))

    return cheapest_flight