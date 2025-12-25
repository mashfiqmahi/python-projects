import os
import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
BUY_PRICE = 150
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
heeader = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}
amazon_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=amazon_url, headers=heeader)
response.raise_for_status()
amazon_webpage = response.text
# print(amazon_webpage)
# print("\n\n\n")
soup = BeautifulSoup(amazon_webpage, "lxml")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
product_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip().encode('ascii', 'ignore')
product_name = product_name.decode("utf-8")
message = f"Subject:Amazon Alert!!\n\n{product_name} is now ${price_as_float}"
print(message)
if price_as_float < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="Amkabir6@gmail.com", msg=message.strip("b'"))
        print("Email sent")