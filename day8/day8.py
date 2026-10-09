#dictionary
#creating a dictionary
empy_dic = {}
dct = {'key1':'value1',
       'key2':'value2',
       'key3':{
           'key2.1':'value2.1'
       }}
#dictionry lenght
len(dct)
#accessing dictionary items
dct = {'key1':'value1',
       'key2':'value2',
       'key3':{
           'key2.1':'value2.1'
       }}
print(dct['key1']) #value1
#accessing items by key name
print(dct.get('key1')) #value1
#adding items to a dictionary
dct['key4'] = 'value4'
#modifying items in a dictionary
dct['key1'] = 'value-one'
#checking keys in a dictionary
print('key2' in dct) #true   
print('key5' in dct) #false
#removing key and value pairs from a dictionary
dct.pop('key1') #removes key1 item
dct.popitem() #removes the last item 
del dct['key2'] #removes key2 item
#changing dictionary to a list of items
dct = {'key1':'value1','key2':'value2'}
print(dct.items()) #dict_items([('key1', 'value1'), ('key2', 'item2')])
#clearing a dictionary
print(dct.clear()) #none
#deleting
del dct
#copy
dct_copy = dct.copy()
#getting dictionary keys as a list
keys = dct.keys()
print(keys) #dict_keys(['key1', 'key2'])
#getting dictionary values as a list
values = dct.values()
print(values)

