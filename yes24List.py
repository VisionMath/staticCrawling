from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pymysql
import time


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    r_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return r_driver


driver = set_chrome_driver()
url = 'http://www.yes24.com/Product/Search?domain=BOOK&query=%EB%94%A5%EB%9F%AC%EB%8B%9D&page=1'

driver.implicitly_wait(2)
driver.get(url)
driver.implicitly_wait(2)

stopFlag = False
book_list = []

# while True:
li_list=driver.find_elements(By.CSS_SELECTOR, '#yesSchList > li')

for li in li_list:
    title = li.find_element(By.CSS_SELECTOR, 'a.gd_name').text
    author = li.find_element(By.CSS_SELECTOR, 'span.authPub.info_auth > a').text
    pub = li.find_element(By.CSS_SELECTOR, 'span.authPub.info_pub > a').text
    pub_date = li.find_element(By.CSS_SELECTOR, 'span.authPub.info_date').text
    price = li.find_element(By.CSS_SELECTOR, 'div.info_row.info_price > strong > em').text
    image = li.find_element(By.CSS_SELECTOR, '#yesSchList > li > div > div.item_img > div.img_canvas > span > span > a > em > img').get_attribute('src')
    # print(title, author, pub, pub_date, price)
    print(image)

    # image_name=image.split('/')
    # print(image_name)

driver.quit()
