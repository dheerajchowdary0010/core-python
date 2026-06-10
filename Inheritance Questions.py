#q1
# class Animal:
#     def sound(self):
#         print("test")
# class Dog(Animal):
#     def sound(self):
#         print("bow")

# q2
# class A:
#     def show(self):
#         print("a")
# class B(A):
#     def show(self):
#         print("b")
#         super().show()
#
# b = B()
# b.show()

# q3
# class A:
#     def display(self):
#         print("a")
# class B(A):
#     def display(self):
#         print("b")
# class c(B):
#     def display(self):
#         print("c")
#         super().display()
# c1 = c()
# c1.display()

# q4
# class Vehicle:
#     def wheels(self):
#         print("base")
# class Bike(Vehicle):
#     def wheels(self):
#         print("2 wheels")
# class car(Vehicle):
#     def wheels(self):
#         print("4 wheels")
# b = Bike()
# c = car()

# q5
# class Employee:
#     def salary(self):
#         self.salar= 1000
#
# class Manager(Employee):
#     def salary(self):
#         self.salar = 100000
#         self.incentive = 1000
# e = Employee()
# m = Manager()
# e.salary()
# m.salary()
# print(e.salar)
# print(m.salar,m.incentive)

# # q6
# class University:
#     name = "hello"
#     @classmethod
#     def m(cls,a):
#         cls.name=a
# class College(University):
#     pass
# c = College()
# print(c.name)
# c.m("ad")
# print(c.name)

# # q7
# class MathOps:
#     @staticmethod
#     def add(a,b):
#         return a+b
# class AdvancedOps(MathOps):
#     pass
# a = AdvancedOps
# print(a.add(1,2))

# # q8
# class Father:
#     def skills(self):
#         print("faher")
# class Mother:
#     def skills(self):
#         print("mother")
# class Child(Father,Mother):
#     pass
# c = Child()
# print(Child.mro())
# c.skills()
# super(Father,c).skills()

# q9
# class Person:
#     def __init__(self,n):
#         self.name = n
# class Student(Person):
#     def __init__(self,n,ro):
#         self.name = n
#         self.roll = ro
#     def __str__(self):
#         return  f"name:{self.name},roll:{self.roll}"
# s = Student("test",12)
# print(s)


