# # 5
# from abc import ABC,abstractmethod
# from functools import reduce
#
#
# class payment(ABC):
#     def __init__(self,b):
#         self.__balance = b
#     @abstractmethod
#     def pay(self):
#         pass
#     @abstractmethod
#     def valid(self):
#         pass
#     @property
#     def bal(self):
#         return self.__balance
#     @bal.setter
#     def bal(self,x):
#         self.__balance=x
#
#     def __add__(self, other):
#         return  (self.pay()+other.pay())
#
# class card(payment):
#     def pay(self):
#         x = int(input("enter amount(card) "))
#         if self.valid(x):
#
#             self.bal=self.bal-x
#             return x
#     def valid(self,x):
#         return self.bal-x>=0
# class wallet(payment):
#     def pay(self):
#         x = int(input("enter amount(wallet) "))
#         if self.valid(x):
#             self.bal = self.bal - x
#             return x
#
#     def valid(self, x):
#         return self.bal - x >= 0
# class upi(payment):
#     def pay(self):
#         x = int(input("enter amount(upi) "))
#         if self.valid(x):
#             self.bal = self.bal - x
#             return x
#
#
#     def valid(self, x):
#         return self.bal - x >= 0
#
# c = card(1000)
# w =wallet(500)
# up =upi(100)
#
# def checkout():
#     k = int(input("enter total bill"))
#     op = list(map(int,input("choose options 1:card,2:wallet,3:upi").split()))
#     l=[]
#     for i in op:
#         if i%3 ==1:
#             l.append(c)
#         elif i%3==2:
#             l.append(w)
#         else:
#             l.append(up)
#     from functools import reduce
#     def test(x,y):
#         if isinstance(x,int):
#
#             return x+y.pay()
#         else:
#             return x+y
#     s = reduce(test,l)
#     print(s)
#     if s>k:
#         print(f"here is the change {s-k}")
#     elif s==k:
#         print("done with payment")
#     else:
#         print("insufficent amount")
# checkout()
#
