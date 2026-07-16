# The Ambiguity: The "Diamond Problem"
#    A
#   / \
# B    C
#  \ /
#   D
#Python resolves this ambiguity using a strict,
#  predictable algorithm called Method Resolution Order (MRO)
# MRO creates a linear list of classes that Python will search through, 
# one by one, when looking for a method or attribute.

#Children before parents:
#                        A child class is always checked before its parent classes.

#Left-to-right: 
#             If a class inherits from multiple parents, Python checks them in the order they are listed in the parentheses. (e.g., in class D(B, C):, B is checked before C).

#Because D inherits (B, C) in that exact order, the MRO for D is:
# D -> B -> C -> A 

# Checking MRO 
                #print(D.__mro__)
# Output:
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# USE super(). if want to execute all parent methods
#super() does not just mean "call the parent." 
# It actually means "call the next class in the MRO."

class A:
    def process(self):
        print("Processing in A")

class B(A):
    def process(self):
        print("Processing in B")
        super().process() # Calls C, NOT A!

class C(A):
    def process(self):
        print("Processing in C")
        super().process() # Calls A

class D(B, C):
    def process(self):
        print("Processing in D")
        super().process() # Calls B

obj = D()
obj.process()
