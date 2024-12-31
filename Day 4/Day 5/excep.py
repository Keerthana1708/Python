'''class Custom_Exception(Exception):
    def __init__(self, message):
        super()
class Sample:
    def test(self,name,age):
        if age>12:
            raise Custom_Exception("Not Eligible")
        else:
            print("Succesfully registered")
obj=Sample()
try:
    obj.test("Keerthana",22)
except Custom_Exception as e:
    print(e)
'''
'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3,"b"}

set3 = set1.symmetric_difference(set2)
print(set3)

x="sys"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)'''

it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon","kkk"]
n = len(it_companies)
if n == 0:
  print("Doesnt Exist")
elif n % 2 == 1:
        middle_index = n // 2
        print([it_companies[middle_index]])
else:
        middle_index1 = (n // 2) - 1
        middle_index2 = n // 2
        print(it_companies[middle_index1:middle_index2 + 1])
