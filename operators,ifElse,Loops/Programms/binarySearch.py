arr =[1,2,3,4,5,6]
size = len(arr)
target = int(input('Enter the target to search for '))
s = 0 
e = size -1 
mid = s + (e-s)//2 
find = False
while s <= e :
  if arr[mid] == target :
      find = True 
      break 
  elif arr[mid] > target :
      e = mid -1 
  else :
       s = mid +1 
  mid = s + (e-s)//2

if find :
    print('target found')
else :
    print('not found ')