from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys

# def set_chrome_driver():
#     chrome_options = webdriver.ChromeOptions()
#     r_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     return r_driver

# driver=set_chrome_driver()
driver=webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element((By.ID, 'id')).send_keys('blood337')
driver.find_element((By.NAME, 'pw')).send_keys('')

driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

