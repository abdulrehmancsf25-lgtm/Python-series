arr = [1,2,3,4,5,[6,7]]
#  positive indexing
print(arr[5]) # ouput [6,7]
print(arr[5][1]) # output 7
# negative indexing
print(arr[-1][0]) # output 6
print(arr[-1][::-1]) # reverse of [6,7]
print(arr[-1][-2])
print()
print('slicing')
# slicing
print(arr[:5]) # output[1,2,3,4,5]
print(arr[-2:])
print(arr[-4::1]) # output [3,4,5,[5,6]]
print(arr[5:][0:]) # output [[6,7]] first 5: starts from index 5 onwards in list arr
# then create a list [] containing that item [5,6] then 0: starts from inde 0 of this list print first item [5,6]
print(arr[5:][1:]) # output[]