# baic class format 
# IN python only object can access the datamembers or methods of a class
# Even a function of class cann't call another function of class
# For this issue self keyword is used which is the object itself 
class Hero:
    hi = 56
    def __init__(self,stname,age):
      self.name = stname
      self.age = age
      print('hello')
      self.details()
    
    def details(self):
       print('Name :',self.name)
       print('Age',self.age)
# basic object format

h1 = Hero('abdul',20)
h2 = Hero('usman',26)
# print(h1.hi)
Hero.hi = 30

print(h2.hi)












# list is a class in python
# format of list object
# arr = list() # or arr = [] for ease
# L = [1,2,3]
# print(type(L))

