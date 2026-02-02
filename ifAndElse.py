#short hand if 
if 20 > 10: print("20 is greater than 10")
print(" ")
#short hand if else
a= 15
b=30
print("a is greater") if a>b else print("b is greater ")

#chaining consitional expression
x= 350
i=150
print("x is lesser") if x<i else print("i is lesser") if i<x else print("they are equal")


#turnary operation

username = "wavy"
user= username if username else "guest"
print("Welcome ",user)