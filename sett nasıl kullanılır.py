
# set içinde bir değer ancak bir kere yazılır.. 
sayilar = set()          # boş set 

for i in range(10):
    x = int(input("Sayı gir: "))
    sayilar.add(x)       # x değerini set'e ekle

print(sayilar)