kilo = int(  input("kilonuzu giriniz(kg)") )
boy = float(  input("boyunuz giriniz(mt)")  )
bki = kilo / (boy*boy)
print("boy kilo endeksiniz", bki)
if bki<18.5:
    print("zayıfsınız")
elif bki<25:
    print("sağlıklısınız")
elif bki<30:
    print("az kilolusunuz")
elif bki<35:
    print("1.derece obezsiniz")
elif bki<40:
    print("2.derece obesiniz")
else:
    print("3.derece obezsiniz")
    


