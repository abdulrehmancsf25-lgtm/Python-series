'''
arr = [6,7,8,9]
for i in range(0,len(arr)) :
    print(arr[i], end=' ')
print()
# patter
for i in range(1,4) :
    print('*'*i)
#printing even index values
arr = [9,8,7,6,5,4]
for i in  range(0,len(arr)) :
    if i & 1 == 0 :
        print(arr[i] , end=' ')
print()
    
rows = 4
# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for printing stars in that row
    for j in range(i):
        print('*', end='')
    
    # Move to the next line after finishing the row
    print()

# pattern

rows = 4
for i in range(rows):
    for j in range(i):
        print(' ',end='')
    for k in range(rows - i):
        print('*',end='')
    print()    
    '''
for i in range(1,4):
    num = 3
    for j in range(1,i+1):
       print(num,end='')
       num -=  1 
    print()