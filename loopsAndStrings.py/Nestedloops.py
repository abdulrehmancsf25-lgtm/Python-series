# unique pairs 
'''
for i in range(1,5):
    for j in range(1,5):
        print('(',i,j,')' ,end='')
'''
# pattern
'''
*
**
*** 
rows = int(input('enter rows '))
#for i in range(1,rows+1):
#   print('*'*i)

for i in range(1,rows+1):
    for j in range(i):
        print('*',end='')
    print()  
'''

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end='') 
    for k in range(i-1,0,-1):
        print(k,end='') 
    print()