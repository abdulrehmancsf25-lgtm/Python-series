arr =[1,2,3,4,5,6]
size = len(arr)
target = int(input('Enter the target to search for '))
s = 0 
e = size -1 
mid = s + (e-s)//2 
while s <= e :
  if arr[mid] == target :
      print('target found at index : ' , mid )
      break 
  elif arr[mid] > target :
      e = mid -1 
  else :
       s = mid +1 
  mid = s + (e-s)//2
    
else :
    print('not found ')