from functools import reduce
class frac:
    def __init__(self ,x,y):
        if y  == 0:
          raise ZeroDivisionError("Denominator cannot be zero")
        if y < 0:
          x,y = -x,-y 
        self.num  = x 
        self.den = y 

    def __str__(self):
        return("{}/{}".format(self.num , self.den))
    
    
    def __add__(self,other):
        new_num = self.num*other.den + other.num*self.den
        new_den =self.den*other.den
        return frac(new_num , new_den).simplify()
    
    def simplify(self):
      num = abs(min(self.num , self.den))
      gcd = 1
      for i in range(2,num+1):
         if self.num % i == 0 and self.den % i == 0:
            gcd = i 
      return frac(self.num // gcd,self.den // gcd)
    
    def to_Decimal(self):
       return self.num / self.den      



fr1 = frac(1,2) 
#print(fr1)

#print(frac(-6,-4).simplify())
print( frac(5,3).__add__(frac(1,2)))
