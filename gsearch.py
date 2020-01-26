#import du librairies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#defining the browser to be used with its driver : chromedriver
browser = webdriver.Chrome(executable_path=r'C:\Users\kmezui\Downloads\chromedriver_win32\chromedriver.exe')

#Opening new instance of Google Chrome
browser.get('https://www.google.com')

#defining the waiting time forthe page to be opened before to continue
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')))

#dealing with the search textbox, using tab instead of enter
browser.find_element_by_css_selector('#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input').send_keys('How to Python Foxtrot' + Keys.TAB)

#dealing with the search button
browser.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input['
                                     'type="submit"]:nth-child(1)').click()

wait.until(EC.presence_of_element_located((By.ID, 'resultStats')))

#We make sure that the text we'll be searching is present in the results
result_stats = browser.find_element_by_id('resultStats').text
print(result_stats)

browser.quit()
