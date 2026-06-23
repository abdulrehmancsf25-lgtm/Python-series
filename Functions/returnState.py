# WITHOUT RETURN STATEMENT 
# defaul return statement is None 
def is_odd(num):
  if num & 1:
    print('odd')
  else:
    print('even')
print(is_odd(5))

# function call stack in global frame(HOUSE) and function calls(Temporary rooms in house )
def printing(num):
  if num == 0:
    return 
  printing(num-1)
  print(num)
printing(5)