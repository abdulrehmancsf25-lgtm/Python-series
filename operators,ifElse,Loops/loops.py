# digit sum program using simple while loop
'''
num = int(input('Enter the number to get digit sum '))
ans =  0
while num != 0 :
    ans += num % 10
    num //= 10 
print('digit sum is ' ,ans)
'''
          # WHILE LOOP WITH ELSE 
#guess number  
'''         
import random
target = random.randint(1,100)
guess = int(input('Guess the number '))
count = 1
while guess != target :
    if (guess > target) :
        print('your guess is higher than target')
    else :
        print('your guess is lower than target ')
    count += 1 
    guess = int(input('Guess the number again '))
else :
    print('Your guess is correct ')
    print('total attempts : ' , count )'''
           #    FOR LOOP
'''
for i in range(1,11) :
    if i == 10 :
        print(i)
    else :
      print(i, end=' ')
for i in range(10,0,-1):
   print(i , end=' ')
print()
for i in range(0,10):
   if i & 1 :
      print(i ,end=' ')
'''
# for loop with else
import math
num = int(input('Enter the number to check for prime '))
if num <= 1 :
    print(num , 'is not a prime number')
else :
    for i in range(2,int(math.sqrt(num)+1)):
       if num % i == 0 :
         print(num , 'is not a prime number')
         break 
    else :
        print(num ,'is a  prime number ')
 
# for loop in strings , lists
for j in 'Delhi'  :
   print(j,end=' ')
print()
for j in [1,2,3,4,5] :
   print(j,end=' ')