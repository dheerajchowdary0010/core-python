# q1
class BankAccount:
    def __init__(self,account_number,b):
        self.account_number= account_number
        self.__balance = b
    def deposit(self,n):
        self.__balance+=n
    def withdraw(self,n):

        if self.__balance<n:
            return "minamount exceeds"
        self.__balance-=n
        return f"remaining {self.__balance}"
b = BankAccount(1,12)
print(b.deposit(190))
print(b.withdraw(1000))
print(b.withdraw(90))

# q2

class Student:
    def __init__(self):
        self.__marks = 0
    @property
    def getmarks(self):
        return self.__marks
    @getmarks.setter
    def getmarks(self,n):
        if 0<=n<=100:
            self.__marks=n

            print(f"set marks :{self.__marks}")
        else:
            print("inavlid marks")
s = Student()
s.getmarks = 100
s.getmarks = -100
print(s.getmarks)

#q3
class SecureFile:
    def __init__(self,n,p):
        self.__content=n
        self.__pass = p
        self._Unauthorized_attempt=0
    def read(self,p):
        if self.__pass==p:
            return self.__content
        self.log()
        return "Invalid password"
    def log(self):
        self._Unauthorized_attempt+=1
s = SecureFile("testing",12)
print(s.read(1))
print(s.read(12))
print(s._Unauthorized_attempt)

# q4
class Employee:
    def __init__(self,s):
        self.__salary = s
        self.accessed = 0
    def getsalary(self):
        self.accessedsalary
        return self.__salary
    @property
    def accessedsalary(self):
        self.accessed+=1
    def updatesalary(self,n):
        if n>self.__salary:
            self.__salary= n

        else:
            print("Invalid update")
e = Employee(1000)
print(e.getsalary())
e.updatesalary(100)
print(e.getsalary())
e.updatesalary(10000)
print(e.getsalary())
print(e.accessed)

#q5
class Product:
    def __init__(self,p:int,d:int):
        self.price = p
        self.discount =d
    def __setattr__(self, key, value):
        if key=="price":
            if value<0:
                print("Invalid price")
                return
        elif key=="discount":
            if value>70:
                print("discount exceeded")
                return
        return super().__setattr__(key,value)
    def get_final_price(self):
        return (self.price-(self.price*self.discount)/100)
p = Product(100,10)
print(p.get_final_price())
p1= Product(-1,10)
p2 = Product(100,90)

# q6
class Character:
    def __init__(self,h):
        self._health=h
    def damage(self,p):
        if self._health<p:
            print("health limit exceeds")
        self._health-=p
    def heal(self,p):
        self._health+=p
    @property
    def currhealth(self):
        return self._health
c = Character(10)
c.heal(100)
c.damage(20)
print(c.currhealth)

# q7
class Engine:
    def __init__(self,t):
        self.__temp = t
    def enginetemp(self):
        return self.__temp
    def cool_engine(self,t):
        self.__temp-=t
        print("engine cooled")
class Car(Engine):
    def start_car(self):
        self.car_started= True
        print("car started")

c =Car(12)
print(c.enginetemp())
c.start_car()
c.cool_engine(10)
print(c.enginetemp())

#q8
class ShoppingCart:
    def __init__(self,i):
        self.items=i
    def add(self,i):
        self.items.append(i)
    def remove(self,i):
        if i not in self.items:
            print("No items found")
            return
        self.items.remove(i)
    def safecopy(self):
        from copy import deepcopy
        self.itemscopy = deepcopy(self.items)
l =["a","b","c"]
s = ShoppingCart(l)
s.add("d")
s.safecopy()
s.remove("a")
print(s.items)
print(s.itemscopy)

# q9
class Class:
    def __init__(self):
        self.attendance = []
class Classfix:
    def __init__(self):
        self.__attendance = []
    def attend(self,a):
        self.__attendance.append(a)
    def show(self):
        return self.__attendance
c = Class()
c.attendance.append("a")
c.attendance.append("b")
cfix = Classfix()
cfix.attend("a")
print(c.attendance)
print(cfix.show())

# q10
class test:
    def __init__(self):
        self.__t = 100
    @property
    def show(self):

        return self.__t
    @show.setter
    def show(self,a):
        self.__t=a
t = test()
print(t.show)
t.show=1000
print(t.show)

