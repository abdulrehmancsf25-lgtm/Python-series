#Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero.
#  Display the sum and average of all the numbers.
print('0 is a sentimental value ')
num = int(input('Enter number ')) 
count = 0 
sum = 0 
while(num != 0):
  count += 1 
  sum += num 
  num = int(input('enter the number '))
print('sum of all numbers is : ' , sum )
if count !=0:
   print('average of all numbers is ' , sum/count)
else :
  print('average of all numbers is  0')