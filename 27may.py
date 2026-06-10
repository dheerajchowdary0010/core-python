# q3
# class SecureFile:
#     def __init__(self,c,p):
#         self.__content = c
#         self.password = p
#     def read(self,password):
#         if password==self.password:
#             return self.__content
#         else:
#             return "403 Unauthorized attempt"
#
# fil = SecureFile("amksac","sss")
# print(fil.read("sss"))

# # q10
# class q10:
#     __va = 10
#     @property
#     def getva(self):
#         return self.__va
#     @getva.setter
#     def getva(self,a:int):
#         self.__va=a
#
# q = q10()
# print(q.getva)
# q.getva = 100
# print(q.getva)