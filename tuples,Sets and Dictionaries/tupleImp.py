 # unpacking tuple into variables BUT size must be equal (equal no. of variables)
t1 = (1,2)
a,b = t1
print(a,b)

# a = (1,2) --> Gives Error

# if you want some items only 
a,b,*other = (1,2,3,4,5,6) # others are sent into list 
print(a,b)
print(other)

#zip function
t1 = (1,2,3,4)
t2=tuple(reversed(t1))
pack =zip(t1,t2) # --> just like reversed zip gives zip object
 #print(tuple(pack)) # 2d tuple
print(list(pack)) # list of tuples
print(tuple(pack))

# type case
print(tuple('hello'))
print(tuple([1,2,3]))