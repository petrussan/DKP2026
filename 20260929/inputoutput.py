nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))

print("Hallo," ,nama, "! Umur Anda: ", umur,"tahun.")

with open("data.txt","w") as file:
    print(nama, file=file)
    print(umur, file=file)
