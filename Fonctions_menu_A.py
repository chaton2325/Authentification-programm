import hashlib


#Fonction qui va hacher
def hash_word(mot):
    hash_object = hashlib.sha256(mot.encode())
    hex_dig = hash_object.hexdigest()
    print("Le haché du mot que vous avez entré est : ",hex_dig)






#Fonction qui va permettre l'attaque par dictionnaire
def dict_attack(mot):
    list_dictionnaire=[]
    with open("dictionnaire.txt","r") as fichier2:
        for ligne in fichier2:
            list_dictionnaire.append(ligne)
            

        #on enleve tout les \n de la liste
        list_dictionnaire_1=[element.replace("\n","") for element in list_dictionnaire]
        

        #vérifier si le mot entré est dans le dictionnaire
        if mot in list_dictionnaire_1:
            #Juste pour montrer le professionnalisme , on fait quelque chose 
            a=list_dictionnaire_1.index(mot)
            print("Attaque par dictionnaire reussi , le mot entré est : ",list_dictionnaire_1[a])
        else:
            print("mot non présent dans votre dictionnaire")
