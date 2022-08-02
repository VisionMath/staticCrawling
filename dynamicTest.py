from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome('chromedriver.exe')
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    r_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return r_driver

driver=set_chrome_driver()
print(f'WebDriver 객체: {type(driver)}')

driver.get('http://www.google.com/ncr')
target=driver.find_element(By.CSS_SELECTOR, "[name='q']")
print(f"찾아온 태그 객체: {type(target)}")
target.send_keys("파이썬")
target.send_keys(Keys.ENTER)
