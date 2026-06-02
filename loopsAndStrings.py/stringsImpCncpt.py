"""
import sys
x = 'a'
print(sys.getsizeof(x))
print(len(x))
st = '''abdul
rehman
arshad'''
print(st)
s = 129
print(str(s))
age = 19
print("my age is "+str(age)+" years old")
"""
# POSITIVE INDEXING(0 TO SO ON LEFT --> RIGHT)
name = 'abdul'
print(name[0]) # print a

# NEGATIVE INDEXING(-1 TO SO ON (LEFT <--- RIGHT))
print(name[-1]) # print l


name  = 'hello world'



# .find function returns first occurence index of a char in string else -1
print('index of i ',name.find('i'))
print('index of space ',name.find(' '))
print('index of l ' ,name.find('l'))
# .index also returns index 
# if char not found not give -1 throughs value Error
print(name.index('h'))

for i in name:
    if i == ' ':
        print()
# to print all indices of a cahracter 
# i is for iterating and value stores that value in string 
for i , value in enumerate(name):
    if value == 'l':
        print(i,end=' ')
print()
# if not want to use enumerate way (un - pythonic way )
for i in range(len(name)):
    if name[i] == 'l':
        print(i," : ",name[i] )
