# For Kullanımı for ile ÇARPIM TABLOSU:

for a in range(1,10): # range() ile ara belirledik 1 ile 10 arası 1 dail. 10a kadar.
                        #in range() içide gezin diyoruz. a ise bizim belirlediğimiz değişken
    for b in range(1,10):# iç içe for  ile aslında 1 * 2 deki ikinci sayıyı belirliyoruz.
        c=a*b # carpma işlemi.. a ve b dongüye her giridğinde +1 olacak ve iki sayı çarpılacak.
        print(f"{a} * {b} = {c}")# a ve b nin değeri ile çarpmanın sonucunu ekrana yazıyruz
    print("-------------------------")# her guruubu birbirinden ayırdık.
