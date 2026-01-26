# Birinci ders örnekeri 
"""Temel giriş cıkış komutlarını kullanmayı öğreniyoruz
Öğrenci adı soy adını alıp
bir ve ikinci ders notu alıp 
Ders ortalamasını ekrana basacagız"""
# Öğrencinin AD Soyadını al
Ad = input("Öğrencinin Adı Soyadı")
# sırası ile birinci notunu ve ikinci notunu int olarak alıyoruz.
ders1 = int(input("Birinci Notunu Giriniz"))
ders2 = int(input("İkinci Notunu Giriniz."))
# iki notun ortalmasını hesaplıyoruz
ortalama = (ders1+ders2)/2
# ekrana ögrenci bilgilerini ve ortalamasını basıyoruz.
print(f"Öğrenci {Ad},Birinci Notu {ders1},İkinci Notu {ders2}, Ortalamsı{ortalama}")
