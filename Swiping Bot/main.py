from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException

import time


brave_options = webdriver.ChromeOptions()
brave_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
brave_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=brave_options)

driver.maximize_window()

driver.get("https://tinder.com/app/recs")

login = driver.find_element(By.XPATH, value='//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

time.sleep(2)
facebook = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
facebook.click()

time.sleep(2)
t_window = driver.window_handles[0]
fb_popup = driver.window_handles[1]

driver.switch_to.window(fb_popup)

time.sleep(2)
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
email.click()
email.send_keys("")
password = driver.find_element(By.ID, value='pass')
password.click()
password.send_keys("")
password.send_keys(Keys.ENTER)


time.sleep(5)
driver.switch_to.window(t_window)
cookies = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]').click()
allow = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]').click()

time.sleep(2)
notif = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]').click()

time.sleep(2)
like = driver.find_element(By.XPATH, value='//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')

for i in range(100):
    time.sleep(1)
    try:
        like.click()
    
    except (ElementClickInterceptedException, StaleElementReferenceException):
        try:
            pass

        except NoSuchElementException:
            time.sleep(2)
            
            
