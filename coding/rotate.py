def isprime(x):

    if x ==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
x = int(input())
n = len(str(x))
a = str(x)
rotate = a+a
i = 0
while i+n<len(rotate):
    j = n+i
    r = rotate[i:j]

    i+=1
    if isprime(int(r)):
        print(r)

