#MEMORY SAVERS
#FUNCTIA LAMBDA
import copy
import csv
from bs4 import BeautifulSoup
import requests

my_lambda = lambda x, y : x + y
my_sum = my_lambda(2,3)
print(my_sum)


players =[
    {
    "first_name": "John",
    "last_name": "Doe",
    "rank": 3
    },
    {
    "first_name": "Kevin",
    "last_name": "McDonald",
    "rank": 1
    },
    {
    "first_name": "Brad",
    "last_name": "Kelvin",
    "rank": 2
    }
]

print(sorted(players, key=lambda player: player["rank"]))

# FUNCTIA MAP

def check_to_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
    return updated_player
players_with_top_3_value = map(check_to_3_player, players)

print(list(players_with_top_3_value))

# FUNCTIA FILTER

all_mcdonalds = filter(lambda player: player["last_name"] == "McDonald", players)
print("All McDonals: ", list(all_mcdonalds))

#FUNCTIA ZIP

list_1 = [1, 2, 3]
list_2 = [10, 20, 30]
list_3 = [100, 200, 300]

z = zip(list_1, list_2, list_3)
print(list(z))

names = ["ion", "vasile", "elena"]
ages = [20, 18, 35]
jobs = ["engineer", "consultant", "teacher"]
for name, age, job in zip(names,ages, jobs):
    print(f"{name} is {job} and has {age} years")

#LIST COMPREHENSION

my_numbers = list(range(1, 11))
print(my_numbers)

squared = [i ** 2 for i in my_numbers]
print(squared)
squared_even_nr = [i ** 2 for i in my_numbers if i % 2 == 0]
print(squared_even_nr)


#LUCRUL CU FISIERELE

new_cars = [
    ["Dacia", "Logan", 2005, 75],
    ["Renault", "Clio", 2005, 75]
]
with open("cars.csv", "a") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    for new_car in new_cars:
        csv_writer.writerow(new_car)



URL = 'https://lpf.ro/liga-1'
r = requests.get(URL)

teams = []
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table', attrs={'class': 'clasament_general white-shadow'})
for row in table.findAll('tr', attrs={'class': 'echipa_row'}):
    echipa = row.find('td', attrs={'class': 'echipa'}).text
    pozitie = row.find('td', attrs={'class': 'poz'}).text
    teams.append({
        'nume-echipa': echipa,
        'pozitie-clasament': pozitie
    })
print(teams)

