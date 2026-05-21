from typing import List


class Product:
    total_products = 0
    newlist = []
    def __init__(self,n,cat,p,q):
        if Product.is_valid_price(p):
            self.name=n
            self.category=cat
            self.price = p
            self.quantity=q

            Product.total_products +=1

        else:
            return None
    @classmethod
    def createobj(cls, product_str):
        a = product_str.split('-')
        Product.newlist.append(a)
        print(Product.newlist)
        return cls(a[0],a[1],a[2],a[3])


    @staticmethod
    def is_valid_price(p):
        return int(p)>0
# name-category-price-quantity
obj0 = Product.createobj("soap-basic-1000-11")
obj1 = Product.createobj("shampoo-basic-100-10")
obj2 = Product.createobj("soap-basic-100-11")
# print(obj1)
allproduct = Product.newlist
# print(allproduct,"all")
def fil(x):
    # print(int(x[-1]))
    return int(x[-1])>10
x = list(filter(fil,allproduct))
print(x,"filtered")
tosort = sorted(allproduct,key=lambda x:int(x[2]))
print(tosort)