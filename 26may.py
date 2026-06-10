# class a:
#     def __init__(self,a,b):
#         self._a = a
#         self.__b = b
#
# a1 = a(10,20)
# print(a1._a)
# # print(a1.__b)
# print(a1._a__b)

class Bank:
    __a = 10
    def __init__(self,a:int,b:int,pin:int,name):
        self.__balance= b
        self.accno= a
        self._pin = pin
        self._name = name
    def withdraw(self,a,pin):
        if self._pin==pin:
            if self.__balance<a:
                return "amount exceeds the balance"
            else:
                self.__balance -= a
                return f"remaining amount {self.__balance}"
        else:
            return f"incorrect pin"
    def display(self):
        i = int(input("enter pin"))
        if self._pin==i:
            return f"name:{self._name} ,balance: {self.__balance},acc:{self.accno}"
        else:
            return "incorrect pin"
    def deposite(self,a):
        if a<0:
            return f"amount cannot be less than 0"
        else:
            self.__balance +=a
            return f"added balance {self.__balance}"
    @property
    def get_a(self):
        return self.__a
    @get_a.setter
    def get_a(self,a):
        self.__a = a
b1 = Bank(111,100,123,"jb")
print(b1.deposite(1000))
print(b1.withdraw(300,123))
print(b1.get_a)
b1.get_a = 30
print(b1.get_a)
# print(b1.display())