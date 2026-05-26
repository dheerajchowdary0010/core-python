# class Node:
#     def __init__(self,v):
#         self.val = v
#         self.next = None
#
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def addlinkedlist(self,v):
#         newnode = Node(v)
#         if self.head is None:
#             self.head = newnode
#             return f"added {v}"
#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = newnode
#         return f"added {v}"
#
# l1 = Linkedlist()
# l1.addlinkedlist(1)
# l1.addlinkedlist(2)
# print(l1.head.val)

class Node:
    def __init__(self,a,n):
        self.h= self
        self.val = a
        self.next = n

n1 = Node(1)
n2 = Node(n1)