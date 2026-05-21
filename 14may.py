# <,>,<=,>=
class A:
    def __init__(self,x,y):
        self.x = x
        self.y =y
    def __add__(self, other):
        return  A(self.x+other.y,self.y+other.y)
    def __sub__(self, other):
        return  A(self.x-other.y,self.y-other.y)
    def tot(self):
        return ((self.x**2)+(self.y**2))**0.5
    def __lt__(self, other):
        return self.tot()<other.tot()

    def __gt__(self, other):


        return self.tot()>other.tot()
    def __ge__(self, other):
        x = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        y = (other.x ** 2 + other.y ** 2) ** 0.5
        return x >= y
    def __le__(self, other):
        x = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        y = (other.x ** 2 + other.y ** 2) ** 0.5
        return x <= y
    def __eq__(self, other):
        x = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        y = (other.x ** 2 + other.y ** 2) ** 0.5
        return x == y
    def __str__(self):
        print(f"{self.x} and {self.y}")
        return f"{self.tot()} "

a1= A(20,20)
a2=A(40,40)
a3 = A(50,50)
a4 = A(50,50)
print(a1)
print(a1+a2+a3)
print(a1<a2)
print(a3>=a1)
print(a3==a4)