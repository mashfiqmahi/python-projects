from selenium import webdriver
from selenium.webdriver.common.by import By

dic = {
    0 : {
        "time": "2024-08-12",
        "name": "Python"
    },
}

driver = webdriver.Chrome()
driver.get("https://www.python.org")
dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for date in dates:
    print(date.text)
name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for event in name:
    print(event.text)
events = {}
for n in range(len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": name[n].text
    }

print(events)
silent = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last time")
for s in silent:
    print(s.text)

driver.quit()