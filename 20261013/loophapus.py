def hapuskembar(L1,L2):
    L1copy = L1[:]
    for x in L1copy:
        if x in L2:
            L1.remove(x)
fruit01=["apel","alpukat","pisang"]
fruit02=["apel","alpukat","nanas"]
hapuskembar(fruit01,fruit02)
print(fruit01)
print(fruit02)