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

driver.implicitly_wait(3)
driver.get('https://movie.naver.com/movie/bi/mi/point.naver?code=213481')
driver.implicitly_wait(3)
target=driver.find_element(By.CLASS_NAME, 'input_text')
target.send_keys('파이썬')
target.send_keys(Keys.ENTER)
# print(target.text)
time.sleep(3)
driver.quit()