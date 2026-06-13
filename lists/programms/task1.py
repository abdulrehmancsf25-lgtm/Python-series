# Q : print prime numbers between 2 and given input x with list comprehension Also
import  math
x = int(input('enter upper limit '))
for i in range(2,x+1):
    for j in range(2,int(math.sqrt(i)) +1):
        if i % j == 0 :
            break
    else:
        print(i,end=' ')

print()
arr = [i for i in range(2,x+1) if all(i % j != 0 for j in range(2,int(math.sqrt(i)) + 1))]
print(*arr ,sep=' ')