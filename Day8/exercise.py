# exercise for day 8 python

dog = {}
dog['name'] = 'Lily'
dog['color'] = 'white'
dog['breed'] = 'lab'
dog['legs'] = 4
dog['age'] = 18
print(dog)

student = {'first_name': 'Jason', 'last_name': 'Smevog', 'gender': 'male', 'age': 24, 'marital_status': False, 'skills': ['java', 'python', 'html', 'css'], 'country': 'US', 'city': 'Corona', 'address': '3138 Lane'}
print('student dict length: ', len(student))
print('skills {}: {}'.format(type(student.get('skills')),  student.get('skills')))
student.get('skills').append('c++')
print(student.get('skills'))
print(student.keys())
print(student.values())
print(student.items())
student.pop('marital_status')
student.popitem()
del student['city']
print(student)
del student