# Day 2: 430 days of python programming

first_name = 'mario'
last_name = 'rossi'
full_name = 'mario rossi'
country = 'italy'
city = 'milan'
age = '40'
year = '2026'
is_married = True
is_true = False
is_light_on = True
skills = ['HTML', 'CSS', 'JS']

print(type('mario'))
print(type('rossi'))
print(type('mario rossi'))
print(type('italy'))
print(type('milan'))
print(type(40))
print(type(2026))
print(type(True))
print(type(False))
print(type(True))
print(type(['HTML', 'CSS', 'JS']))

print(len(first_name))
print(len(first_name), len(last_name))

if len(first_name) > len(last_name):
    print('The first name is longer')
else:
    print('The last name is longer')

num_one = 5
num_two = 4
total = (num_one + num_two)
print('5 + 4 = ', total)

diff = (num_one - num_two)
print('5 - 4 = ', diff)

product = (num_one * num_two)
print('5 * 4 = ', product)

division = (num_one / num_two)
print('5 / 4 = ', division)

remainder = (num_two % num_one)
print('5 % 4 = ', remainder)

exp = (num_one ** num_two)
print('5 ** 4 = ', exp)

floor_division = (num_one // num_two)
print('5 // 4 = ', floor_division)

# radius of a circle = 30 meters 
# area of the circle  A = pi*radius^2
r = 30 
pi = 3.14

area_of_circle = (pi * (r ** 2))
circum_of_circle = (2 * pi * r)
print('Area: ', area_of_circle, ', Circumference: ', circum_of_circle)

# Take radius as user input and calculate the area.
radius = float(input('Enter the radius: '))
area = (pi * (radius ** 2))
print('Area: ', area)


first_name = input('First name: ')
last_name = input('Last name: ')
country = input('Country: ')
age = input('Age: ')

print('You are', first_name, last_name, 'from', country)
print('You are', age, '80years old.')
