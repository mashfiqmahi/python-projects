import smtplib
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "P1T0BFYFF8M7CWVF"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "471666f0cfd44578852e02f9d468e2a0"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

my_email = "kazimashfiqju@gmail.com"
password = "tbqghcmflonetydx"

# -------------------- STOCK DATA -------------------- #
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]

data_list = list(stock_data.values())
yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

difference = yesterday_close - day_before_close
diff_percent = round((difference / day_before_close) * 100, 2)

up_down = "🔺" if difference > 0 else "🔻"

# -------------------- NEWS -------------------- #
if abs(diff_percent) >= 1:   # you can change threshold
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 3,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    formatted_articles = []

    for article in articles:
        headline = article["title"]
        brief = article["description"]

        message = (
            f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
            f"Headline: {headline}\n"
            f"Brief: {brief}"
        )

        formatted_articles.append(message)

    # -------------------- EMAIL -------------------- #
    for msg in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs="mashfiqmahi007@gmail.com", msg=f"Subject: {STOCK_NAME} Stock Alert\n\n{msg}")
            print("Sent:\n", msg)
