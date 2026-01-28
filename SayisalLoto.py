import random # rastgele sayı için ilgili kütüphaneyi ekliyoruz.
# 3 den 11 arası satırlar tek bir kolon üretmek için.
"""cikan=set()   # cikan sayıları tutmak için set uluşturduk.


while len(cikan)<6: # altı adet rasgele sayı üretsin diye dongü..
    kupon=random.randint(1,49) # 1 ile 49 dahil sayı üretilecek 0/50 arası diyebiliriz..
    cikan.add(kupon) # olusturulan sayı cikan sete ekleniyor.


print(sorted(cikan))"""

# buradan sonraki kodlar birden fazla bir birinden farklı kolon üretmek için..
# mantık aynı iç içe while kullandık. ve set için tuple  kullandık..
kuponlar = set()
adet=int(input("Kupon Adedini Giriniz.."))
while len(kuponlar) < adet:
    kupon = set()
    while len(kupon) < 6:
        kupon.add(random.randint(1, 49))
    5
    kuponlar.add(tuple(sorted(kupon)))

for i, k in enumerate(kuponlar, 1):
    print(f"{i}. kupon:", list(k))
