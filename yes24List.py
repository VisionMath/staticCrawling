from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pymysql
import time
import urllib.request


def set_chrome_driver():
    r_driver = webdriver.Chrome(ChromeDriverManager().install())
    return r_driver


def getTagText(tag, by, element_path):
    try:
        elemnet = tag.find_element(by, element_path)
        return elemnet.text
    except NoSuchElementException:
        return ''


driver = set_chrome_driver()

url = 'http://www.yes24.com/Product/Search?domain=BOOK&query=python'

driver.implicitly_wait(2)
driver.get(url)
driver.implicitly_wait(2)

stopFlag = False
book_list = []

while True:
    for n in range(2, 12):

        li_list = driver.find_elements(By.CSS_SELECTOR, '#yesSchList > li')

        for i in range(9):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)

        for li in li_list:
            title = getTagText(li, By.CSS_SELECTOR, 'a.gd_name')
            author = getTagText(li, By.CSS_SELECTOR, 'span.authPub.info_auth > a')
            pub = getTagText(li, By.CSS_SELECTOR, 'span.authPub.info_pub > a')
            pub_date = getTagText(li, By.CSS_SELECTOR, 'span.authPub.info_date')
            price = getTagText(li, By.CSS_SELECTOR, 'div.info_row.info_price > strong > em')

            image = li.find_element(By.CSS_SELECTOR,
                                    '#yesSchList > li > div > div.item_img > div.img_canvas > span > span > a > em > img').get_attribute(
                'src')
            image_name = image.split('/')[-2]
            urllib.request.urlretrieve(image, 'book_images/' + image_name + '.jpg')

        book_count = driver.find_elements(By.CLASS_NAME, 'itemUnit')

        if len(book_count) < 24:
            stopFlag = True
            break
        else:
            try:
                first = driver.find_element(By.CSS_SELECTOR, '#goodsListWrap > div.sGoodsPagen > div > a.bgYUI.first')
                num = n + 2
            except NoSuchElementException:
                num = n
            page = driver.find_element(By.CSS_SELECTOR,
                                       '#goodsListWrap > div.sGoodsPagen > div > a:nth-child(' + str(num) + ')')
            page.click()
            time.sleep(2)

    if stopFlag:
        break

driver.quit()
