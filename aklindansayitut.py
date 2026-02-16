import random as rn

def main ():
	menu = {"1" : pc_karsi_oyna,
		"2" : user_karsi_oyna,
		"3" : cikis
		}
	while True:

		print(menu_list())
		secim = input("Secim Yapınız: ")
		if secim in menu:
			menu[secim]()
		else:
			print(" Geçersiz Seçim ")

def menu_list():
	return(" 1 - Bilgisayarın Tuttuğu Sayıyı Bul.. \n"
			" 2 - Bilgisayar Senin Tuttuğun Sayıyı Bulsun..\n"
			" 3 - Çıkış")

def rastgele_sayi(k_sayi=0,b_sayi=100):
	sayi = rn.randint(k_sayi,b_sayi)
	return sayi

def tahmin_kontrol(sayi,tahmin):
	if sayi==tahmin:
		print("Doğru Tahmin Bildin")
		return True
	elif sayi<tahmin:
		print("Tuttugun sayıyı düşür")
		return False
	else:
		print("Tuttugun sayıyı yükselt")
		return False
	

def pc_karsi_oyna():
	sayi = rastgele_sayi()
	print("0 ile 100 arasında sayı tuttum bil bakalım")
	dogru = False
	while not dogru:
		tahmin = int(input("Hadi Tahmin Gir: "))
		dogru = tahmin_kontrol(sayi,tahmin)
		
def user_karsi_oyna():
	input("Hadi Aklından Bir Sayı Tut..\nTuttuysan ENTER Bas..")
	kucuk_sayilar = [1]
	buyuk_sayilar=[100]
	tahmin = rastgele_sayi()
	
	dogru = False
	while not dogru:
		print(f"Tahminim {tahmin} Doğru ise D  küçükse K büyükse B bas.")
		secim = input().upper()
		if secim =="D":
			dogru=True
		elif  secim =="K" :
			kucuk_sayilar.append(tahmin)
			k_sayi=max(kucuk_sayilar)
			b_sayi=min(buyuk_sayilar)
			tahmin = rastgele_sayi(k_sayi,b_sayi)

		elif secim == "B":
			buyuk_sayilar.append(tahmin)
			k_sayi=max(kucuk_sayilar)
			b_sayi=min(buyuk_sayilar)
			tahmin = rastgele_sayi(k_sayi,b_sayi)
			
		else:
			print(f" Seçim {secim} olamaz. D,K,B birini gir")
def cikis():
	exit()


main()

