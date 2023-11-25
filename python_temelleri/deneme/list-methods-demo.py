names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

#1- "Cenk" ismini listenin sonuna ekleyin.
# names=names + ['Cenk']
# print(names)
# names.append('Cenk')
#2- "Sena" değerini listenin başına ekleyin.
# names=['Sena'] + names
# print(names)
# names.insert(0,'Sena')

#3- "Deniz" ismini listeden siliniz.
# del names[-1]
# print(names)
# names.remove('Deniz')

#4- "Deniz" isminin indeks nedir?
index=names.index('Deniz')
print(index)

#5- "Ali" listenin bir elemanı mıdır?
# names='Ali' in names
# print(names)

#6- Liste elemanlarını ters çevirin.
# print(names[::-1])
# print(years[::-1])
# names.reverse()
# print(names)
 
#7- Liste  elemanlarını alfabetik olarak sıralayın.
# names.sort()
# print(names)

#8- years listesini rakamsal büyüklüğe göre sıralayınız.
# years.sort()
# print(years)

#9- str="Chevrolet,Dacia" karakter dizisini listeye çevriniz.

# list=['Chevrolet','Dacia']
# print(list)
# str= "Chevrolet,Dacia"
# result=str.split(',')    #virgülden ayrılarak liste olsun diyor.

#10- years dizisinin en büyük ve en küçük elemanı nedir?
# x=max(years)
# print(x)
# y=min(years)
# print(y)
# print(max(years))
# print(min(years))

#11- years dizisinde kaç tane 1998 değeri vardır?
# print(years.count(1998))

#12- years dizisinin tüm elemanlarını silin.
# years.clear()
# print(years)

#13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar=[]
marka= input("marka:")
markalar.append(marka)
marka= input("marka:")
markalar.append(marka)
marka= input("marka:")
markalar.append(marka)
print(markalar)