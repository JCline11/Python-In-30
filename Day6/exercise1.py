# exercise 1 for day 6 tuples

empty_tuple = ()
brothers = ("Bob", "Joe")
sisters = ("Sarah", "Jasmine")
siblings = brothers + sisters
print(len(siblings))
family_members = siblings + ("Jeff", "Lea")
print(family_members)

#exercise 2 for day 6 tuples

siblings = family_members[:-2]
parents = family_members[-2:]
print(siblings)
print(parents)

fruits = ['apples', 'oranges', 'lemons']
vegetables = ['broccoli', 'brussells', 'corn']
animal_products = ['meat', 'cheese', 'milk']
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
food_stuff_lt = food_stuff_lt[:3] + food_stuff_lt[-3:]
print(food_stuff_lt)
food_stuff_lt = food_stuff_lt[3:]
print(food_stuff_lt)
del food_stuff_lt

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia: ', 'Estonia' in nordic_countries)
print('Iceland: ', 'Iceland' in nordic_countries)