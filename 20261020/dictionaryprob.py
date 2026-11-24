PRODUK = {
    "A01": {"nama": "Buku Tulis", "harga": 5000},
    "A02": {"nama": "Pensil 2B", "harga": 2500},
    "A03": {"nama": "Penghapus", "harga": 1500},
    "B01": {"nama": "Air Mineral", "harga": 3000},
    "B02": {"nama": "Roti Coklat", "harga": 4500}
}
print(PRODUK)
print(PRODUK.keys())
a = list(PRODUK)  #convert dictionay keys into list
print(a[0])
print(PRODUK[a[0]])
print(PRODUK[a[0]]["nama"])
print(PRODUK["A01"])