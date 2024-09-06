from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/dhruv/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service = s)
driver.get("https://www.ajio.com/")

search = driver.find_element(by= By.XPATH, value = '//*[@id="appContainer"]/div[1]/div/header/div[3]/div[2]/form/div/div/input')
search.send_keys("laptop bags")
search.send_keys(Keys.ENTER)

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    counter+=1
    print(f"old_height = {old_height}, new_height = {new_height}, counter = {counter}")

    if old_height == new_height:
        break 

    old_height = new_height

html = driver.page_source

with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)

input("Press Enter to close the browser...")
driver.quit() 