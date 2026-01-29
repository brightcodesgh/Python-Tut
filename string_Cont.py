#Starting with value assignment(multi value assignment)

x,y,z = "orange", "mango", "banana"
print(x)
print(y)
print(z)
print(" ")

#assigning multiple variables to one value
a = b = c = "cargo"
print(a)
print(b)
print(c)
print(" ")

#unpacking with variables
my_list = ["apple", "cherry", "grapes"]
h,j,k= my_list
print(h)
print(j)
print(k)
print(" ")

#Printing variables
    #the right way
t=5
g="hello"
print(t, g)

    #the wrong way
# p=5
# i="hello"
# print(p + i)
print(" ")

#Slicing a string
p = "Refreshing Python"
# print(p[2:5])
print(p[-2:-1])
print("  ")    

#modifying string to uppercase
print(g.upper())# we use the lower() method for lowercase
print(" ")

#removing white spaces
l="White Spaces "
print(l.strip())
print(l.replace("S", "E"))