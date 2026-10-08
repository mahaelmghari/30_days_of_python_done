lst = list() #syntax
empty_list = list() #empty list no items in the list
print(len(empty_list)) #0

lst = [] #syntax
empty_list = [] #empty list no items in the list
print(len(empty_list)) #0

#we use len() to find the lenght of a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))

#accessing list items using negative indexing: it means beginning from the end, -1 referts to the last item, -2 refers to the second last item and so on.
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_last)

#accessing list items using positive indexing: it means beginning from the start, 0 refers to the first item, 1 refers to the second item and so on.
fruits = ['banana', 'orange', 'mango', 'lemon']     
first_fruit = fruits[0]
print(first_fruit)

#unpacking list items
lst = ['item1', 'item2', 'item3', 'item4']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10] 
print(first)
print(second)
print(third)
print(rest)
print(tenth)

countries = ['germany', 'france', 'belgium', 'sweden', 'denmark', 'finland', 'norway', 'estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#slicing items from a list
fruits2 = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits2[0:4:] #it returns all the fruits
all_fruits = fruits2[0:] #same thing as the one above
orange_and_mango = fruits2[1:3]
orange_mango_lemon = fruits2[1:]
orange_and_lemon = fruits2[::2] #we used a 3rd argument step. It will take every 2cnd item

#modifying lists
frutta = ['banana', 'orange', 'mango', 'lemon']
frutta[0] = 'avocado'
print(frutta)
last_index = len(frutta) -1
frutta[last_index] = 'lime'
print(frutta)

#adding items to a list
#syntax
#lst = lst()
#lst.append(item)

fruttas = ['banana', 'orange', 'mango', 'lemon']
fruttas.append('apple')
print(fruttas)
fruttas.append('lime')
print(fruttas)

#insterting items into a list
fruttam = ['banana', 'orange', 'mango', 'lemon']
fruttam.insert(2, 'apple')
print(fruttam)
fruttam.insert(3, 'lime')
print(fruttam)

#removing items from a list
fruttish = ['banana', 'orange', 'mango', 'lemon']
fruttish.remove('banana')
print(fruttish)

#removing items using pop
fruttish.pop() #last item
print(fruttish)
fruttish.pop(0)
print(fruttish)

#removing itrem using del
frutt = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del frutt[0]
print(frutt)
del frutt[1:3] #deletes items between given indexes
print(frutt)

#clearing list items
frutto = ['banana', 'orange', 'mango', 'lemon']
frutto.clear()
print(frutto)

#copying a list
frut = ['banana', 'orange', 'mango', 'lemon']
frut_copy = frut.copy()
print(frut_copy)

#joining lists
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fru = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fru + vegetables
print(fruits_and_vegetables)

#joining using extend() method. It allows to append list in a list
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)

#counting items in a list
fr = ['banana', 'orange', 'mango', 'lemon']
print(fr.count('orange'))

#finding index of an item
f = ['banana', 'orange', 'mango', 'lemon']
print(f.index('orange'))

#reversing a list 
ft = ['banana', 'orange', 'mango', 'lemon']
ft.reverse()
print(ft)

#sorting list items
ftr = ['banana', 'orange', 'mango', 'lemon']
ftr.sort()
print(ftr) #sorted in alphabetical order
ftr.sort(reverse=True)
print(ftr)

print(sorted(ftr))
ftr = sorted(ftr,reverse=True)
print(ftr)
