'''Dictionary
Dictionary in Python is a collection of keys values,
used to store data values like a map,
which, unlike other data types which hold only a single value as an element.

In some languages it is known as map or assosiative arrays.
dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }
Characterstics:

Mutable
Indexing has no meaning
keys can't be duplicated
keys can't be mutable items'''
# empty dictionary
d0 = {}
print(type(d0))

#   1D Dictionary
d1 = {'name':'abdul','age':21}
print(d1)
 
# 2D dictionary
import json


d2 = {'name':'Abdul Rehman',
      'degree':'BSCS',
      'semester':'2nd',
      'subjects':{
          'LA': 'A',
          'DLD': 'A',
           'PF':'A'}
      }
print(json.dumps(d2, indent=4))

# type cast
#1st method
info = dict(name = 'Abdul Rehman',gender = 'Male',country = 'Pakistan',current_degree = 'BSCS')
print(*info.items(),sep="\n")
print(json.dumps(info,indent=3))

#2nd method
d0 = dict([('name','Abdul')])
print(d0)