import datetime as dt
import smtplib
import random
import pandas
PLACEHOLDER = "[NAME]"
data = pandas.read_csv("birthdays.csv")
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

birthday_list = data.name.to_list()
for person in range(len(birthday_list)):
    birthday_person = data[data.name == birthday_list[person]]
    birthday_day = int(birthday_person.day.to_string(index=False))
    birthday_month = int(birthday_person.month.to_string(index=False))
    birthday_tuple = (birthday_month, birthday_day)
    today = dt.datetime.now()
    today_tuple = (today.month, today.day)
    if birthday_tuple == today_tuple:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
            letter_content = letter_file.read()
            birthday_letter = "Subject:Testing Happy Birthday!\n\n" + letter_content.replace(PLACEHOLDER, birthday_person.name.to_string(index=False))
            birthday_mail = birthday_person.email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_mail, msg=birthday_letter)
