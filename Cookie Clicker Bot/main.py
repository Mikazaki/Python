from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time


brave_options = webdriver.ChromeOptions()
brave_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
brave_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=brave_options)

driver.maximize_window()

driver.get("https://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, 'cookie')


timeout = time.time() + 5
five_min = time.time() + 60 * 5 



while time.time() < five_min:
    cookie.click()

    if time.time() > timeout:
        upgrades = driver.find_elements(By.CSS_SELECTOR, value='#store div')

        for upgrade in reversed(upgrades):
            try:
                if upgrade.get_attribute('class') != 'grayed':
                    upgrade.click()
                    timeout = time.time() + 5
                    break 
            except StaleElementReferenceException:
                pass

cps = driver.find_element(by=By.ID, value="cps").text
print(cps)

