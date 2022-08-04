import time
import pandas as pd
import pymysql
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def getTagText(tag, by, element_path):
    try:
        elemnet = tag.find_element(by, element_path)
        return elemnet.text
    except NoSuchElementException:
        return ''


driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'http://www.yes24.com/Product/Search?domain=BOOK&query=python'

driver.implicitly_wait(2)
driver.get(url)
driver.implicitly_wait(2)

stopFlag = False
book_list = []
json_list = []

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
            score = getTagText(li, By.CSS_SELECTOR, 'div.info_row.info_rating > span.rating_grade > em')

            image = li.find_element(By.CSS_SELECTOR, '#yesSchList > li > div > div.item_img > div.img_canvas > span > span > a > em > img').get_attribute('src')
            image_name = image.split('/')[-2]
            # urllib.request.urlretrieve(image, 'book_images/' + image_name + '.jpg')
            json_list.append({'title': title, 'author': author, 'publisher': pub, 'pub_date': pub_date, 'price': price, 'score': score, 'image_src': image, 'image_name': image_name})
            book_list.append((title, author, pub, pub_date, price, score, image, image_name))

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
            page = driver.find_element(By.CSS_SELECTOR, '#goodsListWrap > div.sGoodsPagen > div > a:nth-child(' + str(num) + ')')
            page.click()
            time.sleep(2)

    if stopFlag:
        break
df = pd.DataFrame(book_list, columns=['title', 'author', 'publisher', 'pub_date', 'price', 'score', 'image_src', 'image_name'])
df.to_csv('data/yes24List.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df.fillna("", inplace=True)
book_list = df.values.tolist()
print(book_list)


def insert_books(books):
    conn = pymysql.connect(host='localhost', user='root', password='vm28283', db='pydb', charset='utf8')
    cursor = conn.cursor()
    sql = 'insert into yes24List(title, author, publisher, pub_date, price, score, image_src, image_name) values(%s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.executemany(sql, books)
    conn.commit()
    conn.close()


def select_all():
    conn = pymysql.connect(host='localhost', user='root', password='vm28283', db='pydb', charset='utf8')
    cursor = conn.cursor()
    sql = 'select * from yes24List'
    cursor.execute(sql)
    for book in cursor:
        print(book)
    conn.commit()
    conn.close()


insert_books(book_list)
select_all()

driver.quit()
