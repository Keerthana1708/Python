'''def m1():
    print("Hello")
m1() 

def m1(a,b):
    print(a+b)
m1(10,20)'''

#object oriented programming   
class Sample:
    a=10
    name="Python"
    def m1(self):
        print("m1")
    def m2(self): #self is "this" in python
        self.m1() #calling a func inside a func
    def __init__(self):
        print("Hello")
obj1=Sample()
print(obj1.a)
print(obj1.name)
obj1.m2()