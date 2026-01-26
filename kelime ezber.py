import random
import json
kelimeler="KelimeEzber/kelimeler.json"
def kelime_yukle():
    try:
        with open(kelimeler, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def kelime_kaydet(kelime):

    with open(kelimeler, "w", encoding="utf-8") as f:
        json.dump(kelime, f, ensure_ascii=False, indent=4)

def ing_tr_oyun():
    ing_kelime=kelime_yukle()
    if not ing_kelime:
        print("Kelime Yüklenik Değil..")
        return
    ingilizce=random.choice(list(ing_kelime.keys()))
    dogru_cevap=ing_kelime[ingilizce]
    print(f"\n Kelime: {ingilizce}")
    cevap = input("Türkçesi: ").lower()

    if cevap == dogru_cevap:
        print(" Bildin kanka!")
    else:
        print(f"Yanlış. Doğrusu: {dogru_cevap}")

def tr_ing_oyun():
    tr_kelime=kelime_yukle()
    if not tr_kelime:
        print("Kelime Ekli Değil..")
        return
    
    ters_sozluk = {tr: ing for ing, tr in tr_kelime.items()}
    turkce = random.choice(list(ters_sozluk.keys()))
    dogru_cevap = ters_sozluk[turkce]
    print(f"\n Kelime: {turkce}")
    cevap = input(" İngilizcesi: ").lower()

    if cevap == dogru_cevap:
        print(" Bildin kanka!")
    else:
        print(f" Yanlış. Doğrusu: {dogru_cevap}")

def kelime_ekle():
    kelimeler = kelime_yukle()

    ing = input("İngilizce kelime: ").lower()
    tr = input("Türkçe anlamı: ").lower()

    kelimeler[ing] = tr
    kelime_kaydet(kelimeler)

    print("Kelime başarıyla eklendi!")



def menu():
    while True:
        print("\n KELİME EZBER OYUNU..\n" \
        "       1 - ING ---> TR\n" \
        "       2 - TR ---> ING\n" \
        "       3 - Kelime Girin\n" \
        "       4 - Cıkış")
        secim=input("Seçim Yapınız..")
        if secim == "1":
            ing_tr_oyun()
        elif secim == "2":
            tr_ing_oyun()
        elif secim == "3":
            kelime_ekle()
        elif secim == "" or secim =="4":
            break
    

menu()