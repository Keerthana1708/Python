from threading import Thread
from time import sleep 
class Sample(Thread):
    def m1(self):
        for i in range(1,21):
            print(i)
            sleep(1)
    def run(self):
        self.m1()
class Demo(Thread):
    def m2(self):
        for i in range(21,41):
            print(i)
            sleep(1)
    def run(self):
        self.m2()
obj1 = Sample()
obj2=Demo()
obj1.start()
obj2.start()