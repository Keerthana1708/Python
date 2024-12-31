class Sample:
    def m1(self):
        print("m1")
class Demo(Sample):
    def m2(self):
        print("m2")
obj1=Demo()
obj1.m2()
obj1.m1()
