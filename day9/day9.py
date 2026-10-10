#CONDITIONALS
#if
a = 3
if a > 0:
    print("A is a positive number")
#if else
a = 3
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")
#if elif else (for multiple conditions)
a = 0
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is a zero")
#short hand
a = 3
print("A is positive") if a > 0 else print("A is negative") 
#if condition and logical operations
a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is positive integer")
elif a == 0:
    print("A is a zero")
else:
    print("A is negative")
#if and or 
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied!")