class aclaaa:
    def __init__(self):
        self.a = 10
    def m1(self):
        print("afa")

class acl(aclaaa):
    def m1(self):
        print("afa")
class ac(aclaaa):
    def m1(self):
        print("afa")
class b(acl,ac):
    def __init__(self):
        self.b1 = 20

    def m1(self):
        print("add")

b1 = b()
print(b.mro())
