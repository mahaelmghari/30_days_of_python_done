#TUPLE
tlp = ('item1', 'item2', 'item3')

#tuple lenght
tpl = ('item1', 'item2', 'item3')
len(tpl)
#accessing tuple items
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
last_index = len(tlp)
last_item = tpl[last_index]
#negative indexing
first_item = tpl[-4]
second_item = tpl[-3]
#slicing tuples
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4] #all items
all_items = tpl[0:] #all items
middle_two_items = tpl[1:3] #does not include irems at index 3
#range of negative indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4]
middle_two_items = tpl[-3:-1] #does not include item at index 3 (-1)
#changing tuples to lists
tpl = ('item1', 'item2', 'item3', 'item4')
tpl = list(tpl) #tuple is immutable if we want to modifyt a tuple we should change it to a list
#checking an item in a tuple
tpl = ('item1', 'item2', 'item3', 'item4')
print('item2' in tpl)  #true
#joining tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item5', 'item5', 'item6')
tpl3 = tpl1 + tpl2
#deleting tuples
tpl1 = ('item1', 'item2', 'item3', 'item4')
del tpl1

