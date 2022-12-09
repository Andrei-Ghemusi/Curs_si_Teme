'''Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri

- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
'''

'''
!!\\\\\\\!!!

Unele din site-uri cateodata nu merge, sunt la "pamant".
E posibil ca cele de la heroku si phptravels sa nu mearga site-ul in sine :(

!!!!\\\\!!!!
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# time.sleep(2)
# chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
# time.sleep(2)
# chrome.find_element(By.ID, 'autocomplete').send_keys('Albania')
# time.sleep(2)
# chrome.find_element(By.CLASS_NAME, 'dismissButton').click()
# chrome.back()
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'orm').click()
# time.sleep(2)
# chrome.find_elements(By.TAG_NAME, 'input')[2].send_keys('Caramidar')
# time.sleep(2)
# lista_clase = chrome.find_elements(By.CLASS_NAME, 'form-control')
# lista_clase[1].send_keys('Ionel')
# time.sleep(2)
# chrome.find_element(By.CLASS_NAME, 'btn-primary').click()
# time.sleep(2)


# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# time.sleep(2)
# chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()
# time.sleep(2)
# chrome.find_element(By.ID, 'username').send_keys('Johnny Bravo')
# time.sleep(2)
# lista = chrome.find_elements(By.TAG_NAME, 'input')
# lista[1].send_keys('abcd')
# time.sleep(2)
# chrome.find_element(By.CLASS_NAME, 'radius').click()
# time.sleep(2)
# chrome.quit()


# CSS
# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/login')
# time.sleep(1)
# chrome.find_element(By.CSS_SELECTOR, "#username").send_keys('Brotha')
# time.sleep(1)
# chrome.find_element(By.CSS_SELECTOR, 'input[id="password"').send_keys('gigi21')
# time.sleep(1)
# chrome.find_element(By.CSS_SELECTOR, '.radius').click()
# time.sleep(1)
# text_pt_username = chrome.find_element(By.CSS_SELECTOR, 'div > label[for="username"]').text
# assert text_pt_username == 'Username', f'Error, expected - Username -, got {text_pt_username} instead'
# time.sleep(1)
# chrome.quit()

# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://jules.app/sign-in')
# time.sleep(1)
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your email"]').send_keys('auras@yoda.com')
# time.sleep(1)
# chrome.find_elements(By.CSS_SELECTOR, '.MuiInputBase-input')[1].send_keys('Aleluia')
# time.sleep(1)
# text_for_down = chrome.find_element(By.CSS_SELECTOR, 'div.css-92xsvj > span').text
# assert text_for_down == "Don't have an account?", f"Error, expected - Don't have an account? -, got {text_for_down}"
# time.sleep(1)
# chrome.quit()



# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/login')
# verificare = chrome.find_element(By.CSS_SELECTOR, 'div.row > div:first-of-type label').text
# assert verificare == 'Username', f'Error, expected - Username - , got {verificare} instead'
# chrome.find_element(By.CSS_SELECTOR, 'div.example>form>div:first-of-type input').send_keys('tomsmith')
# time.sleep(2)
# chrome.find_element(By.CSS_SELECTOR, 'div.example > form > div:nth-of-type(2) input').send_keys('SuperSecretPassword!')
# time.sleep(2)
# chrome.find_element(By.CSS_SELECTOR, '#login> div + button').click()
# time.sleep(2)
# chrome.quit()



'''
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
'''

# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://jules.app/sign-in')
# chrome.find_element(By.XPATH, '//div[@class="css-1rs1o1r"][1]//input').send_keys('vasilescu@gmail.com')
# time.sleep(2)
# chrome.find_element(By.XPATH, '//input[@placeholder="Enter your password"]').send_keys('cumetreee')
# time.sleep(2)
# chrome.find_element(By.XPATH, '//*[@class="MuiButton-label"]').click()
# time.sleep(2)
# chrome.quit()



# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# time.sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="ez-manage-settings"]').click()
# time.sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="ez-show-vendors"]').click()
# time.sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="ezVendors"]/div[6]/div[1]/div[2]//input').click()
# time.sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="ez-save-settings"]').click()
# time.sleep(1)
# chrome.find_element(By.NAME, 'firstname').send_keys('Gheorghe')
# time.sleep(1)
# chrome.find_element(By.NAME, 'firstname').clear()
# chrome.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input').send_keys('Ionel')
# time.sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input/parent::div/following-sibling::div[4]/preceding-sibling::div[1]/input').send_keys('Vasilescu')
# time.sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="datepicker"] | //*[@id="continents"]').send_keys("20-09-1990")
# time.sleep(1)
# chrome.quit()


# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# time.sleep(2)
# chrome.find_element(By.XPATH, '//a[@href ="/login"]').click()
# full_text = chrome.find_element(By.XPATH,'//a[text()="Elemental Selenium"]').text
# print(full_text)
# time.sleep(2)
# chrome.back()
# chrome.find_element(By.XPATH, '//a[text()="A/B Testing"]').click()
# time.sleep(1)
# chrome.back()
# chrome.find_element(By.XPATH, '//a[text()="Broken Images"]').click()
# time.sleep(1)
# chrome.back()
# chrome.find_element(By.XPATH, '//a[contains(text(),"Geo")]').click()
# time.sleep(2)
# chrome.quit()



# chrome = webdriver.Chrome()
# chrome.maximize_window()
# chrome.get('https://phptravels.net/')
# time.sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="ACCOUNT"]').click()
# time.sleep(1)
# chrome.find_element(By.XPATH, '//a[text()="Customer Signup"]').click()
# time.sleep(1)
# def choice(placeholder_text, input_value):
#     input = chrome.find_element(By.XPATH, f'//input[@placeholder = "{placeholder_text}"]')
#     input.clear()
#     input.send_keys(input_value)
# choice('First Name', 'Andrei')
# choice('Last Name', 'Ghemusi')
# choice('Email', 'andreighemusi@gamil.com')
# choice('Phone', '070000000')
# choice('Password', 'alabalaportocala')
# time.sleep(1)
# chrome.find_element(By.XPATH, '//*[@id="select2-account_type-container"]').click()
# time.sleep(2)
# chrome.quit()












