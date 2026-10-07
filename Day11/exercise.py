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

