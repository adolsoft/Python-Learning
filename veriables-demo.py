"""
1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
Müşteri adı
Müşteri soyadı
Müşteri ad + soyad
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı
"""
musteriAdi = 'Ali'
musteriSoyad = 'Yılmaz'
musteriAdSoyad = musteriAdi + ' ' + musteriSoyad
musteriCinsiyet = True #Erke olsun
musteriTcKimlik = '12345678910'
musteriDogumYili = 1989
musteriAdres = 'İstanbul Kadiköy'
musteriYasi = 2024 - musteriDogumYili

print(musteriYasi)

# Siparis Toplam bilgisi hesaplama

order1 = 110 
order2 = 1100.5
order3 = 356.95
total = order1 + order2+ order3
print("Toplam =", total)