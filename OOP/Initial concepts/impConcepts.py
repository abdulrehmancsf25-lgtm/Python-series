# instance variable
# class variable 
# local variable 
# reference variable 

# in python by default user_defined objects are mutable
# by default attributes & methods are public 
class Hero:
    def __init__(self  , name , age ):
        self.name = name 
        self.age = age 
    
p1 = Hero('abdul' , 19)  # p1 and p2 are refernces variables for objects 
p2 = Hero('usman' , 25)

print(id(p1.name))
print(id(p2.name))
        