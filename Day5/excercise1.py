# excercise 1 for day 5

lst = []
lst = [1, 2, 3, 4, 5, 6]
print(len(lst))
print(lst[0])
print(lst[-1])
print(lst[(len(lst) - 1) // 2])

mixed_data_types = ["jason", 23, 6.1, False, "3123 Lane"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[-1])
print(it_companies[(len(it_companies) - 1) // 2])
it_companies[3] = "Tesla"
print(it_companies)
it_companies.append("Netflix")
it_companies.insert(3, "Samsung")
it_companies[3] = it_companies[3].upper()
print("#, ".join(it_companies))
print("IBM" in it_companies)
it_companies.sort()
it_companies.reverse()
print(it_companies[3:])
print(it_companies[:-3])
print(it_companies[:3] + it_companies[-3:])
middle = it_companies.index(it_companies[(len(it_companies) - 1) // 2])
print(it_companies[:middle] + it_companies[middle+1:])
it_companies.remove(it_companies[0])
it_companies.pop()
del it_companies[middle]
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + ["Python", "SQL"] + back_end
print(full_stack)