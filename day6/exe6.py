#1
tpl = ()
print(tpl)
#2
sisters = ('sister1', 'sister2')
brothers = ('brother1', 'brother2')
#3
siblings = sisters + brothers 
print(siblings)
#4
print(len(siblings))
#5
siblings = list(siblings)
siblings.insert(4, 'father')
siblings.insert(5, 'mother')
family_members = siblings
print(family_members)

#LEVEL 2
#1
siblings = family_members[:4]
parents = family_members[4:]
print(siblings, parents)
#2
fruits = ('banana', 'orange', 'mango', 'lemon','kiwi')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('chicken','beef', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
#4
print(len(food_stuff_lt))
middle_item = food_stuff_lt[6]
print(middle_item)
#5
first_three = food_stuff_lt[3:]
last_three = food_stuff_lt[:10]
print(first_three)
print(last_three)
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)