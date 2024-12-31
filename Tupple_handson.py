a = ()
print(a)

siblings=("Karthikeya","Kavya","Kaustubha","Subhashini","Aditya","Akilesh","Venkatesh")
print(siblings)

brothers=("Karthikeya","Suresh","Kaustuba")
sisters=("Subhashini","Aradya","Kavya")
siblings=sisters.__add__(brothers)
print(siblings)

n=len(siblings)
print(n)

family_members=siblings+("Shyam","Veena")
print(family_members)

len=len(family_members)
sib = family_members[0:len-2]
print(sib)
parents = family_members[len-2:]
print(parents)

fruits =("Mango","Banana","Apple")
vegetables=("Raddish","Brinjal","Cucumber")
animal_prod=("Dairy","eggs")
food_stuff_tp=fruits.__add__(vegetables).__add__(animal_prod)
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

first = food_stuff_lt[0:3]
last = food_stuff_lt[3:]
print(first)
print(last)

#del food_stuff_tp
#print(food_stuff_tp)

nordic_countries = ('Denmark', 'India','Iceland', 'Norway', 'Sweden') 
m= 'Estonia' in nordic_countries
print(m)
n = 'Iceland' in nordic_countries
print(n)