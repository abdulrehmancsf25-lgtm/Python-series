# FlexibleDict
# As of now we are accessing values from dictionary with exact keys. 
# Now we want to amend accessing values functionality.
#  if a dict have key 1 (int) the even if we try to access values by giving '1' (1 as str) as key,
#  we should get the same result and vice versa.
# Write a class FlexibleDict upon builtin dict class with above required functionality.
# Example :
'''d = FlexibleDict()
fd['a'] = 100
print(fd['a']) # Like regular dict

fd[5] = 500
print(fd[5]) # Like regular dict

fd[1] = 100
print(fd['1']) # actual Key is int but still trying to access through str key.
fd['1'] = 100
print(fd[1])'''

class flexible_dict(dict):
    # changing the getting value with key 
    def __getitem__(self, key):
        if(type(key) == str and key.isdigit()):
         return super().__getitem__(int(key))
        else:
           return super().__getitem__(key)
    
    def __setitem__(self, key, value):
       if(type(key) == str and key.isdigit()):
         return super().__setitem__(int(key), value)
       else:
          return super().__setitem__(key, value)
          

myDic_1 = flexible_dict()
myDic_1[1] = "hi"
myDic_1['1'] = "hey"

print(myDic_1)

myDic_1['2'] = 'I'
myDic_1[3] = 'am a'
myDic_1['4'] = 'programmer'

print(myDic_1[4])
