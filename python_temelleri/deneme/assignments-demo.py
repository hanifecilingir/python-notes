x,y,z = 2,5,10

numbers=1,5,7,10,6

#1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
# a=int(input('sayi1:'))
# b=int(input('sayi2:'))
# carpim=a*b
# toplam=x + y+ z 
# sonuc=carpim - toplam
# print(sonuc)

#2- y'nin x'e kalansız bölümünü hesaplayınız.
# print(y//x)

#3- (x,y,z) toplamının mod 3'ü nedir?
# print((x+y+z)%3)

#4- y'nin x.kuvvetini hesaplayınız.
# print(y**x)

#5- x,*y,z = numbers işlemine gire z'nin küpü nedir?
# x,*y,z = numbers
# print(x,y,z)
# print(z**3)

#6- x,*y,z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
x,*y,z=numbers
result=y[0] + y[1] +y[2]
print(result)