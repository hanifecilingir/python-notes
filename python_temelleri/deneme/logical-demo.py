# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# a=int(input('Sayi:'))
# result= (a>0 and a<100)
# print(result)


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# a=int(input('Sayi:'))
# result= ((a>0) and (a % 2==0))
# print(result)


# 3- Email ve parola bilgilerini ile giriş kontrolü yapınız.
# email='hnfclngr@gmail.com'
# parola='asd123'
# girilenparola=input('Sifreniz:')
# girilenemail=input('Email:')
# result=(girilenemail==email) and (girilenparola==parola)

# print(f'uygulamaya giriş başarılı mı:{result}')


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# a=int(input('1.sayi:'))
# b=int(input('2.Sayi:'))
# c=int(input('3.Sayi:'))

# result=(a>b) and (a>c)
# print(f'a en büyük sayıdır:{result}')

# result=(b>a) and (b>c)
# print(f'b en büyük sayıdır:{result}')

# result=(c>a) and (c>b)
# print(f'c en büyük sayıdır:{result}')


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# vize1=float(input('vize1:'))
# vize2=float(input('vize2:'))
# final=float(input('final:'))

# ort=(((vize1+vize2)/2)*0.6 + final*0.4)
# # result=(ort>=50) and (final>=50)
# result=(ort>=50) or (final>=70)
# print(f'Ortalamanız:{ort} ve dersten geçme durumunuz:{result}')



# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül:(Kilo/boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4      =>Zayıf
#    18.5-24.9   =>Normal
#    25.0-29.9   =>Fazla Kilolu
#    30.0-34.9   =>Şişman(Obez)
name=(input('Adı:'))
kg=float(input('Kilo:'))
hg=float(input('Boy:'))
indeks=((kg)/(hg**2))
zayıf=(indeks>=0 and (indeks<=18.4))
normal=(indeks>18.4) and (indeks<=24.9)
fazlakilolu=(indeks>24.9) and (indeks<=29.9)
obez=(indeks>29.9) and (indeks<=34.9)

print(f'{name} kilo indeksin:{indeks} ve kilo değerlendirmen zayıf:{zayıf}')
print(f'{name} kilo indeksin:{indeks} ve kilo değerlendirmen normal:{normal}')
print(f'{name} kilo indeksin:{indeks} ve kilo değerlendirmen fazlakilolu:{fazlakilolu}')
print(f'{name} kilo indeksin:{indeks} ve kilo değerlendirmen obez:{obez}')