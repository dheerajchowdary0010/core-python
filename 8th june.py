# # # class circle:
# # #     def __init__(self,r):
# # #         self.shape = "circle"
# # #         self.radius =r
# # #
# # #
# # # class shape:
# # #
# # #
# # #
# # #     def area(self,s):
# # #         if s.shape == "circle":
# # #             return s.radius**2*3.14
# # #
# # #
# # #
# # # c = circle(4)
# # # s = shape()
# # # print(s.area(c))
# #
# #
# #
# # class rectangle:
# #     def __init__(self,l,b):
# #         self.length = l
# #         self.breadth = b
# # class square:
# #     def __init__(self,s):
# #         self.side = s
# # class traingle:
# #     def __init__(self,l,b):
# #         self.length = l
# #         self.breadth = b
# # class Circle:
# #     def __init__(self,r):
# #         self.radius = r
# # class Shapes:
# #     def areaof(self,s):
# #         if isinstance(s,Circle):
# #             return f"area of circle {s.radius ** 2 * 3.14}"
# #         elif isinstance(s,rectangle):
# #             return f"area of rectangle{s.breadth*s.length}"
# #         elif isinstance(s,square):
# #             return f"area of square {s.side**2}"
# #         elif isinstance(s,traingle):
# #             return f"area of traingle{(s.length*s.breadth)*1/2}"
# #         return
# # s = Shapes()
# # c=Circle(4)
# # sq = square(4)
# # r = rectangle(4,5)
# # tr = traingle(4,4)
# # print(s.areaof(c))
vo = "aeiou"
l = ["Hello","hi","who','are",'you","?Bye']
def m(a):
    z = ""

    for i in a:
        if i.lower() not in vo:
            z+=i
    return z
def asc(a):
    s = 0
    for i in a:
        s +=ord(i)
    return s
def fill(x):
    for i in x:
        if i.lower() in vo:
            return False
    return True
ma = list(map(m,l))

print(ma)

oma = list(map(asc,ma))
print(oma)
fil= list(filter(fill,l))
print(fil)

# n = 11
#
# if n >0:
#     for i in range(n):
#         c = 1
#         for j in range(n):
#             if j<i:
#                 print(" ",end="")
#             else:
#                 if i+1>10:
#                     print(" ",end="")
#                 print(f"{c}",end="")
#             print(" ",end="")
#
#             c+=1
#         print()
# else:
#     print("Invalid Input")
# n = 5
#
# if n > 0:
#     c = 1
#     for i in range(n):
#
#         for j in range(n*n):
#             if j >= (n*n) - (j + 1):
#
#                 print(f"{c:02d}", end="")
#                 print(".",end="")
#                 c += 1
#             else:
#                 print(",", end="")
#
#         print()
# else:
#     print("Invalid Input")