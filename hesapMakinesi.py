import math
class basitHesaplama():
    def topla(self, birinciSayi, ikinciSayi):
        return birinciSayi + ikinciSayi
    def cikar(self, birinciSayi, ikinciSayi):
        return birinciSayi - ikinciSayi 
    def carp(self, birinciSayi, ikinciSayi):
        return birinciSayi * ikinciSayi
    def bol(self, birinciSayi, ikinciSayi):
        return birinciSayi / ikinciSayi
class gelismisHesaplama():
    def usAl(self, taban, ust):
        return pow(taban, ust)
    def karakokAl(self, sayi, derece):
        return pow(sayi, 1/derece)
    def logAl(self, sayi, taban):
        return math.log(sayi, taban)
    def trigonometriHesapla(self, fonk, derece):
        derece = math.radians(derece)
        if(fonk == "sin"):
            return math.sin(derece)
        elif(fonk == "cos"):
            return math.cos(derece)
        elif(fonk == "tan"):
            return math.tan(derece)
        elif(fonk == "cot"):
            return 1/math.tan(derece)
        else:
            print("Hatali fonksiyon girdiniz! (sin,cos,tan,cot fonksiyonlarini girerek tekrar deneyiniz.)")
class hesapMakinesi(basitHesaplama,gelismisHesaplama):
    def anaMenuYazdir(self):
        print("\n*****Hesap Makinesi*****\n")
        print("1.Toplama\n2.Cikarma\n3.Carpma\n4.Bolme\n5.Us Hesaplama\n6.Karakok Alma\n7.Logaritma\n8.Trigonometri\n0.Cikis")
        islemNo = int(input("Yapmak istediginiz islemin sira numarasini giriniz: "))
        return islemNo
    def DegerAl(self, islemNo):
        bh = basitHesaplama()
        gh = gelismisHesaplama()
        if(islemNo < 8):
            birinciSayi = int(input("1.Sayiyi giriniz: "))
            ikinciSayi = int(input("2.Sayiyi giriniz: "))
        elif(islemNo >= 8):
            fonk = input("Fonksiyonu giriniz(sin,cos,tan,cot): ")
            derece = int(input("Dereceyi giriniz: "))
            print(fonk, "(", derece, ")", "=", gh.trigonometriHesapla(fonk, derece))
        else:
            print("Hatali islem numarasi sectiniz! (1,2,3,4,5,6,7,8 numaralarindan birini giriniz.)")
        if(islemNo == 1):
            print(birinciSayi, "+", ikinciSayi, "=", bh.topla(birinciSayi, ikinciSayi))
        elif(islemNo == 2):
            print(birinciSayi, "-", ikinciSayi, "=", bh.cikar(birinciSayi, ikinciSayi))
        elif(islemNo == 3):
            print(birinciSayi, "*", ikinciSayi, "=", bh.carp(birinciSayi, ikinciSayi))
        elif(islemNo == 4):
            print(birinciSayi, "/", ikinciSayi, "=", bh.bol(birinciSayi, ikinciSayi))
        elif(islemNo == 5):
            print(birinciSayi, "^", ikinciSayi, "=", gh.usAl(birinciSayi, ikinciSayi))
        elif(islemNo == 6):
            print(ikinciSayi, ".dereceden √", birinciSayi, "=", gh.karakokAl(birinciSayi, ikinciSayi))
        elif(islemNo == 7):
            print("log", birinciSayi, "(",ikinciSayi, ") =", gh.logAl(ikinciSayi, birinciSayi))
hm = hesapMakinesi()
islemNo = hm.anaMenuYazdir()
while(islemNo != 0):
    hm.DegerAl(islemNo)
    islemNo = hm.anaMenuYazdir()
else:
    exit
