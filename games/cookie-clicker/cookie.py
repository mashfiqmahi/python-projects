# pip install selenium==3.141.0
# pip install --upgrade urllib3==1.26.16

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

my_cookie = driver.find_element(By.ID, value="money")

prices = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in prices]
print(item_ids)
timeout = time.time() + 5
five_min = time.time() + 5*60

while True:
    cookie.click()
    #Every 5 second
    if time.time() > timeout:
        #Upgrage all <b> prices
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        #Convert into integer
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = item_ids[n]

        # Get current cookie count
        my_cookie = driver.find_element(By.ID, value="money").text
        if "," in my_cookie:
            my_cookie = my_cookie.replace(",", "")
        cookie_count = int(my_cookie)

        # Find upgrades that we can currently afford
        affordable_upgrade = {}
        for cost,id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrade[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrade)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrade[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()
        timeout = time.time() + 5
    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
#driver.quit()