kilo = int(  input("kilonuzu giriniz(kg)") )
boy = float(  input("boyunuz giriniz(mt)")  )
bki = kilo / (boy*boy)
hedef1 = (18.5*boy*boy) - kilo
hedef2 = kilo - (25*boy*boy)
print("boy kilo endeksiniz", bki)
if bki<18.5:
    print("zayıfsınız")
    print("sağlıklı olmak için ", hedef1, "kilo almalısınız")
elif bki<25:
    print("sağlıklısınız")
elif bki<30:
    print("az kilolusunuz")
    print("sağlıklı olmak için ", hedef2, "kilo vermelisiniz")
elif bki<35:
    print("1.derece obezsiniz")
    print("sağlıklı olmak için ", hedef2, "kilo vermelisiniz")
elif bki<40:
    print("2.derece obesiniz")
    print("sağlıklı olmak için ", hedef2, "kilo vermelisiniz")
else:
    print("3.derece obezsiniz")
    print("sağlıklı olmak için ", hedef2, "kilo vermelisiniz")
    