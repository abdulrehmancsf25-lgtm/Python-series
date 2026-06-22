'''
d0 = {'name':'Abdul','Degree':'BSCS'}
print(d0['name'])
d0['name']= 'Abdul Rehman'
print(d0['name'])

d1 = {'name':'Abdul','subjects':{
                                 'DS':93,
                                  'DSA': 87} 
}
print(d1['subjects']['DS'])


# To add a new key
d0['semester'] = '3rd'

import json
print(json.dumps(d0,indent=4))
'''
d1 = {'name':'Abdul','subjects':{'DSA':90,'MVC':91}}
# adding OOP key
d1['subjects']['OOP'] = 90
print(d1)

# deleting items
#.pop()
d1.pop('name')
print(d1)

# again adding
d1['name'] = 'Abdul'
d2 = dict(reversed(d1.items()))
d1 = d2
d1['subjects'].pop('OOP')
print(d1)

# .popitem removes last key value pair
d1['subjects']['OOP'] = 91
d1.popitem()
print(d1)

# delete 
del d2
del d1['name']
print(d1)

# .clear 
d = {'name':'Lays','Price':50}
d.clear()
print(d)