ad='yunus'
soyad='erzurum'
yas=20

greeting='Merhaba benim adım  '+ad+' soyadım '+soyad+' ve ben \nI  '+str(yas)+' 20 yaşındayım.' #str yi silip deneyiniz
lenght=len(greeting)

#print(greeting) yazımızı greetinge atadık 
print(greeting[0]) # yazımızdaki 1. değeri göstermesi sagladık yani 'M' değerini gösterdik.
print(greeting[1]) # yazımızdaki 2. değeri göstermesi sagladık yani 'e' değerini gösterdik.
print(lenght)# yazımızdaki toplam karakter sayımız 70
print(greeting[lenght-1]) # en sondaki karakteri görmek için kullanırız.