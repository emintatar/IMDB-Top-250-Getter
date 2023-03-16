from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.imdb.com/chart/top/"
req = requests.get(url)
soup = BeautifulSoup(req.content, "lxml")
data = soup.find("tbody", class_="lister-list").find_all("tr")

movie_list = []

for i in data:
    movie_name = i.find("td", class_="titleColumn").a.text
    movie_year = (i.find("td", class_="titleColumn").span.text).replace(
        "(", "").replace(")", "")
    movie_rating = i.find("td", class_="ratingColumn imdbRating").strong.text

    movie_list.append({
        "name": movie_name,
        "year": movie_year,
        "rating": movie_rating
    })

print("Top 250 Movies on IMDB")
print()

for movie in movie_list:
    print("Name: ", movie["name"])
    print("Year: ", movie["year"])
    print("Rating: ", movie["rating"])
    print()
