"""
created by Nagaj at 05/06/2021
"""

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
    Country("taiwan", "24000000iso"),
    Country("portugal", "10000000iso"),
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
    return int(pop[:-3]), name


def get_sorted():
    """Return the country list so that it is sorted first by population
    and then alphabetically by country name."""
    return sorted(country_list, key=get_pop_and_name)


def test_sorted():
    expected = [
        Country("jordan", "10000000iso"),
        Country("portugal", "10000000iso"),
        Country("netherlands", "17500000iso"),
        Country("niger", "24000000iso"),
        Country("taiwan", "24000000iso"),
        Country("nepal", "30000000iso"),
        Country("japan", "128000000iso"),
        Country("nigeria", "198000000iso"),
    ]
    actual = get_sorted()

    assert actual == expected
