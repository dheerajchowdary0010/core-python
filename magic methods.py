class A:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f"a:{self.a},b:{self.b},c:{self.c}"
    def __add__(self, other):

        if isinstance(other,int):
            return self.b+other
        elif isinstance(other,str):
            return self.a+other
        elif isinstance(other,A):
            return self.c+other.c
        else:
            return "error"

a = A("hi",20,20)
a2 = A("hi",20,20)

print(a)
print(a+" hello")
print(a+75)
print(a+a2)
