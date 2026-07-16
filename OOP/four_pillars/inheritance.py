# # inheritance sign is ◀ in class diagram 
class Parent: 
    def __init__(self, name , pin):
        self.name = name 
        self.pin = pin 
    def printing_details(self):
        print(self.name , self.pin)

# child class 
class Child(Parent): # syntax
    
    def __init__(self , name , pin ): # constructor overriding        
        super().__init__(name , pin ) # super used to call parent constructor 
        self.name = 'abdul' # changing name attribute 
    
c1 = Child("usman" , 1234)
c1.printing_details()

# Inheritance main purpose is code reuseability
# DRY RULE IN PROGRAMMING -> Don't repeat yourself 

# method overrriding 
class Prt:
   def greet(self):
       print("ho from parent class ")

class chld(Prt):
    def greet(self):
        print(" hi from child ")
        super().greet()
    

x = chld()
x.greet()
# super is in built_in function as well as reserved keyword in python 
super(chld , x).greet()
#You can use it anywhere in your code—even in global scope—
# if you explicitly pass the class and the instance to it.