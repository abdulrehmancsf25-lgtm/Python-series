#Problem-1: Class inheritence
#Create a Bus child class that inherits from the Vehicle class.
#  The default fare charge of any vehicle is seating capacity * 100.
#  If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
#  So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

#Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
# You need to override the fare() method of a Vehicle class in Bus class.

class Vehicle:
    def __init__(self , capacity ):
        self.__capacity = capacity

    def fare(self):
        return self.__capacity * 100
    
class Bus(Vehicle):
    def fare(self):
        temp_fare = super().fare()   # use super().fare() to sharply use parent method 
        final_fare = 0.10  * temp_fare + temp_fare
        return int(final_fare)
Bus1 = Bus(50)
print(Bus1.fare())
        