# class Atm:
#     def __init__(self):
#         self.pin = 0 
#         self.balance = 0
#     def details(self):
#         print(self.pin )
#         print(self.balance)
    
# m1 = Atm()
# m1.details()

# m1.pin = 'hehehe'
# m1.details()

class new_Atm:
    def __init__(self):
        self.__pin = 0 # private instance variable 
        self.balance = 0 
    def details(self):
        print('new_atm pin ' , self.__pin)
        print('new atm balance ' , self.balance)

m2 = new_Atm()
m2.details()
m2.pin = 'hehe' # new attribute created inside class 
# the programmer who is using your object can not chage the private variable 
m2.details()

# if somehow he know your private attribute name and change it it will not change 
# __pin a new private variable will be made in side your object from outside 
# original __pin will act in memory as _new_Atm__pin 
m2.__pin = 'hehehe'
m2.details()

m2._new_Atm__pin = 'hehehe' # it will change the pin into variable and code logics may crash due to string dataType
m2.details()