import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSecAnO6YCFgnoVGNE0Diyv1msI3k5-uFulUBrvKEbcg4WWqPw/viewform?usp=sf_link'
ZILLOW = 'https://appbrewery.github.io/Zillow-Clone/'


response = requests.get(ZILLOW)

web = response.text

soup = BeautifulSoup(web, 'html.parser')

find_links = soup.find_all(name='a', class_='property-card-link')
find_prices = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
find_addresses = soup.find_all('address')

links = [link.get('href') for link in find_links]
prices = [price.getText().strip('+/mo').replace('+ 1 bd', "").replace("+ 1bd", "") for price in find_prices]
addresses = [address.getText().strip().replace('|', "") for address in find_addresses]

brave_options = webdriver.ChromeOptions()
brave_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
brave_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=brave_options)

driver.maximize_window()

driver.get(FORM)

q1 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
q2 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
q3 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')


for i in range(len(links)):
    
    time.sleep(2)
    q1 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q2 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q3 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    
    q1.send_keys(addresses[i])
    q2.send_keys(prices[i])
    q3.send_keys(links[i])
    
    submit.click()
    
    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    
    




