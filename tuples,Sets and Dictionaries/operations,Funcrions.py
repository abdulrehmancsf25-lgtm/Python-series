d0 = {'name':'Abdul','university':'PUCIT','age':19}
# membership operator
print('age'in d0) # --> Key
print('Abdul' in d0) # --> Not key
print()
# loop
for i in d0:
    print(i,d0[i])

# Functions 
d1 = dict(sorted(d0.items()))
print(d1)
print(sorted(d0))
