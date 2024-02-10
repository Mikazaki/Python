from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

brave_options = webdriver.ChromeOptions()
brave_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
brave_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=brave_options)

driver.get("https://www.python.org/")

menu = {}

for i in range(1, 6):
    
    title = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]')
    date = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/time')
    text = title.text.strip()
    time = date.get_attribute("datetime")
    parsed_datetime = datetime.fromisoformat(time)
    formatted_date = parsed_datetime.strftime("%Y-%m-%d")


    cleaned_text = text.split('\n', 1)[-1]

    menu[int(f"{i}")] = {'Time': formatted_date, 'Name': cleaned_text}



print(menu)