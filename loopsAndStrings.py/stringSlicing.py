# SLICING (MORE THAN ONE CHARCATERS )
'''
name  = 'hello world'

print(name[0:5]) # index 0 to 4 will print out 
print(name[:3]) # print till index 2
print(name[3:]) # print from index 3 to last 
print(name[:]) # full string 
print(name[::3]) # print index from 0 with jump 3
print(name[0:5:2])#index 0 top 4 with jump 2
'''
s = 'radar'
print('length of string s : ',len(s))
print(s[:])
print(s[-1:-6:-1]) # index -1 to -5 all elements in reverse with -1 increase
s = 'balo'
print(s[:-2]) # index 0  to 1 excluding -1 & -2 indexes from right but print from left--> right
print(s[-1:-2:-1])
print(s[-1::-2])
s = 'radar'
if s == s[::-1]:
    print('palindrome')  
  # OR 
if s[:] == s[::-1]:
    print('palindrome ')
               # CONVERTING TO UPPER OR LOWER CASE & first letter upper case
    s= 'abdul'
    ustring = s.capitalize()
    print(ustring)
    ustring = s.upper()
    print(ustring)
    s = ustring.lower()
    print(s)
                  # to cpitalize  FIRST WORD OF EVERY WORD 
sr = 'abdul rehman'
sr += ' arshad'
print(sr.title())

# delete a string 
del sr
# print(sr) will trough an error as it is deleted 
