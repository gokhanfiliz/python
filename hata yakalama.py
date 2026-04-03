# hata yakalayıp hatayı ekrana basma.
# örnek kod basit bir parola kontrol sistemi yapmı.
# Girilen değerleri kontrol edilecek. Parola en 8 karakter En az bir büyük ve bir küçüm harf.
# Ve en az bir rakam ile ascii karakterlerden oluşacak şekilde olacak.

import re

def kontrol(parola):
    if len(parola) < 8:
        raise Exception ("Parola 8 Karakterden Az Olamaz.!")
    elif not re.search("[a-z]",parola):
        raise Exception("Parola içinde Küçük Harf Olması Lazım.!")
    elif not re.search("[A-Z]",parola):
        raise Exception("Parolada Büyük Harf Olması Lazım.!")
    elif not re.search("[@$*+_]",parola):
        raise Exception("Parola için @+*/-$ Olması Lazım.!")
    elif not re.search("[0-9]",parola):
        raise Exception("Parolada Rakam İçirmelidir.!")
    elif re.search("\\s",parola):
        raise Exception("Parolada Boşluk Var.!")
    
while True:
    sifre = input(" Parola girişi yapınız! ")
    try:
        kontrol(sifre)
    except Exception as hata:
        print(hata)
    else:
        print("Geçerli Parola..")
        break
    finally:
        pass

    
