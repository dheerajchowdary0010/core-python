def ispalindrome(x):
    s=0
    y=x
    while x!=0:
        r = x%10
        s=s*10+r
        x=x//10
    return y==s
a = int(input("enter num"))
b =0
while b<a:
    if ispalindrome(b):
        print(b,end=" ")
    b+=1