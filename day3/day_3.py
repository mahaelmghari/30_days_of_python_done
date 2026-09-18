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
