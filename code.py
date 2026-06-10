
n = 11
# for i in range(n):
#     for j in range(n):
#
#         if j+1<n-i:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()
#    *
#    **
#   ***
#  ****
# *****
# for i in range(n):
#     for j in range(n):
#         if j+1<=n-i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# *****
# ****
# ***
# **
# *

if n > 0:
    for i in range(n):
        c = 1
        for j in range(n):
            if j < i:
                print(" ", end="")
            else:
                x = len(str(i)) - 1
                if i + 1 > 10:
                    print(" " * x, end="")
                print(f"{c}", end="")

            print(",", end="")

            c += 1
        print()
else:
    print("Invalid Input")