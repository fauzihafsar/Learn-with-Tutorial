uang = input("punya uang berapa??")
harga = 25000

if int(uang) < harga:
  print("maaf uang anda kurang")
  print("barang tidak bisa dibeli")

elif int(uang) == harga:
    print("terimakasih, silahkan dateng lagi!!")

else:
  print("uang nya kami terima")
  print("ini kembaliannya")
