arr = [1,2,3,4]
print(arr * 0)
print(arr * -1) # neagtive numbers treated as 0 in this case
print( arr * 2) # --> arr + arr 
print(arr + [5,6,7])

print(arr.index(2))
str1 = 'hello'
print(str1.index('e'))

arr = [1,2,3,[4,5]]
print(4 in arr) # false
print(2 in arr)