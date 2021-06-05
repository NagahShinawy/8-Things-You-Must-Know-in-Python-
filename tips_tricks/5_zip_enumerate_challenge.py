"""
created by Nagaj at 05/06/2021
"""
years = list(range(2010, 2020))
births = [
    723_165,
    723_913,
    729_674,
    698_512,
    695_233,
    697_852,
    696_271,
    679_106,
    657_076,
    640_370,
]


def annual_births_average(year, birth):
    index = years.index(year)
    avrg = (sum(births[:index]) + birth) / (len(births[:index]) + 1)
    return year, birth, avrg


def annual_births_average_2(years, births):
    result = []
    for index, (year, birth) in enumerate(zip(years, births), start=1):
        total = sum(births[:index])
        avg = round(total / (index))
        result.append((year, birth, avg))
    return result



for year, birth in zip(years, births):
    result = annual_births_average(year, birth)
    print(result)

# [(2010, 723165, 723165), (2011, 723913, 723539), (2012, 729674, 725584), (2013, 698512, 718816)

print(annual_births_average_2(years, births))