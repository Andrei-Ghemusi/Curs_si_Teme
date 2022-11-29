# Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
# - https://www.phptravels.net/
# - http://automationpractice.com/index.php
# - https://formy-project.herokuapp.com/
# - https://the-internet.herokuapp.com/
# - https://www.techlistic.com/p/selenium-practice-form.html
# - jules.app
# Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# ● Id
# ● Link text
# ● Parțial link text
# ● Name
# ● Tag*
# ● Class name*
# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
# observație:
# - Probabil nu vei găsi un singur website care să cuprindă toate variantele
# de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
#
# - Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
# Interactionează cu un element la alegere din listă.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/')
time.sleep(2)
chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
time.sleep(2)
chrome.find_element(By.ID, 'autocomplete').send_keys('Albania')
time.sleep(2)
chrome.back()
chrome.find_element(By.PARTIAL_LINK_TEXT, 'orm').click()
time.sleep(2)
lista_inputuri = chrome.find_elements(By.TAG_NAME, 'input')
lista_inputuri[2].send_keys('Caramidar')
time.sleep(2)
lista_clase = chrome.find_elements(By.CLASS_NAME, 'form-control')
lista_clase[1].send_keys('Ionel')
time.sleep(2)
chrome.find_element(By.CLASS_NAME, 'btn-primary').click()
time.sleep(2)

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
time.sleep(2)
chrome.find_element(By.NAME, 'firstname').send_keys('Gheorghe')
time.sleep(2)
chrome.quit()