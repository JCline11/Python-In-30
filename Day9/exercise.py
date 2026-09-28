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

num1 = int(input('Enter nubmer 1: '))
num2 = int(input('Enter nubmer 2: '))
if num1 > num2:
	print('{} is greater than {}'.format(num1, num2))
elif num1 < num2:
	print('{} is greater than {}'.format(num2, num1))
else:
	print('{} is equal to {}'.format(num1, num2))

# level 2
score = int(input('Enter a score 0 - 100: '))
if score >= 90:
	print('Your score {} got an A'.format(score))
elif score >= 80:
	print('Your score {} got a B'.format(score))
elif score >= 70:
	print('Your score {} got a C'.format(score))
elif score >= 60:
	print('Your score {} got a D'.format(score))
else:
	print('Your score {} got an F'.format(score))

month = input('Enter a month: ')
if month == 'September' or month == 'October' or month == 'November':
	print('The season is Autumn.')
	
elif month == 'December' or month == 'January' or month == 'February':
	print('The season is Winter.')
	
elif month == 'March' or month == 'April' or month == 'May':
	print('The season is Spring.')
	
else:
	print('The season is Summer.')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit not in fruits:
	fruits.append(fruit)
	print(fruits)
else:
	print('That fruit already exist in the list')

# level 3 
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person.get('skills') is not None:
	print(person.get('skills')[len(person.get('skills')) // 2])
	if('Python' in person.get('skills')):
		print('Python is a skill.')
	else:
		print('Python is not a skill.')

	if(len(person['skills']) is 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']):
		print('He is a front end developer')
	elif('Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB' in person['skills']):
		print('He is a fullstack developer')
	elif('Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']):
		print('He is a backend developer')
	else:
		print('unknown title')


if person.get("is_married"):
	print('{} {} lives in {}. They are married'.format(person['first_name'], person['last_name'], person['country']))
else:
	print('{} {} lives in {}. They are not married'.format(person['first_name'], person['last_name'], person['country']))