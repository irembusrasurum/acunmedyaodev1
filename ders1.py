print("kodlamaio")

# Değişken Tanımlama (variableName = değer(int, float, string, boolean))
baslik = "Araba Kredisi"  # string => metinsel ifade

print(baslik)

baslik = "İhtiyaç Kredisi"  # string => metinsel ifade

print(baslik)

vade = 36  # int => tam sayı
ekVade = 6  # int => tam sayı

vade2 = "36"  # string => metinsel ifade

aylikOdeme = 200.50  # float => ondalıklı sayı

artisVarMi = True  # boolean => doğru veya yanlış

# Matematiksel Operatörler

# + => toplama
print(5 + 5)  # 10
print(vade + 12)  # 48
print(vade + ekVade)  # 42
print(36 + 6)  # 42

# - => çıkarma
print(5 - 5)  # 0
print(vade - 12)  # 24
print(vade - ekVade)  # 30
print(36 - 6)  # 30

# * => çarpma
print(5 * 5)  # 25
print(vade * 12)  # 432
print(vade * ekVade)  # 216
print(10 * 10)  # 100

# / => bölme
print(5 / 5)  # 1.0
print(vade / 2)  # 18.0
print(vade / ekVade)  # 6.0
print(10 / 2)  # 5.0

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)  # 18.0
print(indirimliFiyat)  # 80

# % => mod (bölme işleminden kalan)
print(10 % 2)  # 0
print(vade % 5)  # 1
print(vade % ekVade)  # 0
print(30 % 10)  # 0

# Mantıksal Operatörler

# == => eşittir
print(1 == 1)  # True
print(1 == 2)  # False

# > => büyüktür
print(1 > 2)  # False
print(3 > 1)  # True
print(1 > 1)  # False
print(1 >= 1)  # True

# < => küçüktür
print(1 < 2)  # True
print(3 < 1)  # False
print(1 < 1)  # False
print(1 <= 1)  # True

# != => eşit değildir
print(1 != 1)  # False
print(1 != 2)  # True

# or => veya
# En az birinin doğru olması yeterlidir
print(1 > 2 or 5 > 2)  # (False veya True) => True
print(1 > 2 or 5 > 2 and 3 > 2)  # (False veya True ve True) => True
print(1 > 2 and 5 > 2 and 3 > 2)  # (False ve True ve True) => False
print(2 > 1 or 1 > 2 and 3 > 2)  # (True veya False ve True) => True

# and => ve
# Hepsinin doğru olması gerekir
print(1 > 2 and 5 > 2)  # (False ve True) => False

# Koşullu İfadeler (If Statement)

# if koşul:
#     kod bloğu çalışır

sayi1 = 15
sayi2 = 15

if sayi1 < sayi2:
    print("sayi1, sayi2'den küçüktür")
    print("if bloğunun içindeyiz")
elif sayi1 == sayi2:
    print("sayi1, sayi2'ye eşittir")
    print("elif bloğunun içindeyiz")
else:
    print("sayi2, sayi1'den küçüktür")
    print("else bloğunun içindeyiz")

print("if bloğunun dışındayız")

if sayi1 <= sayi2:
    print("sayi1, sayi2'ye küçük veya eşittir")
if sayi1 == sayi2:
    print("sayi1, sayi2'ye eşittir")
else:
    print("sayi2, sayi1'den büyüktür")

# Sonuç => sayi1, sayi2'ye küçük veya eşittir, sayi1, sayi2'ye eşittir

if sayi1 < sayi2:
    print("sayi1, sayi2'den küçüktür")
    if sayi1 == sayi2:
        print("sayi1, sayi2'ye eşittir")
else:
    print("sayi2, sayi1'den büyüktür")

# Sonuç => sayi2, sayi1'den büyüktür
