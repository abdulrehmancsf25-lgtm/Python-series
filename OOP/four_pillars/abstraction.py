# AI chat to clarify abstraction 
# https://chat.z.ai/s/6448e93e-1899-41d2-b66d-51f2095eab11

# TWO TYPES OF METHOD 
# 1) Concrete method 
# 2) Abstract method (must be overridden)

from abc import ABC , abstractmethod
# abstract class inherits from ABC(Abstract Base Class)
class Vehicle(ABC): # we cann't create an instance of Vehicle class
    def __init__(self , name , engine , model):
        self.__name  = name 
        self.__engine = engine 
        self.__model = model
    def get_name(self):
        return self.__name

    def get_engine(self):
        return self.__engine
    
    def get_model(self):
        return self.__model
    
    # abstract method -> must be overriten in child class    
    @abstractmethod
    def run(self):
        pass

# inheriting Vehicle in our child class
class electric_car(Vehicle):
    # overriding features metof
    def run(self , speed , remainig_battery = 0):
       print(" OUR CAR IS RUNNING AT {}km/h".format(speed))
     #  print("REMAINIG BATTERY IS : {}".format(remainig_battery))
    
class combustion_car(Vehicle):
    def run(self,speed , remaining_fuel = 0):
       print(" OUR CAR IS RUNNING AT {}km/h".format(speed))
     #  print("REMAINIG BATTERY IS : {}".format(remaining_fuel))


# creating objects of child classes
V1= electric_car("Tesla" ,"No engine" , 2026)
V2 = combustion_car("Toyota" ,"2000cc" ,2025)

# now driver has to drive the car 
# he doesno't focus on what is the car type and its internal mechanism
# we hide the complexity of electric and combustion car by abstraction
def drive_car(car : Vehicle):
    print("""
          Car name : {}
          Car engine : {}
          Car model : {}""".format(car.get_name() , car.get_engine() ,car.get_model()))
    car.run(150 )
    print() # for better view in terminal
        

# now we give the car to driver -> he has to drive 
drive_car(V1)
drive_car(V2)   