d0 = {'name':'Mobiles','Types':{
                                'KeyPad Phone':{
                                    'Nokia' :'Model 161',
                                    'Q mobile':'Model 2005'

                                },
                                'Touch phone': {
                                    'Samsung':'Model S22 ultra',
                                     'Iphone':'Model 14pro max'
                                }
                                }
}
import json 
print(json.dumps(d0,indent=4))
print(d0['name'])
print(d0['Types'])

#  type conversion
d0 = dict(name = 'Abdul',degree = 'BSCS',semester = '3rd')

lst1 = ['university-name*','student-contact*','location']
lst2 = ['PUCIT','03265858565']
d1 = dict(zip(lst1,lst2))

d2 = dict([('LA','A'),('DLD','A'),('PF','A-')])

print(d0)
print(json.dumps(d1,indent=4))
print(*d2.items(),sep='\n')


