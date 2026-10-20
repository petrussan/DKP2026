myList = [11,222,43]
print(myList)
myList.append(3)
print("append:",myList)
myList.extend([49,16])
print("extend:",myList)
del(myList[5])
print("del:",myList)
myList.remove(3)
print("remove:",myList)
x = myList.pop()
x = myList.pop()
print("pop pop:",myList)
print(x)
myList.extend([11,21,222,750,2,4,3])
print("extend:", myList)
myList.reverse()
print("reverse:",myList)
sortedList = sorted(myList)
print("sorted:",sortedList)
print("after sorted:",myList)
myList.sort()
print("sort:",myList)
myList.sort(reverse=True)
print("sort,reverse:",myList)

nameList = ["Jasen","Richard","Jonathan","joseph"]
nameList.sort(key=len)
print(nameList)
nameList.sort()
print(nameList)
nameList.sort(key=str.lower)
print(nameList)

#convert string to list
s = "I Love PCU"
lists= list(s)
print(lists)
listword= s.split(' ')
print(listword)

#convert list to string
aList = ['a','b','c']
aString = ''.join(aList)
print(aString)

secondList = myList.copy()
thirdList = myList[:]
selectedList = myList[0:4:2]
print(secondList)
print(thirdList)
print(myList)
print(selectedList)
myList.pop()
print(secondList)
print(thirdList)
print(myList)

warm = ["yellow","orange"]
hot = ["red"]
brightcolors = [warm]
brightcolors.append(hot)
print(brightcolors)
hot.append("pink")
print(hot)
print(brightcolors)
