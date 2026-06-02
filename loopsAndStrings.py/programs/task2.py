'''
arr = ['a','b','c']
arr2 = ['d','e','f']
arr += arr2
print(arr)
arr = [1,2,3]
arr2= [4,5,6]
print(arr+arr2)
str1 = 'thi'
print(str1.isupper())
'''
str1 = 'Abdul Rehman Arshad'
result = "".join(sorted(str1,key=str.lower)) # use str. not str1 in key
print(result)