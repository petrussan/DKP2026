import winsound

def is_even(n):
    """
    input: n, an integer number
    return True if in is even, otherwise False
    """
    print("inside function is_even")
    return n%2==0

def hello():
    print("Hello World!")
    print(chr(7))
    winsound.Beep(2000,1500)

def tentukanganjilgenap(n):
    """
    input: n, an integer number
    """
    if n%2==0:
        print("Bilangan genap")
    else:
        print("Bilangan ganjil")

# number = int(input("Masukkan bilangan: "))
# print(is_even(number))
# print(is_even.__doc__)
# print(print.__doc__)
# n=100
# print(n)

# tentukanganjilgenap(number)
# hello()


# sum = lambda a1,a2 : a1+a2
# hasil = lambda a,b,c,d,e : a*b+c/d-e
# print("Hasil Penjumlahan: ",sum(10,20))
# print("Hasil perhitungan: ",hasil(1,11,2,20,3))

total = 0
def add(arg1,arg2):
    # print(total)
    # global total
    total = arg1+arg2
    print("total, di dalam fungsi: ", total)
    return total

# total = add(10,20)
add(10,20)
print("total, di luar fungsi: ", total)

# 5vPLOB
# IdPoTJ