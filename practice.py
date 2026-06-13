arr = [1,2,3,4,5,6] 
for i in range(0,len(arr)) :
    print(arr[i], end=' ')
arr.append(7)
print(arr[6])

temp = ['a','b','c']
for i in  range(0,len(temp)) :
    print(temp[i],end=',')
print()
#to avoid , after last element
print(*temp,sep='-')
print(temp)

# for adding more items together in list 
arr = [1,2,3]
temp = [4,5]
arr.extend(temp)
for i in range(0,len(arr)):
    if(i < len(arr) -1):
      print(arr[i],end=',')
    else :
        print(arr[i])

# string list 
x = ['oranges','mangos']
print(*x, sep='-')
x.extend(['bananas','strawberies'])
print(*x,sep='-')
# extracting last element
x.pop()
print(*x,sep='-')

