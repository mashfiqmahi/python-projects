from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
# link = driver.find_element(By.LINK_TEXT, value="Orange cup coral")
# link.click()
# driver.maximize_window()
#Find the search input by name
search = driver.find_element(By.NAME, value="search")
#Keyboard inputs
search.send_keys("Python", Keys.ENTER)
