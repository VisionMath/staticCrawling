from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    r_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return r_driver

driver=set_chrome_driver()

driver.implicitly_wait(10)
driver.get('https://www.naver.com/')
time.sleep(2)
# target=driver.find_element(By.CSS_SELECTOR, "[name='query']")
# target=driver.find_element(By.NAME, 'query')
# target=driver.find_element(By.ID, 'query')
target=driver.find_element(By.CLASS_NAME, 'input_text')
target.send_keys('파이썬')
target.send_keys(Keys.ENTER)
# print(target.text)
time.sleep(3)
driver.quit()