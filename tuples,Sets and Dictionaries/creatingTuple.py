 # tuples are just like lists but they are immutable
t1 = ()  # empty tuple
t2 = (2,) #single item tuple 
print(t1,t2)
t3 = (1,2,3)  
t4 = t3 + (4,) # creating new tuple with previous tuple
print(t4)

t2 += (3,4 ,5)
print(t2)

item = -321
item //= 10
print(item)

t1 = (1,2,3)
t2 = (1,2,3)
t4 = t2[1:]
print(id(t1),id(t2),id(t4))