#  [expression for item in iterable if condition == True]
"""
#  Q: print 1 to 10
#  print(list(i for i in range(1,11))) # i for i in so on --- provides iterator 
x =[i for i in range(1,11)]
print(x)

# Q print numbers between 1 & 50 which are even
x = [i for i in range(1,51) if not(i&1)]
print(x)

# Q print languages in given list which starts with p
languages = ['java','python','c++','php']
 # x = [lan for lan in languages if lan[0] == 'p']  OR 
x = [lan for lan in  languages if lan.startswith('p') ]
print(*x ,sep='-')

# nested (2D result)
'''1,2,3
   4,5,6
   7,8,9 '''
x = [[i*3 +j +1 for j in range(3)] for i in range(3)] # inner [] for inner loop
print(x)

numbers = [10,11,12,13,14,15,16]
x = [i for i in numbers if not(i&1)]
print(x)
"""
# mark students' grades as 'A' for >=85 ,'A-' for >= 80 and 'B' for >=75 ,>=50 pass else fail
names = ['ali','hamza','ayesha','nomaan','hashir','uzma','kamran']
marks = [87,76,82,50,35,40,93]
grades = ["A" if score >= 85 else "A-" if score >= 80 else  "B" if score >= 75 else
         "pass" if score >= 50  else "fail"  for score in marks]
res = [" ".join([i,str(j),k]) for i,j,k in zip(names,marks,grades) ]
# Print header with alignment (<- left aligned, >- right aligned)
print(f"{'Names':<10} {'Marks':<8} {'Grades':<6}")
print("-" * 26) # Separator line

# Print rows neatly aligned
for name, mark, grade in zip(names, marks, grades):
    print(f"{name.title():<10} {mark:<8} {grade:<6}")