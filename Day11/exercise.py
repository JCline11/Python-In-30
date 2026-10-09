# Code for Day 11 Python functions

def add_two_numbers(num1, num2):
	return num1 + num2
print("sum of 1 and 2 = {}".format(add_two_numbers(1,2)))

def area_of_circle(radius):
	return 3.14 * radius * radius
print("area of a circle with radius 2 = {}".format(area_of_circle(2)))

def add_all_nums(*nums):
	sum = 0
	for i in nums:
		sum += i
	return sum
print("sum of 1, 2, 3, 4  is {}".format(add_all_nums(1,2,3,4)))

def convert_celsius_to_fahrenheit(celsius):
	return (celsius*9/5) + 32
print("32 celsius converted to fahrenheit is {}".format(convert_celsius_to_fahrenheit(32)))

def check_season(month):
	season = {"Spring": ["March", "April", "May"], "Summer": ["June", "July", "August"],
	          "Fall": ["Septmeber", "October", "November"], "Winter": ["December", "January", "February"]}
	for seas in season.keys():
		if month in season[seas]:
			return seas
print("April is in {}".format(check_season("April")))

def calculate_slope(x, y, b):
	return (y - b) / x
print("calculate m for : 3 = m2 + 5. m = {}".format(calculate_slope(2,3,5)))

def print_list(lst):
	for l in lst:
		print(l, end=" ")
	print()
print_list([4, 5, 6, 7])

def reverse_list(lst):
	front = 0
	end = len(lst) - 1
	while front < end:
		temp = lst[front]
		lst[front] = lst[end]
		lst[end] = temp
		front+=1
		end-=1
	return lst
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]

def capitalize_list_items(lst):
	for l in range(len(lst)):
		lst[l] = lst[l].capitalize()
	return lst
print(capitalize_list_items(["item", "string", "print"]))

def add_item(lst, item):
	lst.append(item)
	return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

def remove_item(lst, item):
	lst.remove(item)
	return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(num):
	sum = 0
	for i in range(num+1):
		sum += i
	return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odds(num):
	sum = 0
	for i in range(num+1):
		if (i % 2) is 1:
			sum  += i
	return sum
def sum_of_evens(num):
	sum = 0
	for i in range(num+1):
		if (i % 2) is 0:
			sum  += i
	return sum
print("sum of odd {}".format(sum_of_odds(20)))
print("sum of even {}".format(sum_of_evens(20)))

#level 2
def even_and_odds(num):
	even = 0
	odd = 0
	for i in range(num+1):
		if i % 2 is 0:
			even +=1
		else:
			odd +=1
	dic = {"even": even, "odd": odd}
	return dic
print(even_and_odds(20))

def factorial(num):
	fact = 1
	for i in range(num+1):
		if i is 0:
			continue
		else:
			fact *= i
	return fact
print("6! = {}".format(factorial(6)))

def is_empty(item):
	if item:
		return True
	return False
item = None
print(is_empty(item))
item = 5
print(is_empty(item))

def greet(name = 'Guest'):
	return "Hello, {}!".format(name)
print(greet())
print(greet("Jeff"))