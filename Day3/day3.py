# Coding exercise for day 3 of 30

age = 23
height = 6.1
complex_num = 4 + 3j

base = int(input("Enter base: "))
height_triangle = int(input("Enter height: "))
area = 0.5 * base * height_triangle
print("The area of the triangle is: ", area)

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter)

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area: ", area, "Perimeter: ", perimeter)

radius = int(input("Enter radius: "))
area = 3.14 * (radius ** 2)
circumference = 2 * 3.14 * radius
print("Area: ", area, "Circumference: ", circumference)

slope1 = 2
x_intercept = 1
y_intercept = -2
slope2 = (10-2) / (6-2)
print("slope1: ", slope1, "slope2: ", slope2, slope1 is slope2)

x = 3
y = (x**2) + (6*x) + 9
print("y = x^2 + 6x + 9")
print("x = 3, y = ", y)
x = 4
y = (x**2) + (6*x) + 9
print("x = 4, y = ", y)

str1 = len("python")
str2 = len("dragon")
print("length of python is length of dragon", str1 is str2)
print("on in python and on in dragon","on" in "python" and "on" in "dragon")
print("jargon in I hope this class is not full of jargon", "jargon" in "I hope this class is not full of jargon")
print('there is not on in both dragon and python', 'on' not in 'python' and 'on' not in 'dragon')

length = int(len('python'))
leng = float(length)
lenstr = str(leng)
print(lenstr)

print('is even if n % 2 = 0, where n = some integer')
print('7 // 3 is int(2.7)', (7 // 3) is int(2.7))

print('type of 10(str) is equal to type of 10(int)', type('10') is type(10))

print('int(9.8) is 10', int(9.8) is 10)

hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
print('Your weekly earning is: ', hours * rate)

years = int(input('Enter number of years: '))
print('You have lived for ', years * 365 * 24 * 60 * 60, ' seconds.')

for i in range(1,6):
    print(i, 1, i, i**2, i**3)

