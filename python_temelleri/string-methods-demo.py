website='http://www.sadikturan.com'
course='Python Kursu:Baştan Sona Python Programlama Rehberiniz (40 saat)'


#1-' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
# message=' Hello World '
# message=message.strip()
# print(message)

#2-'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
# result='www.sadikturan.com'.strip('w.moc')
# print(result)


#3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
# course=course.lower()
# print(course)


#4-'website' içinde kaç tane a karakteri vardır? (count('a'))
# website=website.count('a')
# print(website)


#5-'website' www ile başlayıp com ile bitiyor mu
#website=website.startswith('www')
# website=website.endswith('com')
# print(website)


#6-'website' içinde '.com' ifadesi var mı
# result=website.find('.com')
# print(result)

#7-'course' içindeki karakterlerin hepsi alfabetik mi?
# result=course.isalpha()
# result='Hello'.isalpha()
# result=course.isdigit()
# result='123'.isdigit()
# print(result)


#8-'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
# result='Contents'.center(50,'*')
# print(result)

#9-'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
# course=course.replace(' ','-')
#course=course.replace(' ','')    #aradaki boşluk karakterlerini siler
# course=course.replace(' ','-',5)  #ilk 5 boşluğa çizgi koyar
# print(course)

#10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
# result='Hello World'.replace('World','There')
# print(result)


#11-'course' karakter dizisini boşluk karakterlerinden ayırın.
# course=course.split(' ')
# print(course)

