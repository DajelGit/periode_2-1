
"""

# opgave 1
### A
class A:
    def __init__(self, i = 0):
        self.i = i
    
    def m1(self):
        self.i += 1

class B(A):
    def __init__(self, j = 0):
        super().__init__(3)
        self.j = j
    
    def m1(self):
        self.i += 1
    
def main():
    b = B()             # b.i = 3  b.j = 0
    print(b.i, b.j)     #  3 0
    b.m1()              # b.i = 4  b.j = 0
    print(b.i, b.j)     #  4 0

main()



### B
class A:
    def __init__(self, i):
        self.i = i
    
    def __str__(self):
        return "I am class A"

class B(A):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
    
    def __str__(self):
        return "I am class B"


def main():
    a = A(1)            # a.i = 3
    b = B(1, 2)         # b.i = 1   b.j = 2
    print(a)            # "I am class A"
    print(b)            # "I am class B"
    print(a.i)          # 3
    print(b.i, b.j)     # 1 2

main()


# opgave 2
#  NEE


"""

# opgave 3
class Circle():
    PI = 3.14159265358979

    def __init__(self, straal):
        self.straal = straal
    
    def area(self, persision = 2):
        return round(self.straal * self.straal * self.PI, persision)    
    
    def perimeter(self, persision = 2):
        return round(self.straal * 2 * self.PI, persision)


c = Circle(8)
print(c.area())
# assert c.area() == 200.96
# assert c.perimeter() == 50.24
# assert c.perimeter() == 50.24