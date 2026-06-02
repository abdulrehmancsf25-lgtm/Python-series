'''Problem 13:Given string contains a combination of the lower and upper case letters.
 Write a program to arrange the characters of a string so that all lowercase letters should come first.
Given:
str1 = PyNaTive

Expected Output:
yaivePNT
'''
# Code here
str1 = input()
str2 = ""
str3 = ""
for i in str1:
  if i.islower():
    str2 += i
  else:
    str3 += i 
print(str2+str3)