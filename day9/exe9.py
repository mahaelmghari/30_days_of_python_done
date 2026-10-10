#1
age = int(input("Enter your age:"))
if age >= 18:
    print("You are old enough to drive.")
else:
    years = 18 - age
    print("You need", years,"more years to learn to drive.")
#2
my_age = 26
your_age = int(input("Enter your age:"))
if your_age == my_age:
    print("We are the same age")
elif your_age == 27:
    print("You are 1 year older than me")
elif your_age > my_age:
    age_gap = your_age - my_age
    print("You are", age_gap, "years older than me")
else:
    print("I am older than you")
#3
a = float(input("Enter number one:"))
b = float(input("Enter number two:"))
if a > b:
    print(a,"is greater than", b)
elif a < b:
    print(a,"is less than", b)
else:
    print(b,"is equal than", a)

#LEVEL 2
#1
score = float(input("Enter score:"))
if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score <= 89:
    print("Your grade is B")
elif 70 <= score <= 79:
    print("Your grade is C")
elif 60 <= score <= 69:
    print("Your grade is D")
else:
    print("Your grade is F")
#2
month = input("Enter a month:")
winter = ['December','January','February']
spring = ['March','April','May']
summer = ['June','July','August']
autumn = ['September','October','November']
if month == winter:
    print("It's winter")
elif month == spring:
    print("It's spring")
elif month == summer:
    print("It's summer")
elif month == autumn:
    print("It's autumn")