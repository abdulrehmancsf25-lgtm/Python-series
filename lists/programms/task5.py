'''Q: remove dupliates from list'''
arr = [1,2,1,3,2,3,2,1,2]
arr.sort()
if len(arr) == 0:
    x =[]
else:
  x = [arr[0]]
  for i in arr[1:]:
    if i != x[-1]:
        x.append(i)
print(x)

'''Q : check a given list is in ascending order  or not'''
arr = [1,2,3,5,3,6,8,6,1,1]
if arr == sorted(arr):
   print(True)
else:
   print(False)
# OR New method 
arr = [1,3,4,5,7]
x = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
print(x)