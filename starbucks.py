from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    r_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return r_driver

driver=set_chrome_driver()

driver.implicitly_wait(3)
driver.get('https://www.starbucks.co.kr/store/store_map.do')
target=driver.find_elements(By.CLASS_NAME, 'quickResultLstCon')
for t in target:
    print(t.text)
driver.quit()



