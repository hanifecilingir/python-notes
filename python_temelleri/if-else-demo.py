# 1- Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise ya da üniversite olmalıdır.
# isim = input('İsim:')
# yas= int(input('Yas:'))
# egitim= input('Eğitim Durumunuz:')
# if (yas>=18): 
#     if(egitim == 'lise' or egitim=='üniversite'):
#         print(f'{isim} Ehliyet Alabilirsiniz.')
#     else:
#         print(f'{isim} ehliyet alamazsın egitim durumun yetersiz.')            
# else:
#     print(f'{isim} Ehliyet alamazsın yaşın tutmuyor.')    




# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0-24 => 0
#    25-44=> 1
#    45-54=> 2
#    55-69=> 3
#    70-84=> 4
#    85-100=> 5


# yazili1=int(input('1.Yazili:'))
# yazili2=int(input('2.Yazili:'))
# sozlu=int(input('Sözlü:'))
# ort= (yazili1 + yazili2 + sozlu )/3

# if (0 < ort <= 24) :
#     print(f'ortalamanız:{ort}  Notunuz:0')
# elif (24 < ort <= 44) :
#     print(f'ortalamanız:{ort}  Notunuz:1') 
# elif (44 < ort <= 54) : 
#     print(f'ortalamanız:{ort}  Notunuz:2')   
# elif (54 < ort <= 69) :
#     print(f'ortalamanız:{ort}  Notunuz:3')
# elif (69 < ort <= 84) :
#     print(f'ortalamanız:{ort}  Notunuz:4')
# elif (84 < ort <= 100) :
#     print(f'ortalamanız:{ort}  Notunuz:5')     
# else:
#     print('yanlış bilgi girdiniz.')



# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere 
#    göre hesaplayınız.
#    1.Bakım => 1. yıl 
#    2.Bakım => 2.yıl
#    3.Bakım => 3.yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    ***datetime modülünü kullanmanız gerekiyor.
#    (simdi) - (2018/8/1) =>gün 
import datetime 
tarih =input('aracınız hangi trafikte trafiğe çıktı (2019/8/9):')
tarih= tarih.split('/')
trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi -  trafigecikis
days = fark.days

if (days <= 365):
    print('1.Servis aralığı')
elif days >365 and days <=365*2:
    print('2. Servis aralığı')
elif days >365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('hatalı süre.')    