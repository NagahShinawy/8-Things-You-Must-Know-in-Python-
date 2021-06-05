"""
created by Nagaj at 05/06/2021
"""
countries = ["Netherlands", "Nigeria", "Jordan", "Nepal", "Niger", "Japan"]
print(countries)
countries.reverse()  # reverse in place and reverse the original one
# so that string and tuple don't contain reverse()
# because reverse update the original obj and string, tuple are immutables
print(countries)
print("#" * 100)
names = ["John", "James", "Leon", "Smith", "Mickael"]
rev_names = reversed(names)  # type == > list_reverseiterator  : make a copy not reverse the original one
print(rev_names)
for name in rev_names:
    print(name)

print(names)
print("#" * 100)
# reverse using slicing
salaries = [9, 6, 7, 40, 10]
print(salaries[::-1])

# because string immutable that can not updated , reversed updates the original obj , the same with tuple
# print('test'.reverse())  AttributeError: 'str' object has no attribute 'reverse'
# so, with string and tuple you can use 'reversed()' not reverse() or slicing to reverse [::-1]
red = (0, 0, 255)
color = reversed(red)
print(tuple(color))
