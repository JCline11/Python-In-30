# excercise 2 for day 5

from data.countries import countries


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("min age: ", ages[0])
print("max age: ", ages[-1])
print("median age: ", ages[(len(ages) - 1) // 2])
print("average age: ", sum(ages) / len(ages))
print("range of ages: ", ages[-1] - ages[0])
print("compare min - avg and max - avg", abs(ages[0] - sum(ages) / len(ages)), abs(ages[-1] - sum(ages) / len(ages)))

middle = countries.index(countries[(len(countries) - 1) // 2])
print("middle: ", countries[middle])
first_half = countries[:middle]
second_half = countries[middle+1:]
cntry = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_item, second_item, third_item, *rest = cntry
print("first item: ", first_item)
print("second item: ", second_item)
print("third item: ", third_item)
print("scandic: ", rest)
