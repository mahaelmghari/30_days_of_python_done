#1
dog = {}
#2
dog = {'name':'puppy',
       'color':'gray',
       'breed':'husky',
       'legs':'4',
       'age':'2'
       }
#3
student = {'first_name':'Sara',
           'last_name':'Rossi',
           'gender':'female',
           'age':'60',
           'marital_status':'married',
           'skills':'none',
           'country':'Italy',
           'city':'Milan',
           'address':'Duomo'}
#4
print(len(student))
#5
print(student.get('first_name'))
print(student.get('last_name'))
print(student.get('gender'))
print(student.get('age'))
print(student.get('skills'))
print(student.get('marital_status'))
print(student.get('skills'))
print(student.get('country'))
print(student.get('address'))

values = student.values()
print(values)
#6
student['children'] = 'two'
print(student)
#7
student_keys = student.keys()
print(student_keys)
#8
student_values = student.values()
print(student_values)
#9
student_tpl = list(student.items())
print(student_tpl)
#10
del student['skills']
print(student)
#11
del student