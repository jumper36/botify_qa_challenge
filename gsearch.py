#import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#specify the webdriver to be used
browser = webdriver.Chrome(executable_path=r'C:\Users\kmezui\Downloads\chromedriver_win32\chromedriver.exe')

#create an instance of google chrome
browser.get('https://www.google.com/')

wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')))

#entering a query for the research and press Enter key
browser.find_element_by_css_selector('#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input').send_keys('How To Python Foxtrot' + Keys.TAB)
#browser.find_element_by_css_selector('#tsf > div:nth-child(2) > div > div.FPdoLc.VlcLAe > center > input[type="submit"]:nth-child(1)').click()

#find the element using the ID
wait.until(EC.presence_of_element_located((By.ID, 'resultStats')))

result_stats = browser.find_element_by_id('resultStats').text
print(result_stats)

#closing the browser
browser.quit()

