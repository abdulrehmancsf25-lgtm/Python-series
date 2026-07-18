
      # writelines func() use iterbale (list , tuple , dictionary )

# t = ("i\n" , "love\n" , "coding\n")
# f = open('File Handling/FirstTextFile.txt' , 'a')
# f.writelines(t)
# f.close()

# lst = ["\nLearning" , "\nPython "]
# f1 = open('File Handling/FirstTextFile.txt' , 'a')
# f1.writelines(lst)
# f1.close()

# st1 = {'\nPython libraries' ,'\nNumpy' , '\nPandas'}
# f2 = open('File Handling/FirstTextFile.txt' , 'a')
# f2.writelines(st1)
# f2.close()

# st1 = {'\nPython libraries':1 ,'\nNumpy':2 , '\nPandas':3}
# f2 = open('File Handling/FirstTextFile.txt' , 'a')
# f2.writelines(st1)
# f2.close()

# for keys and values to write in file
st1 = {'\nPython libraries':1 ,'\nNumpy':2 , '\nPandas':3}

# convert fist it into list of strings 
lst1 = ['{} : {}'.format(key,value) for key,value in st1.items()]
# now pass the list 
f3 = open('File Handling/FirstTextFile.txt' , 'a')
f3.writelines(lst1)
f3.close()
