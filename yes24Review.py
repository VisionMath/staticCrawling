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
url = 'http://www.yes24.com/Product/Goods/30666296'
# url='http://www.yes24.com/Product/Goods/101349345'

driver.implicitly_wait(2)
driver.get(url)
driver.implicitly_wait(2)

stopFlag = False
review = []

while True:
    for n in range(4, 14):

        review_more = driver.find_elements(By.CLASS_NAME, 'review_more')
        for r in review_more:
            r.click()
            time.sleep(1)

        review_cont = driver.find_elements(By.CSS_SELECTOR, '#infoset_reviewContentList > div.reviewInfoGrp.lnkExtend.infoMoreSubOn > div.reviewInfoBot.origin > div.review_cont')
        for r in review_cont:
            review.append(r.text)

        if len(review_more) < 5:
            stopFlag = True
            break
        else:
            linkurl = 'div.review_sort.sortBot > div.review_sortLft > div > a:nth-child(' + str(n) + ')'
            linkNum = driver.find_element(By.CSS_SELECTOR, linkurl)
            linkNum.click()
            time.sleep(2)

    if stopFlag:
        break

for i in range(len(review)):
    print(i)
    print('-'*100)
    print(review[i])

print(len(review))