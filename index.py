#Importation du module randint pour généré un nombre
from random import randint

#stockage du nombre généré dans une variable
number_generate = randint(1,1000)

#Défini notre nombre de tentative
tentative = 7

while tentative > 0:
    choix = int(input("Veuillez choisir un nombre : "))
    
    if choix == number_generate:
        print("\nC'est Gagné !!\n")
        break
        
    elif choix > number_generate:
        print("\nC'est Moins !\n")
        tentative -= 1
        
    elif choix < number_generate:
        print("\nC'est Plus !\n")
        tentative -= 1

print("\nFIN DU JEUX !")
if tentative == 0:
    print("Dommage c'étais " + str(number_generate))
