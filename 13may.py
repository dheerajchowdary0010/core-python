from select import select


class Product:
    def __init__(self,n,p,q):
        self.name = n
        self.price = p
        self.quantity= q
    def __str__(self):
        return f"name:{self.name},product:{self.price},quantatity:{self.quantity}"
class cart:

    def __init__(self):
        self.product= []

    def totalof(self):
        s= 0
        for i in self.product:
            s+=i.price*i.quantity
        return s

    def __str__(self):
        for i in self.product:
            print(i)
        print(self.totalof())
        return "end"
        # reduce(lambda x, y: x + y(y.price * y.quantity), self.l, 0)
    def __add__(self, other):
        if isinstance(other,Product):
            self.product.append(other)
        return f"added {other} "
    def __sub__(self, other):
        if isinstance(other, Product):
            if other in self.product:
                self.product.remove(other)
        return f"added {other} in {self.cart}"
p1= Product("a",10,1)
c1 = cart()
c2=c1+p1
# print(p1)
print(c1)