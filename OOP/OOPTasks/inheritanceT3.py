from abc import ABC , abstractmethod
class Polygon(ABC):
    def take_dimensions(self , base , height):
      self.__base = base 
      self.__height = height 
    
    # getters
    def getBase(self):
       return self.__base
    def getHeight(self):
      return self.__height
    
    # abstract method
    @abstractmethod
    def area(self):
       pass

# first child class
class Triangle(Polygon):
   def area(self):
      return 0.5 * self.getBase() * self.getHeight()

class Rectangle(Polygon):
   def area(self):
      return self.getBase() * self.getHeight()

# we cann't make an instance of parent class in abstraction
Tr1 = Triangle()
Tr1.take_dimensions(2,6)
R1 = Rectangle() 
R1.take_dimensions(2,6)


def get_area(shape : Polygon): 
   print(shape.area())

# calling function
get_area(Tr1)


   
      