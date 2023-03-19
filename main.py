from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL).text

soup = BeautifulSoup(response, "html.parser")
print(soup.prettify())

movies = []
counter = 0
top100list = []

movie_div = soup.find(name="div", class_="entity-info-items__list")
moive_list = movie_div.find_all(name="li")

for item in moive_list:
    counter += 1
    movies.append(f"{counter}) {item.getText()}")

with open("top100list.txt", "w") as file:
    for item in movies:
        file.write(f"{item}\n")