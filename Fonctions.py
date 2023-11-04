from Fonctions_menu_A import hash_word , dict_attack
from Fonctions_MenuB import CESAR_ASCII , CESAR_key , decipher_CESAR_ASCII , decipher_CESAR_26_letters
from Fonctions_menu_C import Courbe_dataset , dict_dataset

#Menu en cas d'identifiants trouvé dans le fichier texte

def Menu():
    print("A- Donnez un mot a haché (Celui si sera en mode invisible)\n\ta- Haché le mot par sha256\n\tb- Attaquer par dictionnaire le mot inséré\n\td- Revenir au menu principal\nB- Décalage par CESAR\n\ta- Donnez un mot à chiffrer\n\t\t1- Cesar avec code ASCII\n\t\t2- Cesar dans les 26 lettres\n\tb- Chiffrer le message (a)\n\tc- Déchiffrer le message (b)\n\td- Revenir au menu principal\nC- Collecter une Dataset de votre choix\n\ta- Affichez le Dataset sous forme de dictionnaire\n\tb- Afficher des courbes de votre choix\n\tc- Revenir au menu principal  ")
    while True:
        valeur=input("Entrez une lettre entre A,B,C : ")
        if valeur=="A":
            sub_Menu_A()
            break
        elif valeur=="B":
            sub_Menu_B()
            break
        elif valeur=="C":
            sub_menu_C()
            break
        else:
            print("\nMauvais choix , entrez entre A , B et C")


   


#Fonction qui va gérer le sous menu A  
def sub_Menu_A():
    import getpass
    import hashlib
    mot=getpass.getpass("A- Donnez un mot a haché (Celui ci est en mode invisible)")
    print(f"Votre mot est : {mot}")
    while True:
        choix=input("\ta- haché le mot par sha256\n\tb- Attaquer par dictionnaire le mot inséré\n\tc-Revenir au menu principal: ")
        if choix=="a":
            hash_word(mot)
            while True:
                decise=int(input("Entrez 1 pour quitter et 2 pour aller au menu principal: "))
                if decise==1:
                    print("Vous avez quitter \n")
                    break
                elif decise==2:
                    Menu()
                    break
                else:
                    print("\nEntrez 1 ou 2")
            break
        elif choix=="b":
            dict_attack(mot)
            while True:
                decise=int(input("Entrez 1 pour quitter et 2 pour aller au menu principal: "))
                if decise==1:
                    print("Vous avez quitter \n")
                    break
                elif decise==2:
                    Menu()
                    break
                else:
                    print("\nEntrez 1 ou 2")
            break
        elif choix=="c":
            Menu()
            break
        else:
            print("Mauvais choix , réessayer \n")

#Fonction qui va gérer le sous menu B
def sub_Menu_B():
    print("B- Décallage césar ")
    choix1=input("\ta- Donnez un mot a chiffrer : ")
    print("\t\t1- César avec code ASCII\n\t\t2- César dans les 26 lettres")

    #On vérifie que la clé est entre 1 et 26
    while True:
        key=int(input("entrez la clé Entre 1 et 26 (Un entier Pour le chiffrement CESAR): "))
        if key>0 and key<27:
            break
        else:
            print("\nMauvaise clé , réessayer\n")

    while True:
        sub_choix=input("\tb- Chiffrer le message (a): ")
        if sub_choix=="b":
            CESAR_ASCII(choix1,key)
            CESAR_key(choix1,key)
            while True:
                sub=input("Entrez 'c' pour déchiffrer le message en (b) et 'c' pour retourner au menu principal: ")
                if sub=="c":
                    decipher_CESAR_ASCII(key)
                    decipher_CESAR_26_letters(key)
                    while True:
                        decise=int(input("\nEntrez 1 pour quitter et 2 pour aller au menu principal: "))
                        if decise==1:
                            print("Vous avez quitter \n")
                            break
                        elif decise==2:
                            Menu()
                            break
                        else:
                            print("\nEntrez 1 ou 2")
                    break
                elif sub=="d":
                    Menu()
                    break
                else:
                    print("Mauvais choix , réessayer entre 'c' et 'd'\n ")
            break
        else:
            print("Entrez un choix correct (b) \n")
    
    


    choix2=("\tb- Chiffrer le message (a)\nc- Déchiffrer le message (b) ")


#Fonction qui va gérer le sous menu C
def sub_menu_C():
    print("\nC- Collecter une Dataset de votre choix ")
    print("\n\ta- Affichez le Dataset sous forme de dictionnaire\n\tb- Afficher des courbes de votre choix\n\tc- Revenir au menu principal")
    while True:
        valeur1=input("Entrez soit a , b ou c: ")
        if valeur1=="a":
            dict_dataset()
            while True:
                decise=int(input("\nEntrez 1 pour quitter et 2 pour aller au menu principal: "))
                if decise==1:
                    print("Vous avez quitter \n")
                    break
                elif decise==2:
                    Menu()
                    break
                else:
                    print("\nEntrez 1 ou 2")
            break
        elif valeur1=="b":
            Courbe_dataset()
            while True:
                decise=int(input("Entrez 1 pour quitter et 2 pour aller au menu principal: "))
                if decise==1:
                    print("Vous avez quitter \n")
                    break
                elif decise==2:
                    Menu()
                    break
                else:
                    print("\nEntrez 1 ou 2")
            break
        elif valeur1=="c":
            Menu()
            break
        else:
            print("\n entrez a , b ou c ")




