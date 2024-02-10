import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PASSWORD = "uqwjawnamvtmqnuy"

URL = "https://www.amazon.com/SOHOMACH-Electric-Standing-Desk-Adjustable/dp/B0CF7J5HGB/ref=sr_1_7?keywords=standing%2Bdesk&sr=8-7&th=1"

response = requests.get(URL,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                            "Accept-Language": "en-US,en;q=0.6"})

web = response.text

soup = BeautifulSoup(web, 'lxml')

whole = soup.find(name='span', class_="a-price-whole")
fraction = soup.find(name='span', class_="a-price-fraction")

price = whole.getText() + fraction.getText()

title = soup.find(id="productTitle").get_text().strip()

if float(price) < 140:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="pythontemp69@gmail.com", password=PASSWORD)
        connection.sendmail(
            from_addr="pythontemp69@gmail.com",
            to_addrs="messikazi2121@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
