"""
created by Nagaj at 05/06/2021
"""
import random

numbers = [random.randint(50, 100) for _ in range(10)]
salaries = [4, 8, 9, 10, 25, 11, 17, 3, 15]
print(numbers)

print(max(numbers))
print(min(numbers))
print("#" * 100)
print(max(salaries))
print(min(salaries))

print("#" * 100)
countries = ["Netherlands", "Nigeria", "Jordan", "Nepal", "Niger", "Japan"]
print(max(countries))  # max of alphabetic
print(min(countries))  # min of alphabetic
print("#" * 100)
# using _ with long number for easy visualization of number
population = [17_500_000, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]

countries = dict(zip(countries, population))  # dict == > {country: pop}
print(countries)

max_pop = max(population)
print(max_pop)

for country in countries:
    pop = countries[country]
    if pop == max_pop:
        print({country: pop})

print(sorted(countries.items(), key=lambda item: item[-1]))


def find_max_pop_country(countries: dict):
    # return {country: pop for country, pop in sorted(countries.items(), key=lambda item: item[1])}
    sorted_countries_based_on_pop = sorted(countries.items(), key=lambda item: item[1])
    return sorted_countries_based_on_pop[-1]  # last one means max


print(find_max_pop_country(countries))

print("#" * 100)
countries = list(zip(countries, population))  # [ (country, pop), (country, pop), ....  ] ==> list of tuples

print(countries)
cnrt, pop = zip(*countries)
print(cnrt)  # tuples of countries
print(pop)  # tuples of pop

na = {
    "Egypt": 1000,
    "Tunis": 2000,
    "Morocco": 500,
    "Dubai": 200,
    "Senegal": 100
}

# todo : you are using dict.items
print(min(na.items(), key=lambda item: item[1]))  # ('Senegal', 200)
print(max(na.items(), key=lambda item: item[1]))  # ('Tunis', 2000)

print("#" * 100)  # max of values
print(min(na.values()))  # 2000
print(max(na.values()))  # 100

print("#" * 100)

# based on alphabetic
print(min(na.keys()))  # Dubai startswith 'D' the min of alphabetic
print(max(na.keys()))  # Tunis startswith 'T' the max of alphabetic


def get_pop(pair):
    country, pop = pair
    return pop


print(min(countries, key=get_pop))  # the same of ===>  key=lambda pair: pair[1] because pop has index 1 of pair tuple
print(min(countries,
          key=lambda pair: pair[1]))  # the same of ===>  key=lambda pair: pair[1] because pop has index 1 of pair tuple

print("#" * 100)
# todo : IMPORTANT: because you are typed population at first comparison was by the value of pop
countries = ["Netherlands", "Nigeria", "Jordan", "Nepal", "Niger", "Japan"]
population = [17_500_000, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]
print(min(zip(population, countries)))  # (10000000, 'Jordan')
