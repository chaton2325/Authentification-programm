#Fonction principale du programme

import re
import string
import random
from colorama import Fore, Back, init, Style
import hashlib
import maskpass
from Fonctions import Menu
init()


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
var="False"
email=""
def isValid(email):
    global var
    if re.fullmatch(regex, email):
        print("Valid email\n")
        var="True"
    else:
        print("\n") 



def mdp():
    global email
    #Ajout a la base de données
    def Ajout_base(email,password):
        hash_object = hashlib.sha256(password.encode())
        hex_dig = hash_object.hexdigest()
        with open("Enregistrement.txt",'a') as fichier:
            contenu_a_ajouter=f"\n{email} {hex_dig}"
            fichier.write(contenu_a_ajouter)
        print("Ajout a la base de donnée avec succès")
        while True:
            decision=int(input("\nEntrez 1 pour vous authentifier et 2 pour quitter"))
            if decision==1:
                authentification()
                break
            elif decision==2:
                print("Merci de vous etre enregistrer")
                break
            else:
                print("Entrez 1 ou 2\n")
        

    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    special=string.punctuation
    number=string.digits
    password=""
    while True:
        choix=int(input(Fore.GREEN + "choissisez une option , 1 ou 2\n1)génération automatique du mot de passe\n2)génération manuelle (mot de passe compris entre 6 et 8 caractères )\n "))
        if choix==1:
            while len(password)<8:
                u1=random.choice(upper)
                l1=random.choice(lower)
                s1=random.choice(special)
                n1=random.choice(number)
                password+=f"{u1}"
                password+=f"{l1}"
                password+=f"{s1}"
                password+=f"{n1}"
            l=[]
            for i in password:
                l.append(i)
            random.shuffle(l)
            pass_melanger="".join(l)
            print("Votre email est : ",email,"\nle mot de passe automatique est :",pass_melanger)
            password=pass_melanger
            Ajout_base(email,password)
            break
        elif choix==2:
            def verify_password():
                global connect
                while True:
                    l1=[]
                    l2=[]
                    l3=[]
                    l4=[]
                    print("entrez un mot de passe\nindications:\tminimum 6 caracteres\n\t,doit contenir des lettres majuscules\n\t,minuscules et caractere speciaux\n")
                    password=maskpass.askpass()
                    if len(password)>=8:
                        #VERIFIER SI IL YA UN UPPERCASE
                        for j in upper:
                            if j in password:
                                l1.append(j)
                        #verifier s'il y'a un lowercase
                        for k in lower:
                            if k in password:
                                l2.append(k)
                        #verifier s'il y'a un caractere special
                        for m in special:
                            if m in password:
                                l3.append(m)
                        for n in number:
                            if n in password:
                                l4.append(m)
                        

                        #On procede aux verifications si le mot de passe saisi manuellemnt est correct 

                        if len(l1)==0 and len(l2)==0 and len(l3)==0 and len(l4)==0:
                            print(Back.RED + "votre mot de passe n'a ni de majuscule ni de minuscule ni de caractere special ni de nombres\n")
                            verify_password()
                        elif len(l1)==0 and len(l2)>0 and len(l3)==0 and len(l4)>0:
                            print(Back.RED + "Votre mot de passe ne contient ni majuscule ni caractere special , reessayer\n")
                            verify_password()
                        elif len(l1)>0 and len(l2)==0 and len(l3)==0 and len(l4)>0:
                            print(Back.RED + "votre mot de passe ne contient ni minuscule ni caractere special , reessayer\n")
                            verify_password()
                        elif len(l1)==0 and len(l2)==0 and len(l3)>0 and len(l4)>0:
                            print(Back.RED + "votre mot de passe ne contient pas de majuscule ni de minuscule , reessayer\n")
                            verify_password()
                        elif len(l1)>0 and len(l2)>0 and len(l3)==0 and len(l4)>0:
                            print(Back.RED + "Votre mot de passe ne contient pas de caractere spécial , reessayer\n")
                            verify_password()
                        elif len(l1)==0 and len(l2)>0 and len(l3)>0 and len(l4)>0:
                            print(Back.RED + "votre mot de passe ne contient pas de majuscules , reesayer\n")
                            verify_password()
                        elif len(l1)>0 and len(l2)==0 and len(l3)>0 and len(l4)>0:
                            print(Back.RED + "votre mot de passe ne contient pas de minuscules , réessayer\n")
                            verify_password()
                        elif len(l1)==0 and len(l2)==0 and len(l3)==0 and len(l4)>0:
                            print("Votre mot de passe ne contient ni majuscules , ni minuscules , ni caractere special , réessayer")
                            verify_password()
                        elif len(l1)>0 and len(l2)==0 and len(l3)>0 and len(l4)==0:
                            print("votre mot de passe ne contient ni minuscule,ni nombre, réessayer \n")
                            verify_password()
                        elif len(l1)==0 and len(l2)>0 and len(l3)>0 and len(l4)==0:
                            print("Votre mot de passe ne contient ni de majuscule ni de nombres, réessayer \n")
                            verify_password()
                        elif len(l1)>0 and len(l2)>0 and len(l3)==0 and len(l4)==0:
                            print("votre mot de passe ne contient ni caractere spécial ni nombre, réessayer \n")
                            verify_password()
                        elif len(l1)==0 and len(l2)==0 and len(l3)>0 and len(l4)==0:
                            print("Votre mot de passe ne contient ni majuscules , ni minuscule,ni nombres réesayer\n")
                            verify_password()
                        elif len(l1)>0 and len(l2)==0 and len(l3)==0 and len(l4)==0:
                            print("Votre mot de passe ne contient ni de minuscule ni caractere special , ni de nombres , réessayer\n")
                            verify_password()
                        elif len(l1)==0 and len(l2)>0 and len(l3)==0 and len(l4)==0:
                            print("Votre mot de passe ne contient ni de majuscule , ni de caractere spécial ni de nombres\n")
                            verify_password()
                        elif len(l1)>0 and len(l2)>0 and len(l3)>0 and len(l4)==0:
                            print("Votre mot de passe ne contient pas de nombres , réessayer\n")
                            verify_password()
                        
                        else:
                            print(Fore.YELLOW + "\tvotre mot de passe est: ",password,"\n\tet votre email est: ",email)
                            Ajout_base(email,password)
                            


                        break

                    else:
                        print(Fore.RED + "entrez un mot de passe de longueur 8 minimum: ")
            verify_password()

            break
        else:
            print("choix incorrect , réessayer\n\n")


