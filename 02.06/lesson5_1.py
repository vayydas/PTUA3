#W#e have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
#Create one final dictionary from all those 3.

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
#You can use input to receive the number. Example:
#



#dic_one = {1:10, 2:20}
#dic_two = {3:30, 4:40}
#dic_three = {5:50,6:60}


#dic_one.update(dic_two)
#dic_one.update(dic_three)
#print(dic_one)


print("iveskite staciojo trikampio informacija")
statmuo1=float(input("ilgis1:  "))
statmuo2=float(input("ilgis2:  "))
izambine=((statmuo1**2+statmuo2**2)**0.5)
perimetras=(statmuo1+statmuo2+izambine)
plotas=((statmuo1*statmuo2)/2)
print("izambine=  ",izambine)
print("perimetras=  ",perimetras)
print("plotas=  ",plotas)






