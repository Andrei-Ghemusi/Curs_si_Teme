import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.get("http://www.seleniumframework.com/Practiceform/")
chrome.find_element(By.NAME,"name").send_keys("Cezar")
time.sleep(1)
lista_emails = chrome.find_elements(By.NAME,"email")
lista_emails[1].send_keys("cezarsopterean@gmail.com")
time.sleep(1)
chrome.find_element(By.NAME,"telephone").send_keys("0756891258")
time.sleep(1)
chrome.find_element(By.NAME,"country").send_keys("Romania")
time.sleep(1)
chrome.find_element(By.NAME,"company").send_keys("itfactory")
time.sleep(1)
chrome.find_element(By.NAME,"message").send_keys("mesaj text pentru submit formular")
time.sleep(1)
chrome.find_element(By.LINK_TEXT,"Submit").click()
time.sleep(1)
chrome.quit()


