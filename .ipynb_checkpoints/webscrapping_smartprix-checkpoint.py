from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/dhruv/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service = s)
driver.get("https://www.smartprix.com/mobiles")

checkbox1 = driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
checkbox1.click()
time.sleep(1)

checkbox2 = driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span')
checkbox2.click()
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:
    load_more = driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    counter += 1
    print(f"old_height = {old_height}, new_height = {new_height}, counter = {counter}")

    if old_height == new_height:
        break

    old_height = new_height

html = driver.page_source

with open('smartprix.html', 'w', encoding='utf-8') as f:
    f.write(html)

input("Press Enter to close the browser...")
driver.quit()