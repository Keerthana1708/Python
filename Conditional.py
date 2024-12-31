
"""my_age=int(input("Enter the age"))
your_age=int(input("Enter your age"))
if my_age<your_age:
    print("You are",(your_age-my_age),"older than me")
elif my_age==your_age:
    print("We are born in the same year")
else:
    print("You are",(my_age-your_age), "younger than me")"""


"""a = int(input("Enter the number one:"))
b= int(input("Enter the number two:"))
if a>b:
    print(a,"is greater than",b)
elif a==b:
    print("Equal")
else:
    print(b,"is greater than",a)"""

"""marks= int(input("Enter the marks:"))
if marks in range(80,101):
    print("A")
elif marks in range(70,90):
    print("B")
elif marks in range(60,70):
    print("C")
elif marks in range(50,60):
    print("D")
else:
    print("F")"""

"""season=input("Enter the season")
if season=="September" or season== "October" or season== "November":
    print("The season is autumn")
elif season=="December" or season== "January" or season== "Febrauary":
    print("The season is winter")
elif season=="March" or season=="April" or season=="May":
    print("The season is Spring")
else:
    print("It is summer")"""

"""fruits = ['banana', 'orange', 'mango', 'lemon'] 
add_fruit = input("Add a fruit")
if add_fruit in fruits:
    print("The fruit already exists in the list")
else:
    fruits.append(add_fruit)
    print(fruits)"""

person={ 
    'first_name': 'Python', 
    'last_name': 'Program', 
    'age': 250, 
    'country': 'India', 
    'is_marred': True, 
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
    'address': { 
        'street': 'Space street', 
        'zipcode': '02210' 
    } 
    } 
'''if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print(middle_skill)'''

"""if 'skills' in person:
     skills = person['skills']
     if "Python" in skills:
          print("Present")
     else:
        print("Not present")
else:
    print("Not such key as that")"""

'''if 'skills' in person:
    skills = person['skills']
    if skills=="Javascipt" and skills=="React":
        print("Front-end developer")
    elif skills=="Node" and skills=="Python" and skills=="MongoDB":
        print("He is a backend developer")
    elif skills=="React" and skills=="Node" and "MongoDB":
        print("Fullstack developer")
    else:
        print("Unknown title")'''

'''if person["is_marred"] and person['country']=="India":
    print("Python program lives in India. He is married")'''

    


