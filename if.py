number = 23
guess = int(input("iveskite sveika skaiciu:"  ))

if guess == number:
    print("sveikiname, jus atspejote, ")  #naujo bloko pradzia

    print("(nors nieko ir nelaimejote)",)   #bloko pabaiga


elif guess < number :
    print("neteisingai, uzduotas skaiciuc didesni.")    #dar vienas blokas
    #bloko viduje jus galite vykdyti viska...
else:
    print("uzduotas skaicius yra mazesnis.")
    #kad papulti cia , guess turi buti didesnis nei number

print("baigta")


