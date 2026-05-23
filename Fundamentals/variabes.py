name  = 'Abdul'
name *= 2
print(name)
# ouput --> AbdulAbdul
a = 5 ; b = 3
print(a + b)

# Dynamic typing VS Static typing
# Python supports dynamic typing means we don;t need to define data type of variable
# Vice versa C++ is static typing language means we have to define type like int a = 5 ;
#python style
age = 5 

# Dynamic VS Static binding(yo change datatype of variable after intialization)
a = 5
print(a)
a = 1.5
print(a)
a = True
print(a)

#multi Variables  Stylish declaration techniques
a = 3 ; b = 4 
print(a + b)
# OR
a,b = 1,2
print(a + b)
a = b =  c = 45
print(a , b , c)