#La fonction pour vérifier si
def choice(): 
    global email       
    while True:
        email=input(Fore.RED + "entrez votre email: ")
        isValid(email)
        if var=="True":
            mdp()
            break
        else:
            print("format d'email incorrect")
    



print(Style.RESET_ALL)


#La fonction pour authentifier 
def authentification():
    global global_connect
    list_user=[]
    print("Bienvenu sur la phase d'authentification\n")
    email=input("entrez votre email: ")
    passwords=input("entrez votre mot de passe: ")

    #recuperer tout les identifiants
    with open("Enregistrement.txt","r") as fichier:
        for ligne in fichier:
            mot=ligne.split()
            mots=tuple(mot)
            list_user.append(mots)
    hash_object = hashlib.sha256(passwords.encode())
    hex_dig = hash_object.hexdigest()
    lv=[]
    for i in list_user:
        emails , passw = i
        if email==emails and passw==hex_dig:
            print("bienvenu utilisateur")
            lv.append("V")
            Menu()
    if lv==[]:
        print("identifiant non trouvé")
        while True:
            choix=int(input("Entrez 1 pour enregistrer un nouvel utilisateur et 2 pour quitter: "))
            if choix==1:
                choice()
                break
            elif choix==2:
                print("Merci d'etre passé")
                break
            else:
                print("Entrez 1 ou 2 \n")

authentification()

        