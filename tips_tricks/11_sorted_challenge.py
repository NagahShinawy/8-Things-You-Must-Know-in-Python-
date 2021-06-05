class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return f"Country({self.name}, {self.population})"

    def __eq__(self, other):
        return (
                f"Country({self.name}, {self.population})"
                == f"Country({other.name}, {other.population})"
        )


country_list = [
    Country("Taiwan", "24000000iso"),
    Country("Portugal", "10000000iso"),
    Country("netherlands", "17500000iso"),
    Country("nigeria", "198000000iso"),
    Country("jordan", "10000000iso"),
    Country("nepal", "30000000iso"),
    Country("niger", "24000000iso"),
    Country("japan", "128000000iso"),
]


def get_pop_and_name(country: Country) -> tuple:
    pop = country.population
    name = country.name
    return int(pop[:-3]), name.lower()  # make sure to put char in the same case to avoid bug of sort upper and lower
    # because upper comes first at ASCII , a not A


def get_sorted():
    """Return the country list so that it is sorted first by population 
    and then alphabetically by country name."""
    return sorted(country_list, key=get_pop_and_name)


def get_sorted_2():
    """Return the country list so that it is sorted first by population
    and then alphabetically by country name."""
    return sorted(country_list, key=lambda country: (int(country.population[:-3]), country.name.lower()))


def get_sorted3():
    cnt = sorted(country_list, key=lambda country: country.name.lower())
    return sorted(cnt, key=lambda country: int(country.population[:-3]))


res = get_sorted()
print(res)
to_title = [country.name.title() for country in res]

print(to_title)

print("#" * 100)

print(get_sorted_2())

print(get_sorted_2() == get_sorted())  # True

print("#" * 100)

print(get_sorted3() == get_sorted() == get_sorted_2())  # True
# ############ ############ ############ ############ ############ ############ ############ ###########
