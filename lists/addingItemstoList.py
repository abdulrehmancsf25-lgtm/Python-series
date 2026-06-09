arr = [1,2,3,4,5,True]
# append adds one item at last of list
arr.append(6)
print(arr)
arr.append([7,8]) # append [7,8] as a single item
print(arr)
print(arr[7])

# extend adds list to parent list means multiple items together not make 2D
arr = [1,2,3]
arr.extend([4,5])
arr.extend('Hello') # adds  ['H','e','l','l','o'] in arr
print(arr)

# insert adds items at your desired index
arr = [1,2,3,4,5]
arr.insert(1,True) # [1,True,2,3,4,5]
print(arr)

                        # imp concept
# insert adds only 1 item at a time so to add multiple items at your desired index
arr = [1,2,3,4,5]
arr = arr[:2] + [100,101]+arr[2:]
print(arr)

array = [1,2,3,4,5]
array[1:1]= [101,102]
print(array)
array[1:1] = [23]
print(array)

arr = [1,2,3]
print(arr.extend([4,5])) # output None because it returns None which shows it modifies original array