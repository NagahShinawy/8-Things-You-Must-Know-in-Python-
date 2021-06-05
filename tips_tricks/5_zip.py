"""
created by Nagaj at 05/06/2021
"""
from itertools import zip_longest


def capital_by_country(countries: list, capitals: list):
    if len(countries) != len(capitals):
        raise ValueError("countries list must be the same length of capitals list")

    for country, capital in zip(countries, capitals):
        print(f"The Capital Of '{country}' is '{capital}'")


def working_with_missing_values(countries, capitals):
    for country, capital in zip_longest(countries, capitals, fillvalue="NA"):
        print(f"The Capital of <{country}> is <{capital}>")


def main():
    countries = ["Netherlands", "Nigeria", "Jordan", "Nepal", "Niger", "Japan", "Egypt"]
    capitals = ["Amsterdam", "Abuja", "Amman", "Kathmandu", "Niamey", "Tokyo", "Cairo"]
    capitals_ = ["Amsterdam", "Abuja", "Amman"]
    capital_by_country(countries, capitals)
    print("#" * 50)
    working_with_missing_values(countries, capitals_)
    pairs = zip(countries, capitals)
    print(pairs)  # <zip object at 0x00000177D0BA1108>
    print(
        list(pairs)
    )  # [('Netherlands', 'Amsterdam'), ('Nigeria', 'Abuja'), ('Jordan', 'Amman'),
    # ('Nepal', 'Kathmandu'), ('Niger', 'Niamey'), ('Japan', 'Tokyo'), ('Egypt', 'Cairo')]

    pairs = list(zip(countries, capitals))
    ctr, cap = zip(
        *pairs
    )  # separate item of each tuple to independent sequences
    # * operator use to unpacking iterable to arguments to function call
    # فى كل مرة بيكون 2 بس (country, capital)
    # so , at the end country is tuple of first items of each nested tuple
    # AND  at the end capital is tuple of second items of each nested tuple
    print(ctr)  # ('Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan', 'Egypt')
    print(cap)  # ('Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo', 'Cairo')
    print("#" * 100)
    # todo : VERY IMPORTANT
    # you have 7 items in list 'pairs', so
    ctr, cap, x, r, t, y, u = zip(
        pairs
    )  # without using '*', means unpacking list pairs as single unit
    # not every tuple , but the example with (*pairs) means unpacking every TUPLE in the list
    # not list itself as single unit.
    print(u)  # (('Egypt', 'Cairo'),)
    print(ctr)  # (('Netherlands', 'Amsterdam'),)


if __name__ == "__main__":
    main()
