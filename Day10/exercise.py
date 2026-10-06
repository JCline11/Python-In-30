# Exercise for day 10 of Python in 30: Loops
# level 1
for i in range(11):
	print(i, end=" ")
print()
k = 0
while k is not 11:
	print(k, end=" ")
	k+=1
print()

for i in range(10,-1,-1):
	print(i, end=" ")
print()
k = 10
while k is not -1:
	print(k,end=" ")
	k-=1
print()

star = 1
for i in range(7):
	print("*" * star)
	star += 1

for i in range(8):
	for k in range(8):
		print("#", end=" ")
	print()

for i in range(11):
	print(str(i) + " x " + str(i) + " = " + str(i*i))

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
	print(i)

for i in range(101):
	if (i % 2) is 0:
		print(i)

for i in range(101):
	if (i % 2) is 1:
		print(i)

# level 2
sum = 0
for i in range(101):
	sum += i
print("The sum of all numbers is {}.".format(sum))

even = 0
odd = 0
for i in range(101):
	if (i % 2) is 0:
		even += i
	else:
		odd += i
print("The sum of all even numbers is {}. The sum of all odd numbers is {}.".format(even, odd))

# level 3
from data.countries import countries
from data.countries_data import countries_data

for i in countries:
	if "land" in i:
		print(i)

fruit = ['banana', 'orange', 'mango', 'lemon']
num = len(fruit) -1
index = 0
while num > index:
	temp = fruit[num]
	fruit[num] = fruit[index]
	fruit[index] = temp
	num -= 1
	index += 1
print(fruit) 

lang = {}
for country in countries_data:
	for i in country["languages"]:
		lang[i] = lang.get(i, 0) + 1
print("There are {} languages in the dataset.".format(len(lang)))

top10 = sorted(lang.items(), key=lambda item: item[1], reverse=True)[:10]
for name, count in top10:
	print(name, " ", count)

pop = {}
for c in countries_data:
	pop[c["name"]] = c["population"]
top10 = sorted(pop.items(), key=lambda item: item[1], reverse=True)[:10]
for name, count in top10:
	print(name, " ", count)