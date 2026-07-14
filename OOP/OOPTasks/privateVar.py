class ATM:
    def __init__(self):
        self.__pin = 1234

A1 = ATM()
#print(A1.__pin) # not works
print(A1._ATM__pin) # exceptio case
# but if a varibale is private means we don't have to touch it 

