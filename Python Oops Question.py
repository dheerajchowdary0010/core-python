# # q1
# class Animal:
#     def sound(self):
#         print("test")
# class Dog(Animal):
#     def sound(self):
#         print("bow")
# class Cat(Animal):
#     def sound(self):
#         print("mew mew")
# class Cow(Animal):
#     def sound(self):
#         print("moo")
# def f(a):
#     a.sound()
# d = Dog()
# c = Cat()
# co = Cow()
# l = [d,c,co]
# for i in l:
#     f(i)
#
# # q2
# def operate(device):
#     device.start()
# class Car:
#     def start(self):
#         print("vroom")
# class Computer:
#     def start(self):
#         print("beep")
# class WashingMachine:
#     def start(self):
#         print("wii")
# c = Car()
# C = Computer()
# W = WashingMachine()
# l = [c,C,W]
# for i in l:
#     operate(i)
# #
# # q3
# class Vector:
#     def __init__(self,x,y):
#         self.x= x
#         self.y=y
#     def __add__(self, other):
#         return self.x+other.x,self.y+other.y
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
# v1 = Vector(1,2)
# v2 = Vector(2,2)
# v3=  Vector(1,2)
# print(v1+v2)
# print(v2==v3)
#
# # q4
# class Transport:
#     def move(self):
#
#         print("started")
# class Bus(Transport):
#     def move(self):
#         print("bus")
#         super().move()
# class Bike(Transport):
#     def move(self):
#         print("bike")
#         super().move()
#
# b = Bike()
# bu= Bus()
# b.move()
# bu.move()

# test
# class person:
#     def __init__(self,n):
#         self.name = n
#     def p(self):
#         print(f"name {self.name},{self.roll}")
# class student(person):
#     def __init__(self,rol,n):
#         super().__init__(n)
#         self.roll = rol
#     def p(self):
#         super().p()
#         print("student")
# s = student(22,"nan")
# s.p()

# q5
# class Payment:
#     def process(self,a):
#         return f"amount {a}"
#
# class CreditCardPayment(Payment):
#     def process(self,a,card_type):
#         return f"amount {a} ,card {card_type}"
# p = Payment()
# c = CreditCardPayment()
# print(p.process(1))
# print(c.process(1,"visa"))

# q6
