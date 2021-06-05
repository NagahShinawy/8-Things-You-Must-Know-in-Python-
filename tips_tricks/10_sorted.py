class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return f"Country({self.name}, {self.population})"


country_list = [
    Country("Taiwan", 24_000_000),
    Country("Portugal", 10_000_000),
    Country("Netherlands", 17_500_000),
    Country("Nigeria", 198_000_000),
    Country("Jordan", 10_000_000),
    Country("Nepal", 30_000_000),
    Country("Niger", 24_000_000),
    Country("Japan", 128_000_000),
]

iso = [
    ("Taiwan", "iso24000000"),
    ("Portugal", "iso10000000"),
    ("Netherlands", "iso17500000"),
    ("Nigeria", "iso198000000"),
    ("Jordan", "iso10000000"),
    ("Nepal", "iso30000000"),
    ("Niger", "iso24000000"),
    ("Japan", "iso128000000"),
]

# sort based on pop


print(sorted(country_list, key=lambda country: country.population))

# sort by name as well in case of 2 or more countries are the same value in pop, then sort ASC by name
# like Country(Portugal, 10000000), Country(Jordan, 10000000) are the same pop so, sort by name as well to put
# Jordan before Portugal
print(sorted(country_list, key=lambda country: (country.population, country.name)))

# sort DESC
print(sorted(country_list, key=lambda country: country.population, reverse=True))

# adding '-' before country.population to be "-country.population" means reverse=True means sort DESk
print(sorted(country_list, key=lambda country: -country.population))

# True: -country.population is the same of reverse=True
print(sorted(country_list, key=lambda country: -country.population) == (
    sorted(country_list, key=lambda country: country.population, reverse=True)))

# sort DESC for pop and sort ASC for name
print(sorted(country_list, key=lambda country: (-country.population, country.name)))

# sort DESC for pop and sort DESC for name
print(sorted(country_list, key=lambda country: (country.population, country.name), reverse=True))

print("#" * 100)


def get_pop_and_name(pair):
    #  pair like ("Taiwan", "iso24000000")
    return int(pair[-1][3:]), pair[0]


def get_pop(pair):
    #  pair like ("Taiwan", "iso24000000")
    return int(pair[-1][3:])


# sort by just pop (example4)
print(sorted(iso, key=get_pop))

# sort by both pop and name (example5)
print(sorted(iso, key=get_pop_and_name))

print("#" * 100)

print(sorted(iso, key=lambda country: int(country[-1][3:])))  # the same of example4 (sort by pop)
print(sorted(iso, key=lambda country: (int(country[-1][3:]))))  # the same of example5 (sort by pop & name)
