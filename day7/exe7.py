# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update({'NVIDIA'})
print(it_companies)
#4
it_companies.remove('Facebook')
print(it_companies)
#5
#What is the difference between remove and discard
#it_companies.remove() #it removes the item and gives error if the item doesn't exist
#it_companies.discard() #it removes the item and does nothing if the item doesn't exist 

#LEVEL 2
#1
C = A.union(B)
print(C)
#2
A.intersection(B)
print(A)
#3
A.issubset(B)
print(A)
#4
A.isdisjoint(B)
print(A)
#5
C = A.union(B)
B = B.union(A)
#6
A.symmetric_difference(B)
#7
del A
del B

#LEVEL 3
#1
age_st = set(age)
if len(age_st) > len(age):
    print("The set is bigger than the list.")
else:
    print("The list is bigger than the set.")
#2 teoria
