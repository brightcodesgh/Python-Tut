myList = ["apple", "banana", "mango"]
newList = ["avocado", "pineapple", "water melon"]
myList[1:3] = ["kiwi", "pear"]
myList.insert(3, "grapes")
myList.append("pawpaw")
print(myList)
myList.extend(newList)
print(myList)
print(len(myList))
print(" ")

#Looping through list items 
for i in myList:
    print(i)

print(" ")
for i,value in enumerate(myList):
    print(i, value)

print(" ")
#looping with index
for i in range(len(myList)):
    print(i)