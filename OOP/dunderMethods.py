class MYInt:
    def __init__(self , x):
        self.x = x
    def __add__(self, other):
        print(self.x + other)
    # if we call object + 6 it works 
    # for 6 + obj python looks first for __radd__ than go for error
    def __radd__(self, other ):
        print(other + self.x)
    
M1 = MYInt(2)
M1 + 6
6 + M1