""" işlemler adında bir sözlük tanımladık.
Ve bu sözlüğün value kısmına lambda ile fonksiyon yatpık + - * / için..  """
islemler = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

while True: # programın ana döngüsü devamlı çalışsın diye
    try: # hataları yaklamaya çalışıyoruz. sıfıra bölme gibi
        sonuc = float(input("Sayı girin: ")) # sonuc değişkeni bizim em sonucu tutan hemnde ilk rakamı alan değişken
        op = input("İşlem (+ - * /): ") # operaötor seçimini op değişkeni ile alıp daha sonra sözlükte duruma göre işlem yapılacak

        if op not in islemler: # +-*/ girilip girilmediğini kotrol ediyoruz.. rakam yada harf girebilir klavyeden.. onun önlemi
            print("Hatalı operatör!")
            continue

        sayi = float(input("Sayı girin: ")) # 2. sayıyı aldık
        sonuc = islemler[op](sonuc, sayi) # işemi yapması için sözlüğe girilen değerler gidiyor.. söyle bişey oluyor + 3,5 gibi
        print("Sonuç:", sonuc)

        while True: # işlem devam etmesi için yapılan döngü
            op = input("Devam için + - * /, sıfırlamak için C: ").upper()
            if op == "C":
                break
            if op not in islemler:
                print("Hatalı operatör!")
                continue

            sayi = float(input("Sayı girin: "))
            sonuc = islemler[op](sonuc, sayi)
            print("Sonuç:", sonuc)

    except ZeroDivisionError:
        print("Sıfıra bölme hatası!")
    except ValueError:
        print("Lütfen sayı giriniz!")

