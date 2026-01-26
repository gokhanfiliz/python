"""Bu dersde if ile ilgili örnek yapılacak
basit bir kullanıcı giriş sistemi yapmak
kullanıcı adını ve şifresini alacak
kulllanıcını kontrol edecek doğru ise
şifreyi kontrol edecek 
şifrede doğru ise giriş başarılı mesajını verecek."""
#Kullanıcı adını alıyoruz
kullanici = input("Kullanıcı Adını Giriniz...")
# kullanıcı şifresini alıyoruz..
sifre = input("Şifrenizi Giriniz...")
# Kotrol yapacagız.. ilk kontrol kullanıcı adı
if kullanici=="gokhan":
    if sifre=="123456":
        print("Giriş Başarılı")
    else: 
        print("Sifre Hatalı")
else:
    print("Kullanıcı Adı Yanlış")
