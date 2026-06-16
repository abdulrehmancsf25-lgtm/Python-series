k = set({})
k.add(1)
print(k)
s = {1,2,3,4,5,5} # 5 only comes 1 time in s
print(s)
s.discard(5)
print(s)
s = {}
print(type(s))
s = {1,2,4}
s.pop()
print(s)

s = (1,2)
t = (3,4)
e = s + t
print(e)
 
x = {i if i&1 else 'hello' for i in range(1,11)}
print(x)