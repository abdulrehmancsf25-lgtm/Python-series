'''
Q : Combine two lists index-wise(columns wise)
Write a program to add two lists index-wise.
Create a new list that contains the 0th index item from both the list, then the 1st index item,
and so on till the last element. any leftover items will get added at the end of the new list.

Given List:
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

Output:
[['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]
'''
list1 = ["M", "na", "i", "Kh","hi","i","am"]
list2 = ["y", "me", "s", "an"]
'''
#x = [[i+j for i,j in zip(list1,list2)] for i in range(length)]
result = []
x= []
for i in range(len(list1)):
  x.extend([list1[i],list2[i]])
  result.append(x)
  x = []
print(result)
'''
x = [[i,j] for i,j in zip(list1,list2)]
if len(list1) > len(list2):
  index = len(list2)
  for i in list1[index:]:
    x +=[[i]]
elif(len(list2) > len(list1)):
  index =len(list1)
  for i in list2[index:]:
    x += [[i]]

print(x)
