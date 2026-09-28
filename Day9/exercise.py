# Code for day 9 exercise

# level 1
age = int(input('Enter your age: '))
if age >= 18:
	print('You are old enough to learn to drive.')
else:
	print('You need {} more years to learn to drive'.format(18 - age))

my_age = 24
your_age = int(input('Enter your age: '))
if my_age > your_age:
	print('I am {} years older than you.'.format(my_age-your_age))
elif your_age > my_age:
	print('You are {} years older than me.'.format(your_age-my_age))
else: 
	print('We are the same age.')

num1 = int(input('Enter nubmer 1'))
num2 = int(input('Enter nubmer 2'))
if num1 > num2:
	print('{} is greater than {}'.format(num1, num2))
elif num1 < num2:
	print('{} is greater than {}'.format(num2, num1))
else:
	print('{} is equal to {}'.format(num1, num2))

