class sorter:
    def change(self,star):
        star.change()
class BS:
    def change(self):
        pass
class MS:
    def change(self):
        pass
class  QS:
    def change(self):
        pass

b = BS()
m = MS()
q  = QS()
s = sorter()
l = [b,m,q]
for i in l:
    s.change(i)

