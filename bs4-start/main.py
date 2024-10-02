from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="td", class_="title")
print(article_tag.getText)






# with open("website.html", encoding="UTF-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# anchor_tags = soup.find_all(name="a")
#
#
# # for tag in anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
#
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)