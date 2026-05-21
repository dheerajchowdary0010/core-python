class Book:
    def __init__(self,t,a,p):
        self.title = t
        self.author = a
        self.pages = p
    def __str__(self):
        return f"{self.title},{self.author},{self.pages}"
    def __add__(self, other):
        return self.pages+other.pages
    def __floordiv__(self, other):
        return self.pages//other
    def timetaken(self):
        return f"{self.pages * 2} minutes"

    def __gt__(self, other):
        return self.pages>other.pages
    def __eq__(self, other):
        return self.title==other.title
    def __getattr__(self, item):
        return f"not found {item}"
    def __setattr__(self, key, value):
        if key == "title":
            if len(value)<7:
                return f"value len must be >7"
        super().__setattr__(key,value)

    def __getattribute__(self, item):

        return super().__getattribute__(item)

b = Book("hashdkai","jhaufhah",100)
b2 = Book("hashdkai","jhaufhah",100)
b3 = Book("hashdaikai","jhaufhah",200)
print(b)
print(b2+b3)
print(b==b2)
print(b.asj)
print(b>b3)
print(b.timetaken())
print(b.title)
b.title="shdjashdhasd"
print(b.title)