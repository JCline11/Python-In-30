# Exercise for day 4 of Python in 30 days
string = ["Thirty" , "Days" , "Of" , "Python"]
strcon = " ".join(string)
print(strcon)

company = "Coding" + " " + "For" + " " + "All"
print(company)
print(len(company))

company = company.upper()
company = company.lower()

print(company.capitalize())
print(company.title())
print(company.swapcase())

company = company.title()

print(company[7:])
print(company.index("Coding"))

company = company.replace("Coding", "Python")

print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")
company = "Coding For All"

print(company[0])

print(company[-1])

print(company[10])

text = "Python For Everyone"
print("".join( word[0] for word in text.split()))

text = "Coding For All"
print("".join( word[0] for word in text.split()))

print(text.index("C"))

print(text.index("F"))

print("Coding For All People".rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
a = sentence.find("because")
b = sentence.rfind("because")

print(sentence[a:b + len("because")])

print(text.startswith("Coding"))
print(text.endswith("Coding"))

print("  Coding For All     ".strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

print("# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = int(3.14 * radius ** 2)
print("The area of the circle with radius {} is {} meters square.".format(radius, area))

a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))