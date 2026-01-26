"""Ögrenci not ortalamasını hesaplayan ve 
gecip gecmedigini soyleyen program
if ve temel giriş çıkıs birimleri kullanılacak"""
# Ögrenci adını soyadını al 
ogrenci = input(" Ögrenci Adı ve Soyadını Giriniz..  ")
# ogrencinin birinci ve ikinci notlarını al..
s1 = int(input(" Ögrencinin Birinci Notunu Giriniz.. "))
s2 = int(input("Ögrencinin İkinci Notunu Giriniz... "))
# ögrencinin not ortalamasını hesapla
ort = (s1+s2)/2
# not ortalamsına göre notunu harf cinsinden belirle ve
# ekrana yazdır.
""" 84 - 100 AA
77 - 83 AB
71 - 76 BA
66 - 70 BB
61 - 65 BC
56 - 60 CB
50 - 55 CC
46 - 49 CD
40 - 45 DC
35 - 39 DD
0 -  34 FF"""
if ort>= 84:
    print(f"{ogrenci} Notun {ort} AA ile Geçtin..")
elif ort>=77:
    print(f"{ogrenci} Notun {ort} AB ile Geçtin..")
elif ort>=71:
    print(f"{ogrenci} Notun {ort} BA ile Geçtin..")
elif ort>=66:
    print(f"{ogrenci} Notun {ort} BB ile Geçtin..")
elif ort>=61:
    print(f"{ogrenci} Notun {ort} BC ile Geçtin..")
elif ort>=56:
    print(f"{ogrenci} Notun {ort} CB ile Geçtin..")
elif ort>=50:
    print(f"{ogrenci} Notun {ort} CC ile Geçtin..")
elif ort>=46:
    print(f"{ogrenci} Notun {ort} CD ile KALDIN..")
elif ort>= 40:
     print(f"{ogrenci} Notun {ort} DC ile KALDIN..")
elif ort>=35:
     print(f"{ogrenci} Notun {ort} DD ile KALDIN..")
else:
     print(f"{ogrenci} Notun {ort} FF ile KALDIN..")