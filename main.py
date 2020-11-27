from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

search_key = 'computer'

browser = webdriver.Chrome()
browser.get("http://aliexpress.com")
time.sleep(2)
search = browser.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[3]/form/div[2]/input')
search.send_keys(search_key + Keys.ENTER)

browser.find_element_by_xpath('/html/body/div[7]/div[2]/div/a').click()