#swapping variables
x = 100
y = 500
# z = x
# x = y
# y = z
print("x: ",x)
print("y: ",y)
(x,y)=(y,x)
print("x: ",x)
print("y: ",y)

def q_and_r(x,y):
    q = x // y
    r = x % y
    return (q,r)

(hasilbagi, sisa) = q_and_r(x,y)
print("Hasil bagi: ", hasilbagi)
print("Sisa: ", sisa)

aTuple = ("makan pagi", "makan siang","snack",-20,500)
for x in aTuple:
    print(x)
