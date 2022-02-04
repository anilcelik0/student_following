def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    adsoyad = liste[0]
    notlar = liste[1].split(',')
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ort = (not1+not2+not3)/3
    if ort >= 50:
        harf = 'geçti'
    else:
        harf = 'kaldı'
    ort = str(ort)
    return adsoyad+': '+ort+' '+harf+'\n'


def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
    

def notlari_gir():
    ad = input('öğrenci adı: ')
    soyad = input('öğrenci soyadı: ')
    not1 = input('not 1 : ')
    not2 = input('not 2 : ')
    not3 = input('not 3 : ')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')

def not_kayit():
    with open('sinav_notlari.txt','r',encoding='utf-8') as file:
        liste = []
        for a in file:
            liste.append(not_hesapla(a))
            with open('sonuclar.txt','w',encoding='utf-8') as file2:
                for i in liste:
                    file2.write(i)


        


while True:
    menu = int(input('1- Notları oku\n2- Notları gir\n3- Notları kayıt et\n4- çıkış\n'))

    if menu == 1:
        notlari_oku()

    elif menu == 2:
        notlari_gir()

    elif menu == 3:
        not_kayit()

    else:
        break