import smtplib
import requests
import pandas
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

details = pandas.read_csv("details.csv")
person_list = details.name.to_list()
print(details)
for n in range(len((details).name.to_list())):
    person = details[details.name == person_list[n]]
    MY_LNG = person.lon
    MY_LAT = person.lat
    to_address = person.email
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LNG,
        "appid": api_key,
        "cnt": 4
    }
    message = ""
    response = requests.get(url=api_endpoint, params=parameters)
    response.raise_for_status()
    data = response.json()
    will_rain = False
    for hour_data in data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if "rain" in hour_data["weather"][0]["description"]:
            message = f"Subject: Rain\n\nHey {person.name.to_string(index=False)}, It will {hour_data["weather"][0]["description"]} today. Bring an umbrella"
        if condition_code < 600:
            will_rain = True
    print(message)

    if will_rain:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=message)
