import random
Mots = ["Test" , "Canard" , "Maison","Voiture ","Casque","Café","Informatique","Ordinateur","Cendrier"]

def afficher_mot(mot,lettres_trouvees):
    print("Mot: ", end='' )
    for i in range(len(mot)):
        if mot[i] in lettres_trouvees:
            print(mot[i], end='')
        else:
            print(" _",end='')

        

def mot_trouver(mot,lettres_trouvees):
    for i  in range(len(mot)):
        if mot[i] not in lettres_trouvees:
            return False 
        
    return True    

def main(Mots):
    mot = random.choice(Mots)
    nombres_tentatives = 6
    lettres_trouvees = set()

    while nombres_tentatives > 0:
        afficher_mot(mot,lettres_trouvees)
        print(" Nombre de tentavtes restantes: ",nombres_tentatives)
        lettre = input("Entrez une lettre :")
        if lettre not in mot:
            nombres_tentatives = nombres_tentatives - 1

        if lettre in mot and lettre not in lettres_trouvees:
            lettres_trouvees.add(lettre)

        if mot_trouver(mot , lettres_trouvees):
            print("Le mot a été trouvé ")    
            print(mot)
            break  
        
        
        if nombres_tentatives == 0:
            print("Le mot n'a pas été trouvé") 
            break   
        

main(Mots)