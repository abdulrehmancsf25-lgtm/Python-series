# with open('bigFile.txt' , 'w') as f:
#     for i in range(1,1001):
#         f.write(f"Line {i}: This is a sample text used for file handling practice. ")
#         f.write("It helps test how your code handles reading large amounts of data.\n")
#     print(f"Success! '{'bigFile.txt'}' generated with {1000} lines.")

  # FILE IS CREATED

# real use of with (use it to load a small chunk of data at a time in memory buffer ,
# so that whole file should not load at a time in memory(10 gb file an easily be read in 8 gb storage by this)

# with open("File Handling/bigFile.txt" , 'r') as f:
#     chunk_number = 1
#     while True:
#         chunk = f.read(100)
#         if len(chunk):
#             # Using end='' prevents print from adding an extra blank line
#             print(f"--- CHUNK {chunk_number} ---")
#             print(chunk) 
#             chunk_number += 1
            
#             # Stop after 5 chunks so you can see the beginning
#             if chunk_number > 5:
#                 break
#         else:
#             break 


# Alternative: Reading 100 lines at a time
with open("File Handling/bigFile.txt", 'r') as rf:
    while True:
        # Read the next 100 lines
        lines = [next(rf, None) for _ in range(100)]
        
        # If the first item is None, the file is empty
        if lines[0] is None:
            break
            
        # Filter out None values at the end of the file
        lines = [line for line in lines if line is not None]
        
        for line in lines:
            print(line, end='')
        user = input("E for exit and C for continue : ")
        if(user.lower() == 'e'):
            break 