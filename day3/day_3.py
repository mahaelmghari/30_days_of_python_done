import math

x = 26 #age
y = 1.52 #height
z = 5 + 9j #complex number

##############################################

# area of the triangle A = 0.5 * b  * 

b = float(input('Enter base: '))
h = float(input('Enter height: '))

area = b * h * 0.5
print('The area of the triangle is', area)

# perimeter of the triangle p = a + b + c

a = float(input('Enter side a:'))
b = float(input('Enter side b:'))
c = float(input('Enter side c:'))

p = a + b + c
print('The perimeter of the triangle is', p)

# calculate the area and perimeter of a rectangle using prompt
# area = lenght * width
# perimeter = 2 * (lenght + width)

lenght = float(input('Enter lenght:'))
width = float(input('Enter width:'))

area_rectangle = lenght * width
perimeter_rectangle = 2 * (lenght + width)

print('The area of the rectangle is', area_rectangle)
print('The area of the perimeter is', perimeter_rectangle)

# calculate the area and circumference of a circle
pi = 3.14
r = float(input('Enter the radius:'))

area_circle = pi * r * r
circumference = 2 * pi * r

print('The area of the circle is', area_circle)
print('The circumference of the circle is', circumference)

# calculate the slope x-intercept and y-intercept of y = 2x - 2
# y = mx + b
m = 2
b = -2

x_intercept = -b / m
y_intercept = b
print("X intercept: ", x_intercept)
print("Y intercept: ", y_intercept)
print("Slope: ", m)

# slope is (m = y2-y1 / x2 - x1). Find the slope and Euclidean distance between point (2, 2) and point (6, 10)
# x1 = 2    x2 = 6  y1 = 2  y2 = 10
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m2 = (y2 - y1) / (x2 - x1)
print("Slope bewteen point (2, 2) and point (6, 10)")
print("m:", m2)

#euclidean distance d = sqrt((x2-x1)**2 + (y2-y1)**2)
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Euclidean distance between the two points:", d)

# compare the slope in tasks 8 and 9
print(m >= m2)

# find the lenght of ' python' and 'dragon' and make a falsy comparison statement
print(len('python') != len('dragon')) #False

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# there is no 'on' in both dragon and python
print('on' in 'drangon', 'on' in 'python')

# even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python
number = int(input("Enter a number: "))
if(number % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 == int(2.7))
#check if type of '10' is equal to type of 10
print(10 == 10)
#check if int('9.8') is equal to 10 
print(int(9.8) == 10)

#write a script that promps the user to enter hours and rate per hour. calculate pay of the person
hours = float(input("Enter hours:"))
rate = float(input("Enter rate per hour:"))
pay = rate * hours
print("Your weekly earning is", pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live.
years = int(input("Enter number of years you have lived:"))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# write a python script that dislpays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
