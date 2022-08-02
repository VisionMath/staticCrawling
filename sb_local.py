from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pymysql

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    r_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return r_driver


driver = set_chrome_driver()

driver.implicitly_wait(2)
driver.get('https://www.starbucks.co.kr/store/store_map.do')
driver.implicitly_wait(2)
loca = driver.find_element(By.CLASS_NAME, 'loca_search')
loca.click()
driver.implicitly_wait(2)
f_link = driver.find_element(By.CSS_SELECTOR, 'div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a')
f_link.click()
driver.implicitly_wait(2)
s_link = driver.find_element(By.CSS_SELECTOR, '#mCSB_2_container > ul > li:nth-child(1) > a')
s_link.click()
driver.implicitly_wait(2)
shop_list = driver.find_elements(By.CSS_SELECTOR, '#mCSB_3_container > ul > li')
driver.implicitly_wait(2)
for shop in shop_list:
    print(shop.text)
print(len(shop_list))

count = 0
temp_list = []
total = len(shop_list)

for shop in shop_list:
    count += 1
    shoplat = shop.get_attribute('data-lat')
    shoplng = shop.get_attribute('data-long')
    shopname = shop.get_attribute('data-name')
    shopinfo = shop.find_element(By.TAG_NAME, 'p').text.split('\n')

    shopaddr = shopinfo[0] if len(shopinfo) == 2 else '-'
    shopphone = shopinfo[1] if len(shopinfo) == 2 else '-'

    # print(shoplat, shoplng, shopname, shopaddr, shopphone)
    temp_list.append((shopname, shoplat, shoplng, shopaddr, shopphone))

    if count != total and count % 3 == 0:
       driver.execute_script("var su=arguments[0];\
       var dom=document.querySelectorAll('#mCSB_3_container > ul > li')[su];\
       dom.scrollIntoView();", count)

print(temp_list)
df=pd.DataFrame(temp_list, columns=['shopname', 'shoplat', 'shoplng', 'shopaddr', 'shopphone'])
# df.to_csv('data/starbucks.csv', index=False)

def insert_shop(shops):
    conn=pymysql.connect(host='localhost', user='root', password='vm28283', db='pydb', charset='utf8')
    cursor=conn.cursor()
    sql='''insert into tbl_shop(shop_name, shop_lat, shop_long, shop_addr, shop_phone) values(%s, %s, %s, %s, %s)'''
    cursor.executemany(sql, shops)
    conn.commit()
    conn.close()

def select_all():
    conn=pymysql.connect(host='localhost', user='root', password='vm28283', db='pydb', charset='utf8')
    cursor=conn.cursor()
    sql='select * from tbl_shop'
    cursor.execute(sql)
    for shop in cursor:
        print(shop)
    conn.commit()
    conn.close()

insert_shop(temp_list)
select_all()
