import requests
from bs4 import BeautifulSoup
import bottle
from bottle import Bottle
from bottle import route, run, template


cities = ["belfast",
          "birmingham",
          "blackpool",
          "bournemouth",
          "brighton",
          "bristol",
          "cardiff",
          "edinburgh",
          "glasgow",
          "leeds",
          "leicester",
          "liverpool",
          "london",
          "manchester",
          "newcastle upon tyne",
          "norwich",
          "nottingham",
          "sheffield",
          "southampton",
          "york"]

print("Scraping city population data...", end="")
population = []
URL = "https://worldpopulationreview.com/countries/cities/united-kingdom"
res = requests.get(URL)
soup = BeautifulSoup(res.content, "html.parser")
body = soup.body
tr = body.find_all("tr")
tr = tr[1:]
for i in tr:
    element = i.find_all("td")
    city = element[0].text
    citypop = element[1].text
    citypop = int(citypop.replace(',',''))
    if city.lower() in cities:
        population.append((city.lower(),citypop))
print(str(len(population)), "cities scraped")
population = sorted(population)

num_restaurants = []
for i in cities:
    print("Scraping Tripadvisor for vegan option restaurants in", i)
    file = i + ".html"
    soup = BeautifulSoup(open(file, encoding="utf8"), "html.parser")
    span = soup.find_all("span")
    for e in span:
        if " results match your filters" in e:
            result = int(e.span.text)
    num_restaurants.append((i,result))
num_restaurants = sorted(num_restaurants)

percapita = []
for i in range(len(num_restaurants)):
    x = num_restaurants[i][0]
    y = num_restaurants[i][1] / population[i][1]
    percapita.append((x, y))
    
percapita.sort(key=lambda a: a[1], reverse=True)
num_restaurants.sort(key=lambda a: a[1], reverse=True)

app = Bottle()

@route('/')
def index():
    heading1 = "<h1>Ranking of cities in the UK, by number of restaurants with vegan options</h1>"
    heading2 = "<h1>Ranking of cities in the UK, by number of restaurants with vegan options per capita</h1>"
    text = "<p>The data below was calculated using the number of restaurants with vegan friendly options from <br><a href=\"https://www.tripadvisor.com/Restaurants-g186216-United_Kingdom.html\" target=\"_blank\">Tripadvisor</a> and population data from  <a href=\"https://worldpopulationreview.com/countries/cities/united-kingdom\" target=\"_blank\">World Population Review</a></p>"
    table1 = "<table><tr><td><b>Rank</b></td><td><b>City</b></td><td><b>Restaurants with vegan options</b></td></tr>"
    table2 = "<table><tr><td><b>Rank</b></td><td><b>City</b></td><td><b>Restaurants with vegan options per capita</b></td></tr>"
    for i in range(len(percapita)):
        table1 = table1 + "<tr><td>" + str(i+1) + "</td><td>" + str(num_restaurants[i][0]) + "</td><td>" + str(num_restaurants[i][1]) + "</td><td></tr>"
        table2 = table2 + "<tr><td>" + str(i+1) + "</td><td>" + str(percapita[i][0]) + "</td><td>" + str(percapita[i][1]) + "</td></tr>"
    table1 += "</table>"
    table2 += "</table>"
    return "<center>" + heading1 + table1 + heading2 + table2 + "</center>"

run(host="localhost", port="8080")





