def checker(fun):
    def inner(a,b):
        x = fun(a,b)
        if x<0:
            return 0
        else:
            return x
    return inner
@checker
def sub(a,b):
    return a-b

print(sub(3,2))
print(sub(4,5))