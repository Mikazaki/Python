from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


brave_options = webdriver.ChromeOptions()
brave_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
brave_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=brave_options)

driver.maximize_window()

driver.get("http://secure-retreat-92358.herokuapp.com/")

# articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

# portals = driver.find_element(By.LINK_TEXT, value='View history')

first = driver.find_element(By.NAME, value='fName')
last = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')


first.click
first.send_keys("Fahim")
first.send_keys(Keys.ENTER)
last.send_keys("Kazi")
last.send_keys(Keys.ENTER)
email.send_keys("yea@gmail.com")
email.send_keys(Keys.ENTER)