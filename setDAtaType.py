mySet = { "Bright", 24, True, 45.67 }
print(mySet)
print(len(mySet))
print(" ")

#access a set item 
colors = { "Red", "Blue", "Green", "Yellow" }
for x in colors:
    print(x)
print(" ")

#add a whole new set to an existing set
newColors = { "Brown", "Purple", "Orange" }
colors.update(newColors)
print(colors)
print(" ")

#add a single item to a set
colors.add("Black")
print(colors)
print(" ")

#remove an item from a set
colors.remove("Green") # raises an error if the item to remove does not exist
print(colors)   