'''Q : merge two lists without + operation 
user_input = input('Enter the list items separated by space :')
lst = user_input.split()
print(lst)
first = [1,2,3,4,5]
second = [6,7,8,9]
first.extend(second)
print(first)
'''

'''Q : Replace an item with other item 
e.g.
arr = [1,3,2,4,5,6,3]
Replace 3 with 300'''

arr = [1,2,3,5,3,5,6]

x = [300 if i == 3 else i for i in arr]
print(x)

for i in range(len(arr)):
    if arr[i] == 3:
        arr[i] = 300 
print(arr)

arr = [1,3,2,5,7,3,6]
while 3 in arr:
    index = arr.index(3)
    arr[index] = 300
print(arr)
