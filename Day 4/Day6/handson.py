#Write a program with a function that the function will multiply the number N with three. 
'''def mul(n):
    print(n*3)
mul(5)'''

#Write a program with a function that the function will check if the number N is divisible by 7. 
'''def div(n):
    if n%7==0:
        print("Divisible")
    else:
        print("Not divisible")
div(49)'''

#Write a function that takes a number N as an argument. 
#Write a program that checks if N is between 200 and 500. 
#Print Yes if N is between 200 and 500. Otherwise, print No. 
'''def check(n):
   if n>200 and n<500:
      print("Yes")
   else:
      print("No")
check(230)'''

#If the bill amount is less than 500, the discount should be "5%". 
#If the bill amount is greater than or equal to 500 and less than 2500, the discount should be "10%" 
#If the bill amount is greater than or equal to 2500, the discount should be "20%" 
'''def calc_discount(bill):
    if bill <500:
        discount=bill-((5/100)*bill)
        print(discount)
    elif bill>=500 and bill<2500:
        discount=bill-((10/100)*bill)
        print(discount)
    else:
        discount=bill-((20/100)*bill)
        print(discount)
calc_discount(300)'''

#Write a function with the name show_number that takes a number N and print all the numbers from 0 to N with a label to identify the even and odd numbers. 
'''def show_number(n):
    if n%2==0:
        print(n,"Even")
    else:
        print(n,"odd")
show_number(8)'''

#For the problem , the prefilled code will contain a function. Write a program that the given function will return the perimeter of the square. 

#The sum of the lengths of the four sides of square is the perimeter of the square. 


'''def perimeter_of_square(side): 
    perimeter=4*side
    return perimeter
side = int(input()) 
result = perimeter_of_square(side) 
print(result) '''

#A function is given in prefilled code that takes a string S as an argument. 
#Write a program that prints the count of uppercase letters in the given string S. 
'''def count_of_uppercase(word): 
    count=0
    for char in word:
        if char.isupper():
            count=count+1
    return count
print(count_of_uppercase("KeerTHANA"))'''

#Write a function with the name get_speed_status that takes the speed(S) as an argument. 
#If the speed is less than 60, it should return "Normal" 
#If the speed is greater than or equal to 60 and less than 80, it should return "Warning" 
#If the speed is greater than or equal to 80, it should return "Over Speed" 
'''def get_speed_status(speed): 
     if speed<60:
          return "Normal"
     elif speed>=60 and speed<80:
          return "Warning"
     else:
          return "Over Speed"

speed = int(input()) 
print(get_speed_status(speed))'''




'''print("Hello,World")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")'''

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()






 



 




