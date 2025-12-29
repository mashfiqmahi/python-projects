import smtplib
import requests
my_email = "kazimashfiqju@gmail.com"
password = "tbqghcmflonetydx"

s = """This dynamic equation takes into account pr…", 'url': 'https://biztoc.com/x/ae7d4f652d3ee2c4', 'urlToImage': 'https://biztoc.com/cdn/ae7d4f652d3ee2c4_s.webp', 'publishedAt': '2024-06-12T14:40:03Z', 'content': "Good Morning Traders!"""
m = s.encode()
import os
import locale
os.environ["PYTHONIOENCODING"] = "utf-8"
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8")
m = s.encode('utf-8', errors='ignore')
print("m : ", m)
print("s: ", s)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="mashfiqmahi007@gmail.com", msg="Subject:ASD\n\n" + str(m))
    print("sent")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "471666f0cfd44578852e02f9d468e2a0"
news_params ={
        "qInTitle": "TSLA",
        "apiKey": NEWS_API
    }
# news_response = requests.get(NEWS_ENDPOINT, params=news_params)
# articles = news_response.json()["articles"]
# print(articles)