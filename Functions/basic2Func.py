def is_even(num):
  """
  This function returns if a given number is odd or even
  input - any valid integer in int ,string or float datatype 
  output - odd/even
  """
  return 'Even' if num % 2 == 0 else  'False'
# printing documentation 
print(is_even.__doc__)
print(is_even(8))

# *args & **kwargs
def sum_of_product_stock(*args):
  ans =  0
  for i in args:
    ans += i
  return ans 
stock_list =  [1,2,3,4,5]
sum_of_product_stock(*stock_list)

#**kwargs
def display_stock(**stock):
  for i in stock.keys():
    print(i)
  for j in stock.values():
    print(j)
  for (i,j) in stock.items():
    print(i,j)
#  simple -->  display_stock(mouse = 3 , keyboards = 4 ,CPU = 0 , Data_cables =1)
#   OR 
item_stock_list = dict(mouse = 3 , keyboards = 4 ,CPU = 0 , Data_cables =1)
display_stock(**item_stock_list)