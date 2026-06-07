'''
arr = [10,90,10]
print(id(arr)) # addrress of that blck which contains size ,
#capacity and pointers referencing to eelements in memory

print(id(10),end=' same as ')
print(id(arr[0]),end=' same as ')
print(id(arr[2]))

# now changing value of arr[0] actually don't change the value at that address
#basically it assigns arr[0] a new adrress in memory pointing to new value
arr[0] = 30 
print(id(30),end=' same as ')
print(id(arr[0]))
print(id(arr[2]))
'''
        # now lists that are mutable

lst = [[1,2],[1,2],[1,2]]
print('lists inside parent list : ')
print(id(lst[0]) , id(lst[1]) , id(lst[2]) ,sep= " not  same as ")
print('Addrress of 1 in all lists inside lst : ')
print(id(lst[0][0]) , id(lst[1][0]) , id(lst[2][0]),sep=' same as ')

