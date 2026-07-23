#  # MOdern way -> use := Walrus operator(assigns and check condition at same line)


# with open('File Handling/FirstTextFile.txt', 'r') as f:
#     # This reads the line, assigns it to 'line', and loops as long as 'line' is not empty
#     while line := f.readline():
#         print(line.rstrip())


with open ('File Handling/FirstTextFile.txt' , 'r') as f:
  for line  in f:
    print(line.rstrip())

                   # V.V.V.V.V.IMP
# we cannot simply use 

# while f.readline() != '':
#print('f.readline()')

# because every time .readline() executes cursir moves to next line
 # so we will skip 1,3,5 so on odd lines
# and print only 1 line after 1st one by sequence 