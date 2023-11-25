#1-'Bmw,Mercedes,Opel,Mazda' elemanlarına sahip bir liste oluşturunuz.
list=['Bmw','Mercedes','Opel','Mazda']
print(list)
#2-Liste kaç elemanlıdır
print(len(list))
#3-Listenin ilk ve son elemanı nedir
print(list[0])
print(list[3])
#4-Mazda değerini Toyota ile değiştirin
list[-1]='Toyota'
print(list)
 
#5-Mercedes listenin bir elemanı mıdır
#list='Mercedes' in list
print(list)

#6-Listenin -2 indeksindeki değer nedir
print(list[-2])

#7-Listenin ilk 3 elamanını alın
print(list[0:3])

#8-listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.
list[-2]='Toyota'
list[-1]='Renault'
print(list)
#veya list[-2:]=['Toyota','Renault']

#9-Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin
#list=list + ['Audi','Nissan']
#print(list)

#10-Listenin son elemanını silin
#del list[-1]
#rint(list)

#11-Liste elemanlarını tersten yazdırın
print(list[::-1])

#12-Aşağıdaki verileri bir liste içinde saklayınız.
#studentA: Yiğit Bilgi 2010,(70,60,70)
#studentB: Sena Turan 1999, (80,80,70)
#studentC: Ahmet Turan 1998, (80,70,90)
listX=['Yiğit', 'Bilgi',2010,[70,60,70]]
listY=['Sena', 'Turan',1999,[80,80,70]]
listZ=['Ahmet', 'Turan',1998,[80,70,90]]
numbers=listX + listY + listZ
print(numbers)



#13-Liste elemanlarını ekrana yazdırın.
print(listX[0])
print(listY[1])
print(listZ[3][2])

result=f"{listX[0]} {listX[1]} {2023-listX[2]} yaşında ve not ortalaması {(listX[3][0] + listX[3][1] + listX[3][2])/3 }"
print(result)
