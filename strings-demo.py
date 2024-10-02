website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1-' course' karakter dizisinde kaç karakter bulunmaktadır ?
#result = len(course)
#print(result)

# 'course' ifadesindeki karakterleri tersten yazdırın.
# result = course[::] # bütün ifade olduğu gibi yazdırılır
# result = course[::-1]

# name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# result = "Benim adım "+ name+ " "+surname+"Yaşım "+str(age)+" ve Mesleğim "+ job # bu zor bunun yerine
# result = "Benim adım {} {}, Yaşım {} ve mesleğim {}. ".format(name,surname,age,job)
# result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."


# Hello word ifadesi W ile değiştirelim
#s='Hello word'
#s.replace("")

# s= '12345'*5
# print(s[::5]) ## sonuz 11111 çıkar

# # 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '.strip() # Boşlık karakteri silerek yapar.
# result = ' Hello World '.strip() # Boşlık karakteri silerek yapar.
# result = ' Hello World '.lstrip() # sadece soldan Boşlık karakteri silerek yapar.
# result = ' Hello World '.rstrip() # sadece sadan Boşlık karakteri silerek yapar.

# result = website.lstrip('/:pth') # burada soldan  /:pth  karakterlerini siler

## 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
# result = 'www.sadikturan.com'.strip('w.moc') # sağdan ve soldan bütün w.moc karakterşeri siler

# # 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
# result = course.lower() # küçük harfe ceviri
# result = course.upper() # bütün harfler büyük
# result = course.title() # sadece baş harfeleri büyük olur

# # 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
# result = website.count('a') # kaç tane a karakteri var sayar
# result = website.count('www')
# result = website.count('www',0,10) # 0 ve 10 karakter arasında arma yapar

# # 5- 'website' "www" ile başlayıp com ile bitiyor mu?
# result = website.startswith('www') # www ile başlıyormu
# result = website.startswith('http') # 
# result = website.endswith('com') # com ile mi bitiyormu

# # 6-  'website' içinde '.com' ifadesi var mı?
# result = website.find('com') # varsa index  numarasını gönderir. 
# result = website.find('com',0,10)
# result = course.find('Python')
# result = course.rfind('Python') # sağ taraftan saymaya başlar.

# result = website.index('com')
# result = website.rindex('com')
# # result = website.rindex('comm') # exception

# # 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
# result = course.isalpha()
# result = 'Hello'.isalpha()
# result = course.isdigit()
# result = '123'.isdigit()

# # 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
# result = 'Contents'.center(50, '*')
# result = 'Contents'.ljust(50, '*')
# result = 'Contents'.rjust(50, '*')

# # 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
# result = course.replace(' ', '-')
# result = course.replace(' ', '-',5)
# result = course.replace(' ', '')

# # 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
# result = 'Hello World'.replace('World','There')

# # 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
# result = course.split(' ')
# # result = result[2]
# result = result[5]

print(result)   