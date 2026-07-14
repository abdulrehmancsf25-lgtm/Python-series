#Write your code here
class Scoop:
  scoops_sold = 0 
  def __init__(self,flavor):
    self.flavor = flavor
    self.__price = 0
    self.__quantity = 1
   
  # set the price of a flavor per scoop
  def Set_ScoopPrice(self ,price):
    if type(price) == int:
      if price < 0 :
        raise ValueError("Price cann't be negative! ")
      else:
        self.__price = price
    else:
      raise TypeError("""Please set price again!
            System Error """) 
    if self.__price > 0 :
       Scoop.scoops_sold += 1
  # getter 
  def getScoop_Price(self):
      return self.__price
  def Set_Scoop_Quantity(self,quantity):
    self.__quantity = quantity
  def get_Qnt(self):
    return self.__quantity
  def __str__(self):
    return "Flavor - {} , Price - {}".format(self.flavor , self.__price)
  
  @classmethod
  def Sold(cls):
    print("Scoops sold : ", Scoop.scoops_sold)
# Bowl class 
class Bowl:
    bowls_sold = 0 
    def __init__(self,capacity=3):
      self.__scoops_list = list()
      self.__capacity = capacity
      self.__curr_capacity = 0
      Bowl.bowls_sold += 1
     
    
    def add_scoops(self,*flavors):
      for scoop in flavors:
        if self.__curr_capacity == self.__capacity:
          print("Bowl is full")
          print(scoop.flavor , " is not added ")
          print("No further capacity ")
          return
        else:
          print(scoop.flavor," is added ")
          flavor_Qnt = 0
          for i in range(1,scoop.get_Qnt()+1): # make getqnt function 
            self.__curr_capacity += 1
            flavor_Qnt += 1
            if self.__curr_capacity == self.__capacity:
              self.__scoops_list.append((scoop.flavor,flavor_Qnt))
              break 
          else:
            self.__scoops_list.append((scoop.flavor , scoop.get_Qnt()))
              

       

    def display(self):
      for i in self.__scoops_list:
        print("Flavor : {} ,No. of scoops : {}".format(i[0],i[1]))

    def bowl_price(self):
     pass 
    
    @classmethod
    def Sold(cls):
      print("Bowls sold : " , Bowl.bowls_sold)


# test 

# scoop1 
vanilla = Scoop("Vanilla")
vanilla.Set_Scoop_Quantity(2)
vanilla.Set_ScoopPrice(150)
#print(vanilla)

# scoop 2 
mango = Scoop("Mangoo")
mango.Set_ScoopPrice(200)
#print(mango)

# scoop 3
choco = Scoop("Choco")
choco.Set_ScoopPrice(170)
#print(choco)

# now bowl test
print(" Bowl : 1")
Bowl1 = Bowl()
Bowl1.add_scoops(choco)
Bowl1.add_scoops(mango,vanilla)

Bowl1.display()
Bowl1.bowl_price()

# total scoops and bowls sold
Scoop.Sold()
Bowl.Sold()