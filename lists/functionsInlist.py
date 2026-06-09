'''
arr= [3,2,4,5,1]
# sorted(x) does not change original list creates a copy 
print(sorted(arr))
print(arr)
# .sort() permanantly changes the list
arr.sort(reverse=True)
print(arr)
'''
# reversed function does not  change original  list
Q =[1,2,3,4,5]
O =reversed(Q) #RETURNS INDEXEX ONLY OR PRINT IMMEDIATELY TO GET TEMPORARY LIST
print(list(O))
  # alternate
O = Q[::-1]
print(O)

arr = [1,2,3,4]
arr.reverse()
print(arr)

# copy function used to copy list into another with different  memory addresses
print('copy function ')
arr = [1,2,3,4]
print(id(arr))
arr2 = arr.copy()
print(id(arr2))
arr2.append(3)
print(arr)
print(arr2)

import copy
arr3 = copy.copy(arr) # shallow copy in case of 2D it copies only outer items separately
# for inner items the references are same for both lists 
arr3 = copy.deepcopy(arr) # deep copy --> every single outer & inner item is stored separately in mempry
print(id(arr3))