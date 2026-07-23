# f = open("File Handling/FirstTextFile.txt" , 'r')
# s = f.read() # read use to read whole file by default 
# print(s)
# f.close

# for specific characters

# s = open("File Handling/FirstTextFile.txt" , 'r')
# print(s.read(20)) # first 20 characters including \n
# s.close()


# for reading line by line 
op = open("File Handling/FirstTextFile.txt" , 'r')
l1 = op.readline()
print(l1.strip()) 
#  use strip to remove \n and extra spaces at start and end 
# use rstrip for only right side 
l2 = op.readline()
print(l2 , end='')

# a wat to find , replace and delete multiple chars
# instead of replace func() for only 1 word 
text = "A, B! A? B."

# Slot 1: Replace 'A' and 'B'
# Slot 2: With '1' and '2'
# Slot 3: Delete ',!?. '
rule = str.maketrans('AB', '12', ',!?. ')

print(text.translate(rule))
# output : 1212



my_text = '    I am ,a ,data scientist!?'
rule = str.maketrans('' , '' , '!?,')
print(my_text.translate(rule).strip())