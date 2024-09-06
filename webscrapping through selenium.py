from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/dhruv/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service = s)
driver.get("http://google.com")


user_input = driver.find_element(by = By.XPATH ,value = '//*[@id="APjFqb"]')
user_input.send_keys('campusx')

user_input.send_keys(Keys.ENTER)

time.sleep(10)

link = driver.find_element(by = By.XPATH, value= '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
link.click()

login_button = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/header/section[2]/a[7]')
login_button.click()

input("Press Enter to close the browser...")
driver.quit() 


