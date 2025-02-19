faiz = 1.59
vade = "36"
krediAdı = "İhtiyaç Kredisi"

print(type(faiz))  # float
print(type(vade))  # str
print(type(krediAdı))  # str

# print(vade + 12) # TypeError: str (int ile) birleştirilemez
# print(int(krediAdı)) # ValueError: int() için geçersiz değer: 'İhtiyaç Kredisi'

print(int(vade) + 12)  # 48

faiz = str(faiz)
print(type(faiz))  # str

vade = int(input("Lütfen istediğiniz vade miktarını girin: "))
print(type(vade))  # int
vade = vade + 12

# String interpolation
print("Seçtiğiniz vade: " + str(vade))
print("Seçtiğiniz vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade: {vade}")

isim = "Busra"
metin = "Merhaba {isim}".format(isim="Irem")
print(metin)

# f-string
metin = f"Hoş geldin {isim}"
print(metin)

# Listeler
dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)  # ['İhtiyaç Kredisi', 10, 5.2, True]

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))  # list

print(krediler)  # ['İhtiyaç Kredisi', 'Taşıt Kredisi', 'Konut Kredisi']
print(krediler[0])  # İhtiyaç Kredisi

# print(krediler[3]) # IndexError: liste dışı indeks

print(len(krediler))  # 3

krediler.append("Özel Kredi")  # Listenin sonuna eleman ekle
print(krediler)  # ['İhtiyaç Kredisi', 'Taşıt Kredisi', 'Konut Kredisi', 'Özel Kredi']

krediler.append("X Kredisi")
print(krediler)  # ['İhtiyaç Kredisi', 'Taşıt Kredisi', 'Konut Kredisi', 'Özel Kredi', 'X Kredisi']

krediler.pop(0)
print(krediler)  # ['Taşıt Kredisi', 'Konut Kredisi', 'Özel Kredi', 'X Kredisi']

krediler.append("Taşıt Kredisi")
print(krediler)  # ['Taşıt Kredisi', 'Konut Kredisi', 'Özel Kredi', 'X Kredisi', 'Taşıt Kredisi']

krediler.remove("Taşıt Kredisi")
print(krediler)  # ['Konut Kredisi', 'Özel Kredi', 'X Kredisi']

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)  # ['Konut Kredisi', 'Özel Kredi', 'X Kredisi', 'Y Kredisi', 'Z Kredisi']

# Döngüler
for i in range(10):
    print(i)  # 0 1 2 3 4 5 6 7 8 9

print("===============")

for i in range(5, 10):
    print(i)  # 5 6 7 8 9

print("===============")

for i in range(0, 51, 10):
    print(i)  # 0 10 20 30 40 50

print("===============")

# for i in range(0.1, 0.5):
#     print(i)  # TypeError: 'float' object cannot be interpreted as an integer

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]

for kredi in krediler:
    print(kredi)  # İhtiyaç Kredisi Taşıt Kredisi Konut Kredisi

print("===============")

for i in range(len(krediler)):
    print(krediler[i])  # İhtiyaç Kredisi Taşıt Kredisi Konut Kredisi

print("===============")

# while True:
#     print("x") # Sonsuz döngü

i = 0
while i < 10:
    print("x")  # x x x x x x x x x x
    i += 1

print("************")

i = 0
while i < len(krediler):
    i += 1
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

print("=====Fonksiyonlar=====")

# Fonksiyonlar
fiyat = 100
indirim = 20

def calculate():
    print(100 - 20)


def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)


def sayHello(isim):
    print(f"Merhaba {isim}")

calculate()
calculateWithParams(100, 20)
calculateWithParams(fiyat, indirim)
sayHello("Ali")
sayHello("Emre")


def calculateAndReturn(fiyat, indirim):
    return fiyat - indirim


yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat)  # 150


# void fonksiyonu
def fiyatcalculate(fiyat, indirim):
    print(fiyat - indirim)


# return değeri olan fonksiyon
def fiyatcalculateAndReturn(fiyat, indirim):
    return fiyat - indirim


print("************")
func1 = fiyatcalculate(100, 50)
func2 = fiyatcalculateAndReturn(300, 100)

print(func1)  # None
print(func2)  # 200

print("************")