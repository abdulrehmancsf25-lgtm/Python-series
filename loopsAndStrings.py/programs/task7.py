# Code here
str1 = ""
arr =[]
for i in range(1,5):
  str1 = ""
  str1 += str(i)
  for j in range(1,5):
    if j != i:
      str1 += str(j)
      for k in range(1,5):
        if k != i and k != j:
          str1 += str(k)
          for l in range(1,5):
            if l != i and l != k and l != j:
              str1 += str(l)
              if len(str1) == 4:
               arr.append(str1)
               new = str1[:-1]
               str1 = new
          new = str1[:-1]
          str1 = new
      new = str1[:-1]
      str1 = new

print(arr)
