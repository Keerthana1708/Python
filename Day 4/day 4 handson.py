 #Declare a function add_two_numbers. It takes two parameters and it returns a sum. 
'''def add_two_numbers(a,b):
   sum=0
   sum=a+b
   return sum
result =add_two_numbers(5,6)
print(result)'''

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
'''def area_of_circle(r):
    return 3.14*r*r
area = area_of_circle(5)
print(area)'''

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback. 
'''def add_all_nums(a,b,c):
    sum=0
    sum=a+b+c
    return sum

result= add_all_nums(1,2,3)
print(result)'''

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit. 
'''def convert_celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
result = convert_celsius_to_fahrenheit(34)
print(result)'''

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer. 
'''def check_season(month):
    if month=="July" or month=="May":
        return "autumn"
    elif month=="December" or month=="January":
        return "winter"
    elif month=="October" or month=="November":
        return "Spring"
    else:
        return "summer"
result = check_season("January")
print(result)'''

#Write a function called calculate_slope which return the slope of a linear equation 
'''def calculate_slope(a,b,c,d):
    slope = int((b-a)/(d-c))
    return slope
result= calculate_slope(2,4,5,6)
print(result)'''

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
'''def print_list(food):
    for i in food:
        print(i)
result=["masal puri", "sev puri" , "pani puri"]
print_list(result)'''

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops). 
#print(reverse_list([1, 2, 3, 4, 5])) 
# [5, 4, 3, 2, 1]
'''def reverse_list(numbers):
    l = len(numbers)
    for i in range(l,0,-1):
        print(i)
numbers = [1,2,3,4,5]
reverse_list(numbers)'''

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items 
def capitalize_list_items(fruits):
    new_fruits =[]
    for i in fruits:
        new_fruits.append(i.upper())
    print(new_fruits)
fruits=["papaya","mango","banana","orange"]
capitalize_list_items(fruits)

