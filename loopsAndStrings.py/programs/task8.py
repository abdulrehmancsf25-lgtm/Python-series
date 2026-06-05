num = int(input('enter thr number to convert into string: '))
str1 = '0123456789'
newstr = ''
while num != 0:
 # newstr += str1[num%10]
  newstr = str1[num % 10] + newstr
  num //= 10
#str1 = newstr[::-1]
print(newstr)
