def l(x):
    minval = 0
    for i in x:


        if i>minval:
            minval=i
        yield minval

k = [1,7,6,5,8,12,11]
a = l(k)
for i in range(len(k)):
    print(next(a),end=" ")