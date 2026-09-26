# Coding exercise for day 7 python

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# level 1
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['FromSoft', 'Ricoh', 'Tik Tok'])
it_companies.remove('IBM')
it_companies.discard('IBM')
# remove raises an error if the item is not present in the set. Discard does not raise error if not present.

# level 2
print(A.union(B))
print(A.intersection(B))
print('A subset B? ', A.issubset(B))
print('A and B disjoint? ', A.isdisjoint(B))
print('A join B ', A.union(B))
print('B join A ', B.union(A))
print(A.symmetric_difference(B))
del A
del B

# level 3
age_st = set(age)
print('set length: ', len(age_st))
print('list length: ', len(age))
# a list[] is iterable and modifiable, a tuple() is iterable but you can not modify the contents after creation, 
# a set{} can contain no duplicates and cannot be indexed. You cannot modify items once theyre added but you can add and remove items.
# a string is a data type used to store a collection of characters in a particular order
sen = 'I am a teacher and I love to inspire and teach people.'
sen_st = set(sen.split(" "))
print('Unique words in \'{}\': {}'.format(sen, len(sen_st)))