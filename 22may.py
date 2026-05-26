from symtable import Class


class A:
    @classmethod
    def m1(cls):
        print("a class")

class B(A):
    @classmethod
    def m1(cls):
        super().m1()
        print("b class")

class C(B):
    @classmethod
    def m1(cls):
        print("c class")
        super().m1()

# print(C.mro())
# c1 = C()
# c1.m1()
class Person:
    def __init__(self,name):
        self.name =name
class Student(Person):
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        super().__init__("a")

s = Student("jjbf",12)
print(s.name)
print(s.roll)