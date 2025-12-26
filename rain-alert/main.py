import os
import smtplib
import requests

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
MY_LAT = 3.57
MY_LNG = 72.46

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=api_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True


if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="mashfiqmahi007@gmail.com", msg="Subject: Rain\n\nIt will rain today")
        print("sent")