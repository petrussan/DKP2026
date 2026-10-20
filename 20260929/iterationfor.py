for i in range(5):
    print(i)
print("")

for i in range(5):
    print(i,end=" ")
print("")

for i in range(5):
    print(i,end=" ")
    for j in range(i):
        print(" ",end="")
print("")

for i in range(1,10,2):
    print(i, end=" ")
print("")

names=["Andi","Budi","Candra","Dave"]
for name in names:
    print(name)