'''
str1 = input('enter string to get its length ')
count = 0 
for i in str1:
  count += 1
print('length of given string ',str1 ,'is ',count)

str1 = input('Enter you gmail to extract user-name : ')
str1 = str1[:str1.find('@')]
print(str1.capitalize())
'''
str1,char = input('enter string & character separated with comma ' \
'to find its frequency : ').split(',')
print(char,' repeats ',str1.count(char),' times ')



