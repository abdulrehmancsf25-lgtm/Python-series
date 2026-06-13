'''
arr = [1,2,3,4,5]
# del Function
del arr
# print(L) will give an error as arr is deleted
           # Deleting specific part of list
arr = [1,2,3,4,5]
del arr[4]
print(arr)
arr.append(5)

del arr[4:]
del arr[-4]
print(arr)
'''
# remove function deletes item  without taking index 
arr = [1,2,3,4,3,5]
arr.remove(3) # item must exist in list before removing
print(arr)
'''
# pop function takes index but by default index in it is -1
arr = [1,2,3,4,5]
arr.pop()
print(arr)
arr.pop(0)
print(arr)

# clear functions clears the list --> make it empty
arr = [1,2,3]
arr.clear()
print(arr)
'''
