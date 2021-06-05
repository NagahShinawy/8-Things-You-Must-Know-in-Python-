"""
created by Nagaj at 05/06/2021
"""
from prettytable import PrettyTable

countries = ["Netherlands", "Nigeria", "Jordan", "Nepal", "Niger", "Japan"]
capitals = {
    "Egypt": "Cairo",
    "France": "Paris",
    "SAR": "Riyad",
    "Germany": "Berlin",
    "England": "London"
}
counter = 1
for country in countries:
    print(f"{counter}-{country}")
    counter += 1

###########################################

print("#" * 100)
countries_table = PrettyTable()
countries_table.field_names = ["id", "Country"]
for counter, country in enumerate(countries, start=1):
    countries_table.add_row([counter, country])

print(countries_table)

# ######################################

capitals_ = PrettyTable()

capitals_.field_names = ["id", "country", "capital"]

for _id, country in enumerate(capitals, start=1):
    capitals_.add_row([_id, country, capitals[country]])

print(capitals_)


# ################################
capitals_ = PrettyTable()
capitals_.field_names = ["id", "country", "capital"]


# [ (id, (country, capital)) ]
# every tuple contains 2 items (id, (country, capital)) so, you must add () to be like _id, (country, capital) to match
# the values to unpack
for _id, (country, capital) in enumerate(capitals.items(), start=1):
    capitals_.add_row([_id, country, capital])

print(capitals_)

print("#" * 100)

for country in enumerate(capitals.items(), start=1):
    print(country)