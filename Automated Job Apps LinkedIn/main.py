from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

import time


brave_options = webdriver.ChromeOptions()
brave_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
brave_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=brave_options)

driver.maximize_window()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3745052393&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# sign in
signin = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
signin.click()
email = driver.find_element(By.ID, value='username')
password = driver.find_element(By.ID, value='password')
email.click()
email.send_keys("")
email.send_keys(Keys.ENTER)
password.send_keys('')
password.send_keys(Keys.ENTER)


time.sleep(25)

all_jobs = driver.find_elements(By.CSS_SELECTOR, value='.job-card-container__link')

for job in all_jobs:
    print("Opening Job Listing")
    job.click()
    time.sleep(2)
    
    try:
        
        easyapply = driver.find_element(By.CSS_SELECTOR, value='.jobs-s-apply button')

        easyapply.click()

        time.sleep(2)
        next = driver.find_element(By.CSS_SELECTOR, value='div button')
        next.click()

        time.sleep(2)
        save = driver.find_element(By.XPATH, value='//button[@data-control-name="save_application_btn"]')
        save.click()

        time.sleep(1)
        continue_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-s-apply button')
        continue_button.click()

        time.sleep(1)
        next = driver.find_element(By.XPATH, value='//button[@type="button"]')
        next.click()

        time.sleep(1)
        next = driver.find_element(By.XPATH, value='//button[@data-easy-apply-next-button=""]')
        next.click()

        time.sleep(1)
        review = driver.find_element(By.XPATH, value='//button[@aria-label="Review your application"]')
        review.click()

        time.sleep(5)
        submit = driver.find_element(By.XPATH, value='//button[@aria-label="Submit application"]')
        submit.click()
        
        dismiss = driver.find_element(By.XPATH, value='//button[@aria-label="Dismiss"]')
        dismiss.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue
