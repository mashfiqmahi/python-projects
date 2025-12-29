import os
import requests

SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")

response = requests.get(url="https://api.sheety.co/66fe5bb16b65f027f68f34a034c133da/flightDeals/users")
data = response.json()


customer_data = data["users"]

customer_emails = [
    row["whatIsYourEmailAddress?"]
    for row in customer_data
    if "whatIsYourEmailAddress?" in row
]

print(customer_emails)

