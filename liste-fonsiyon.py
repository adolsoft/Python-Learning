def sepet_toplam_fiyati(urun_adetleri, urun_fiyatlari):
  """
  Bir alışveriş sepetindeki ürünlerin toplam fiyatını hesaplar.

  Args:
    urun_adetleri: Sepetteki her bir ürünün adedini tutan liste.
    urun_fiyatlari: Her bir ürünün fiyatını tutan liste.

  Returns:
    Sepetin toplam fiyatı.
  """

  toplam_fiyat = 0
  for i in range(len(urun_adetleri)):
    toplam_fiyat += urun_adetleri[i] * urun_fiyatlari[i]
  return toplam_fiyat

# Örnek kullanım:
urunler = [2, 3, 1]  # 2 elma, 3 muz, 1 ananas
fiyatlar = [5, 2, 10]  # Elma 5 TL, muz 2 TL, ananas 10 TL

sonuc = sepet_toplam_fiyati(urunler, fiyatlar)
print("Sepetin toplam fiyatı:", sonuc, "TL")