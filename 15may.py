# class BankAccount:
#     def __init__(self,a,b):
#         self.account_holder=a
#         self.balance=b
#
#     def deposit(self,amount):
#         self.balance += amount
#
#     def withdraw(self,amount):
#         if amount>self.balance:
#             return f"not available balance,balance{self.balance}"
#     def __str__(self):
#         return
#     def __getattribute__(self, item):
#         print(f"called {item}")
#         return super().__getattribute__(item)

class Books:
    def __init__(self,t,a):
        self.title = t
        self.author = a
        self.is_browwed = False
    def __setattr__(self, key, value):
        if key=="title":
            if len(value)<7:
                return f"length of title is not enough"
        return super().__setattr__(key, value)
    def __str__(self):
        return f"title: {self.title},author:{self.author}"
class Library:

    booklist = []
    def broww(self,book,user):
        user.book_borrowed.append(book.title)
        book.is_browwed = True
        Library.booklist.remove(book)
    def __add__(self, other):
        return Library.booklist.append(other)

    def __sub__(self, other):
        if other in Library.booklist:
            return Library.booklist.remove(other)
        else:
            return "Book not found"



class User:
    def __init__(self,n):
        self.name = n
        self.book_borrowed= []

