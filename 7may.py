# class bank:
#     def __init__(self,id,name,pin,bankbalance):
#         self.id = int(id)
#         self.name= name
#         self.pin = pin
#         self.balance = int(bankbalance)
#
#     def deposite(self,amount):
#         if amount<0:
#             print("invalid input")
#             return "invalid input"
#         self.balance +=amount
#
#     def __setattr__(self, key, value):
#         if key =="balance":
#             if value<0:
#                 print("Invalid input 1")
#                 return "Invalid input"
#         return super().__setattr__(key,value)
#
#     def __getattribute__(self, item):
#         if item == "balance":
#             x= input("enter pin")
#             actual_pin = super().__getattribute__('pin')
#             if x != actual_pin:
#                 return "invalid pin"
#         return super().__getattribute__(item)
# obj = bank(11,"hdfc",123,100)
# # x=bank(11,"hdfc",123,-100)
# # obj.deposite(-1000)
# print(obj.balance)

class a:
    def __init__(self,a):
        self.a = a
        self.b = 0
    @property
    def __iter__(self):
        x= int(input("enter 1 for prime or 0 for composite"))
        self.x = x%2
        return self
    def isprime(self,x):
        if x==1:
            return False
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        return True

    def __next__(self):
        while True:
            self.b+=1
            if self.b<self.a:
                if self.isprime(self.b) == self.x:
                    return self.b
            else:
                raise StopIteration

ob = a(20)
for i in ob:
    print(i,end=" ")

