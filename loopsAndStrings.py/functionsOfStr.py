# Common functions of datatypes
'''
len
max
min
sorted
'''
sr = 'Apple banana'
print(max(sr)) # max & min on the basis of ASCII value 
print(min(sr))
print(len(sr))
print(sorted(sr)) # returns a list 

            # OTHER USEFUL ONLY STRING BASED FUNCTIONS
# strip function
sr = '     my name is coder                  '
print(sr.strip(),'ho') # strip remove trailing(very first & very last) spaces in string
# replace
print(sr.replace('i', 'is'))

#split
print(sr.split('is')) # returns list
arr = sr.split() # splits string where is comes
print(arr)
#join        joins list into string with an empty or other string snippet provided
sp = " ".join(arr)
print(sp)
sp = "--".join(arr)  # joins list elements with --
print(sp)