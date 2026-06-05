'''Take a alphanumeric string input and print the sum and average of the digits that appear in the string, 
ignoring all other characters.
Input:
hel123O4every093

Output:
Sum: 22
Avg : 3.142
'''
'''
# Code here
str1 = input()
sum ,count = 0,0
for i in str1 :
  if i.isdigit():
    count += 1
    sum += int(i)
print(sum)
print(sum/count)
'''
a = input()
b = input()
c = input()
print(type(a),type(b))
a,b,c = map(int,[a,b,c])
print(type(a),type(b))


