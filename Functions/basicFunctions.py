 # Basics
def is_even(num):
  """ To check if function is even or not """
  num = int(num)
  return 'Even' if num % 2 == 0 else  'False'
print(is_even('8'))
  
# Argument types
# 1 - DEFAULT 
def power(a=1,b=1):
  return a**b
print("power :",power(2,3) )
print("power :",power())
print("power :",power(2))
print()

# LOCAL VS GLOBAL VARIABLES 
# local variable has more precedence over global variable
def printing(x):
  x += 3
  print(x)
y = 6
x = 5
printing(x)
print('original x :',x)

# again imp concept
# int are immutable so x +=4 creates a copy 
def newprint(x):
  x += 4
  print(x)
y = 5
newprint(y)
print('original y:',y)

# For mutable items 
def print_list(lst):
  for i in range(len(lst)):
    lst[i] += 1 
  return lst 
arr = [1,2,3,4,5]
new = print_list(arr)

print(arr)
print(new)