#1
empty_list = list()
#2
items = [1, 2, 3, 4, 5]
#3
print('Lenght of the list:', len(items))
#4
first_item = items[0]
middle_item = items[2]
last_item = items[4]
print('First item:', first_item)
print('Middle item:', middle_item)
print('Last item:', last_item)
#5
mixed_data_types = ['name', 200, 150, 'divorced', 'italy']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print('Companies:', it_companies)
#8
print('Number of companies in the list:', len(it_companies))
#9
first_c = it_companies[0]
middle_c = it_companies[3]
last_c = it_companies[-1] #-1 it's always the last item on the list even if the list changes
print('First company:', first_c)
print('Middle company:', middle_c)
print('Last company:', last_c)
#10
it_companies.pop(-1) #it removes the last item
print(it_companies)
#11
it_companies.append('NVIDIA')
print(it_companies)
#12
it_companies.insert(3, 'Samsung')
print(it_companies)
#13
it_companies[1] = it_companies[1].upper()
print(it_companies)
#14 join the list with a string '#: '
print('#: '.join(it_companies))
#15
print(it_companies.count('IBM'))
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
del it_companies[:3]
print(it_companies)
#19
del it_companies[-3:]
print(it_companies)
#20
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies[3]
print(it_companies)
#21
del it_companies[0]
print(it_companies)
#22
del it_companies[3]
print(it_companies)
#23
del it_companies[-1]
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
develop = front_end + back_end 
print(develop)
#27
full_stack = develop.copy()
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#LEVEL 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('Min age:', min(ages))
print('Max age:', max(ages))
ages.append(min(ages))
ages.append(max(ages))
print(ages)
