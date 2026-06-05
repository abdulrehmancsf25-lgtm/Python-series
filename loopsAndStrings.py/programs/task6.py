'''
str1 = input('enter string to count number of words ').strip()
count = 1
for i in str1:
    if i == ' ':
        count += 1
print('total words are : ',count)
'''
str1 = input('enter the string to cionvert into titlecase without tite function : ')
arr = str1.split()
# for i in arr or any thing pyrthon creates copy not original element
for i in range(len(arr)):
    s = arr[i]
    arr[i]= s[0].upper() + s[1:]
    

print(" ".join(arr))