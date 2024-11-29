# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
Cars=["Toyota","Bmw","Renault","Mercedes"]
# 2- Liste kaç elemanlıdır?
#Liste 4 elemanlıdır
# 3- Listenin ilk ve son elemanı nedir?
#Listenin ilk elemanı "Toyota",son elemanı "Mercedes"
# 4- "Renault" markasını "Togg" ile güncelleyiniz.
Cars[2]="Togg"
# 5- "Togg" listenin bir elemanı mıdır?
#Güncelledikten sonra listenin elemanı olmuştur.
# 6- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
Cars=Cars+["Ford","Citroen"]
# 7- Listenin son elemanını siliniz.
length=len(Cars)
del Cars[length-1]
# 8- Aşağıdaki verileri liste içerisinde saklayınız (Liste içinde liste mümkündür.).
ogrenci1=["Yiğit","Bilgi",2010,70,80,90]
ogrenci2=["Ada","Bilgi",2011,70,70,80]
ogrenci3=["Çınar","Turan",2017,60,60,90]
    #ogrenci1: Yiğit Bilgi 2010 [70,80,90]
    #ogrenci2: Ada Bilgi   2011 [70,70,80]
    #ogrenci3: Çınar Turan 2017 [60,60,90]

# 9- Öğrencilerin yaşlarını hesaplayınız.
print("İlk öğrenci:"+ogrenci1[0]+" "+ogrenci1[1]+"\n"+"Yaşı:"+str(2024-ogrenci1[2]))
print("İkinci öğrenci:"+ogrenci2[0]+" "+ogrenci2[1]+"\n"+"Yaşı:"+str(2024-ogrenci2[2]))
print("Üçüncü öğrenci:"+ogrenci3[0]+" "+ogrenci3[1]+"\n"+"Yaşı:"+str(2024-ogrenci3[2]))
# 11- Öğrencilerin not ortalamalarını hesaplayınız.
print("İlk öğrenci:"+ogrenci1[0]+" "+ogrenci1[1]+"\n"+"Ortalama:"+str((ogrenci1[3]+ogrenci1[4]+ogrenci1[5])/3))
print("İkinci öğrenci:"+ogrenci2[0]+" "+ogrenci2[1]+"\n"+"Ortalama:"+str((ogrenci2[3]+ogrenci2[4]+ogrenci2[5])/3))
print("Üçüncü öğrenci:"+ogrenci3[0]+" "+ogrenci3[1]+"\n"+"Ortalama:"+str((ogrenci3[3]+ogrenci3[5]+ogrenci3[5])/3))

