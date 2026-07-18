# class point
class point :
    def __init__(self , x ,y):
        self.__x = x
        self.__y = y 
    
    # representation 
    def __repr__(self):
        return "({},{})".format(self.__x , self.__y)
    
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

class Location:
    def __init__(self , source , dest ):
        self.__souceObj = source
        self.__destObj = dest
    def reflectionOfDest(self):
      return point(self.__destObj.getX() , self.__destObj.getY()*-1)
    
p1 = point(1,2)
print(p1)

src1 = point(3,4)
dest1 = point(4,7)

print("Source : {}".format(src1))
print("Destination : {}".format(dest1))

loc_1 = Location(src1 , dest1)
print("Reflection of destination : " , loc_1.reflectionOfDest())
        