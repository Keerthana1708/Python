it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24] 


n=len(it_companies)
print(it_companies)

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["WellsFargo","Flipkart"])
print(it_companies)

it_companies.remove("WellsFargo")
print(it_companies)

it_companies.discard("SalesForce")
print(it_companies)

result=A.union(B)
print(result)

result1=A.intersection(B)
print(result1)

C= A.issubset(B)

C= A.isdisjoint(B)
print(C)

res=A.union(B)
res1=B.union(A)
print(res)
print(res1)

sym = A.symmetric_difference(B)
print(sym)

#del A
del B
#print(A)

new_ages = set(age)
print(new_ages)
#list is bigger as it includes duplicates

sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print(unique_words)
num_unique_words = len(unique_words)
print(num_unique_words)


