class produk:
      def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

      def tampil_info(self):
          print(f"produk={self.nama} , harga Rp{self.harga}")

      def hitung_total(self,jumlah):
          return self.harga*jumlah

#buat 2 objek dari class produk

produk1 = produk("laptop", 250000)
produk2 = produk("tab", 150000)

#tampilkan informasi
produk1.tampil_info()
produk2.tampil_info()

#hitung total harga beli

total_laptop = produk1.hitung_total (4)
total_tab = produk2.hitung_total (5)

print(f"total harga 4 laptop = Rp(total_laptop)")
print(f"total harga 5 laptop = Rp(total_tab)")

