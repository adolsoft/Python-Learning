def crypter(texte, cle):
  """
  Verilen bir metni, belirtilen bir anahtar ile Caesar şifrelemesi yöntemiyle şifreler.

  Args:
    texte: Şifrelenecek metin.
    cle: Şifreleme için kullanılacak anahtar (kaydırma miktarı).

  Returns:
    Şifrelenmiş metin.
  """

  texte_crypte = ""
  for caractere in texte:
    if caractere.isalpha(): # 
      # Büyük veya küçük harf olup olmadığına göre işlem yapar
      print("Karakter "+ caractere)
      if caractere.isupper():
        # Büyük harfler için şifreleme
        texte_crypte += chr((ord(caractere) - ord('A') + cle) % 26 + ord('A'))
        #print(texte_crypte + " " + str((ord(caractere) - ord('a') + cle) % 26 + ord('a'))) 
      else:
        # Küçük harfler için şifreleme
        texte_crypte += chr((ord(caractere) - ord('a') + cle) % 26 + ord('a'))
        #print(texte_crypte + " " + str((ord(caractere) - ord('a') + cle) % 26 + ord('a')))
        
    else:
      # Harf olmayan karakterler olduğu gibi eklenir
      texte_crypte += caractere
      print(texte_crypte)
  return texte_crypte

def decrypter(texte_crypte, cle):
  """
  Verilen bir şifreli metni, belirtilen anahtar ile Caesar şifrelemesinin tersini uygulayarak deşifre eder.

  Args:
    texte_crypte: Şifrelenmiş metin.
    cle: Şifrelemede kullanılan anahtar.

  Returns:
    Deşifre edilmiş metin.
  """

  return crypter(texte_crypte, -cle)

sifrenecek_metin = input("Entrez le mot de passe :") # Sifrenecek Kelime Gir 
anahtar_sayi_gir = input("Entrer le numéro de clé :") # Sifrenecek Kelime Gir 
sifreli_metin = crypter(sifrenecek_metin, int(anahtar_sayi_gir))
cozulmuz_metin = decrypter(sifreli_metin,  int(anahtar_sayi_gir))

print(sifreli_metin)
print(cozulmuz_metin)