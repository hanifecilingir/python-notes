website='http://www.sadikturan.com'
course='Python Kursu:Baştan Sona Python Programlama Rehberiniz (40 saat)'
length=len(website)
#1-'course' karakter dizisinde kaç karakter bulunmaktadır.
print(len(course))

#2-'website' içinden www karakterlerini alın.
print(website[7:10])

#3-'website' içinden com karakterlerini alın
print(website[22:25])
print(website[length-3:length])

#4-'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[:15])
print(course[-15:])


#5-'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])


name,surname,age,job ='Bora','Yılmaz',32,'mühendis'

#6-Ekrana 'Benim Adım Bora Yılmaz,Yaşım 32 ve mesleğim mühendis.' ifadesini yazdırın.
print('Benim adım {} {},yaşım {} ve meslegim {}.'.format(name,surname,age,job))

#7-'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s='Hello world'
s=s[0:6]+ 'W'+ s[-4:]
print(s)


#8-'abc' ifadesini yan yana 3 defa yazdırın.
print('abc'*3)





