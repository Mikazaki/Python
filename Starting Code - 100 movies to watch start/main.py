import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"




# Write your code below this line 👇
response = requests.get(URL)

web = response.text

soup = BeautifulSoup(web, 'html.parser')

tag = soup.find_all(name='h3', class_='title')

title = []

for text in tag:

    title.append(text.getText())

title.reverse()

with open("movies.txt", 'w', encoding='utf-8') as file:

    for movie in title:
        file.write(movie + '\n')






