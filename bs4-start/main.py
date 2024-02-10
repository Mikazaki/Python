from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")

web_pg = response.text

soup = BeautifulSoup(web_pg, 'html.parser')

tag = soup.find_all(name="a", rel="noreferrer")

score = [int(scores.getText().split()[0]) for scores in soup.find_all(name='span', class_='score')]

text = []

link = []

for data in tag:
    text.append(data.getText())
    link.append(data.get("href"))

largest = max(score)

i = score.index(largest)

print(text[i])
print(link[i])
print(score[i])





# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
#
# all_tags = soup.find_all(name='a')
# for tags in all_tags:
#     print(tags.get("href"))