print("=========================")
print("Operasi Matematika")
print("1. Jumlah     [+]")
print("2. Kurang     [-]")
print("3. Kali       [*]")
print("4. Bagi       [/]")
print("=========================")
a = int(input("Pilih operasi (1/2/3/4) :"))
print("=========================")
bilpertama= int(input("Masukkan bilangan pertama :"))
bilkedua= int(input("Masukkan bilangan kedua :"))
def satu_jumlah(a,bilpertama,bilkedua):
    b= bilpertama+bilkedua
    return b
def dua_kurang(a,bilpertama,bilkedua):
    b= bilpertama-bilkedua
    return b
def tiga_kali(a,bilpertama,bilkedua):
    b= bilpertama*bilkedua
    return b
def empat_bagi(a,bilpertama,bilkedua):
    b= bilpertama/bilkedua
    return b
if a==1:
    print("Hasil operasi dari :", bilpertama, "+", bilkedua,"=",satu_jumlah(a,bilpertama,bilkedua))
elif a==2:
    print("Hasil operasi dari :", bilpertama, "-", bilkedua, "=",dua_kurang(a,bilpertama,bilkedua))
elif a==3:
    print("Hasil operasi dari :", bilpertama, "*", bilkedua, "=",tiga_kali(a,bilpertama,bilkedua))
elif a==4:
    print("Hasil operasi dari :", bilpertama, "/", bilkedua, "=",empat_bagi(a,bilpertama,bilkedua))


