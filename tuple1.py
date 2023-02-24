
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)        # ('apple', 'banana', 'cherry')



# thistuple = ("apple",)
# print(type(thistuple))      # <class 'tuple'>

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))      # <class 'str'>


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])        # cherry




# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])       # ('cherry', 'orange', 'kiwi')

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included



# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")



# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)        # ('apple', 'kiwi', 'cherry')



# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)        #('apple', 'banana', 'cherry', 'orange')



# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)        # ('apple', 'banana', 'cherry', 'orange')



# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# print(thistuple)        # ('banana', 'cherry')



# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)         #this will raise an error because the tuple no longer exists



# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)            # apple
# print(yellow)           # banana
# print(red)              # cherry




# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)              # apple
# print(yellow)             # banana
# print(red)                # ['cherry', 'strawberry', 'raspberry']



# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)                # apple
                            # banana
                            # cherry



# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])     # apple
                            # banana
                            # cherry




# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1                 # apple
                            # banana
                            # cherry




# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)              # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')




# Buch1 = "William Shakespeare", "Hamlet", 4223, 12.99
# Buch2 = "Friedrich Schiller", "Die Räuber", 3229, 5.49 
# Buch3 = "Johann Wolfgang von Goethe", "Faust", 5444, 9.99
# print(Buch1[0]) 
# print(Buch1[1]) 
# print(Buch1[2]) 
# print(Buch1[3], "\n")
# print(Buch2[0]) 
# print(Buch2[1]) 
# print(Buch2[2]) 
# print(Buch2[3], "\n")
# print(Buch3[0]) 
# print(Buch3[1]) 
# print(Buch3[2]) 
# print(Buch3[3], "\n")






# Buch1 = {"Autor":"William Shakespeare", "Titel":"Hamlet",
# "Artikelnr.":4223, "Preis:":12.99}
# Buch2 = {"Autor":"Friedrich Schiller", "Titel":"Die Räuber",
# "Artikelnr.":3229, "Preis:":5.49}
# Buch3 = {"Autor":"Johann Wolfgang von Goethe", "Titel":"Faust",
# "Artikelnr.":5444, "Preis:":9.99}
# print(Buch1["Autor"])
# print(Buch1["Titel"]) 
# print(Buch1["Artikelnr."]) 
# print(Buch1["Preis:"], "\n")
# print(Buch2["Autor"])
# print(Buch2["Titel"]) 
# print(Buch2["Artikelnr."]) 
# print(Buch2["Preis:"], "\n")
# print(Buch3["Autor"]) 
# print(Buch3["Titel"]) 
# print(Buch3["Artikelnr."])
# print(Buch3["Preis:"], "\n")




# a = eval(input("Geben Sie bitte den Warenbestand ein: ")) 
# if a >= 100: 
#     print("Warnung: Keine Lagerkapazitäten mehr frei!")
# elif a >= 10:
#     print("Die Warenbestände liegen bei", a,"Artikeln.") 
# elif a > 0: 
#     print("Nur noch ", a, "Artikel vorrätig. Bitte nachbestellen!") 
# elif a == 0:
#     print("Warnung: Artikel nicht mehr verfügbar!")
# else:     
#     print("Ungültige Eingabe!")


fahrzeug1 = ["VW", "Golf", 2011, 5000] 
fahrzeug2 = ["Renault", "Clio", 2013, 6000] 
fahrzeug3 = ["Porsche", "Panamera", 2014, 25000] 
listeFahrzeuge = [fahrzeug1, fahrzeug2, fahrzeug3] 
maxpreis = eval(input("Geben Sie bitte den Maximalpreis ein: "))
if listeFahrzeuge[0][3] <= maxpreis:
  print ("Marke: ",listeFahrzeuge[0][0]) 
  print ("Modell: ",listeFahrzeuge[0][1]) 
  print ("Baujahr: ",listeFahrzeuge[0][2]) 
  print ("Preis: ",listeFahrzeuge[0][3], "\n")
if listeFahrzeuge[1][3] <= maxpreis:
  print ("Marke: ",listeFahrzeuge[1][0]) 
  print ("Modell: ",listeFahrzeuge[1][1]) 
  print ("Baujahr: ",listeFahrzeuge[1][2]) 
  print ("Preis: ",listeFahrzeuge[1][3], "\n")
if listeFahrzeuge[2][3] <= maxpreis:
  print ("Marke: ",listeFahrzeuge[2][0]) 
  print ("Modell: ",listeFahrzeuge[2][1]) 
  print ("Baujahr: ",listeFahrzeuge[2][2]) 
  print ("Preis: ",listeFahrzeuge[2][3], "\n")