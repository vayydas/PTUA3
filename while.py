number = 23
running = True
while running :
    guess = int(input("iveskite sveika skaiciu:"  ))

    if guess == number:
        print("sveikiname, jus atspejote, ")  #naujo bloko pradzia

        running = False #tai stabdo cikla while

     


    elif guess < number :
        print("neteisingai, uzduotas skaiciuc didesni.")    #dar vienas blokas
    #bloko viduje jus galite vykdyti viska...
    else:
        print("uzduotas skaicius yra mazesnis.")
    #kad papulti cia , guess turi buti didesnis nei number
else:

    print("while ciklas baigta")

print("baigta")
