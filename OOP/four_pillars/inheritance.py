# inheritance
# there are 2 types of relationship betweeen class 
# 1) Aggregation(a class owns another class e.g. A user has an address)
class Address: 
    def __init__(self,state,city,town ):
        self.state = state
        self.city = city
        self.__town = town # private it for user privacy 

    # other class cann't access private variable(except : _Address__town which we donn't use)
    def get_town(self): # so getter is made to get it 
        return self.__town
class user:
    def __init__(self,name , phone_No,Address):
        self.__name = name 
        self.__phone_No = phone_No
        self.__address = Address 
    def user_details(self):
        print("User name :" , self.__name)
        print("Phone Number :" , self.__phone_No)
        print("Address details : ")
        print("State : ", self.__address.state)
        print("City :" ,self.__address.city)
        print("Town :" , self.__address.get_town())

# # now test it 
# address_user_1 = Address("Pakistan" ,"Lahore" ,"TownShip")
# user1= user("Abdul" , "+92123456789" ,address_user_1)
# user1.user_details()
d ={}
d[1]= 56
d[0] = 1
print(d)