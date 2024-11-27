# Bankamatik uygulaması

SadikHesap = {
    'ad': 'Sadik Turan',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '98345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranizi alabilirisiniz.')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanilsin mi? (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0 
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranizi alabilirisiniz')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır ")

        else:
            print('üzgünüm bakiyeniz yetmiyor')
    
        print("")

paraCek(SadikHesap, 3000)
paraCek(SadikHesap, 2000)