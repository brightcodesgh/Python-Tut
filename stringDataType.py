#String - assigning a multiline string
my_Statement = """This is my very little state., 
I want to say Python is also cool, 
i never liked it though"""
print(my_Statement) 
print(" ")

#Working with strings as arrays
    #getting a character from a string
h = "This is a subtle comment"
print(h[1])
print(" ")

#Looping through a string
for x in "Banana":
    print(x)
print(" ")

#Getting the length of a string 
q = "Find the length of this String"
print(len(q))
print(" ")

#checking if a text or character exists in a string 
txt = "This is a text.. checking !"
print("checking" in txt)


#Using if statement to do the checks 
if "checking" in txt:
    print("checking exists in the string")
print(" ")

#if "checking does not exists then we use the not keyword"
if "checking" not in txt:
    print("checking is not present in the string")