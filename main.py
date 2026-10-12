from produk import produk

produk1 = produk("laptop", 250000)
produk2 = produk("tab", 150000)

produk1.tampil_info()
produk2.tampil_info()

total_laptop = produk1.hitung_total (4)
total_tab = produk2.hitung_total (5)

print(f"total harga 4 laptop = Rp(total_laptop)")
print(f"total harga 5 laptop = Rp(total_tab)")

#################
from produk import produk

jumlah_produk = int(input("Masukkan jumlah produk : "))

for i in range(1, jumlah_produk + 1):
    print(f"\nProduk {i}")
    nama = input("Nama   : ")
    harga = int(input("Harga  : "))
    jumlah = int(input("Jumlah : "))

    produks = produk(nama, harga)

    produks.tampilkan_info()
    total = produks.hitung_total(jumlah)
    print(f"Total harga {produks.nama} ({jumlah} buah): Rp{total}")