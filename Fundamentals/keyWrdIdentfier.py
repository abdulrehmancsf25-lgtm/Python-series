#keyWoeds(reserved words  : 39  in python)
# e.g print ,if ,is, as , not , for, while , local .etc.
#Identifiers (names of  variables , functions , class that we assign by ourselves)
#  _, digits , alphapbets
'''
first_name = 'abdul'
print(first_name)
_ = 34
print(_)

# USER INPUT
print('Enter your name ' , end='  ')  ; name   = input()
print(name*2) 
'''
'''
alpha = input('Enter your age ')
print('your age is ' , alpha)
print('Enter two numbers',end=' ')
num1 , num2 = input() ,input()
#print(type(num1)) # pythin bydefault stores in string due to universal dataType
# WE HAVE TO TYPE CAST

result  = int(num1) + int(num2 )
print(result)
'''
'''
# TYPE CASTING (EXPLICIT)
num1 , num2 = input().split()
# .split() divides tge string
print(int(num1) + int(num2))
x , y , z = input().split()
print(int(x) + int(y) + int(z))

# str() FOR TYPE CAST INTO STRING 
print(str(8))
# bool type cast
print(bool(-1)) # output --> True 

num1 , num2 , num3 = 0b1010, 0o137 , 0x23fc 
                #     Bin    octal   hexDecimal
print(num1 , num2 , num3 )
'''
#split() by default separates (space , tabspace ,newline)
a , b = input().split() #abdul,rehman (separate abdul rehman )
print(a , b)
name = 'Abdul Rehman'
