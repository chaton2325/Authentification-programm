#Fonction pour l'algorithme cesar avec ASCII
def CESAR_ASCII(choix1,key):
    global list_séparé
    ascii_mot=""
    list_séparé=[]
    for character in choix1:
        test_list=str(ord(character)+key)
        ascii_mot+=str(ord(character)+key)
        list_séparé.append(int(test_list))
    print("\nLe mot crytpé est avec Cesar ASCII key =",key," est: ",ascii_mot)
    



#Fonction pour l'algorithme cesar 26 lettres 
def CESAR_key(choix1,key):
    global result
    choix1=choix1.lower()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    l=list(choix1) #Convertir la chaîne en liste pour apporter des modifications
    result=""
    for i in range(len(choix1)):
        if choix1[i] in alphabet:
            a=alphabet.index(choix1[i])
            b=a+key
            if b>25:
                b-=26  
            l[i]=alphabet[b]  
    result="".join(l)  
    print("\nLe mot crytpé est avec Cesar 26 lettres key =",key," est: ",result)

#Fonction qui va déchiffrer CESAR avec code ascii
def decipher_CESAR_ASCII(key):
    global list_séparé

    #On enlève la clé d'abord de chaque partie de la liste 
    for number in list_séparé:
        #On récupère l'index de number
        a=list_séparé.index(number)
        list_séparé[a]=number-key
    

    #On transforme les nombres de la liste en caractères avec chr
    for number1 in list_séparé:
        #On récu^père encore l'Index
        b=list_séparé.index(number1)
        list_séparé[b]=chr(number1)
    
    #On associe les lettres de la liste pour former une chaine de caractère
    mot_déchiffrer="".join(list_séparé)
    print("\nle mot déchiffré par Cesar decipher ASCII est: ",mot_déchiffrer)


#Fonction qui va déchiffrer CESAR avec les 26 lettres 
def decipher_CESAR_26_letters(key):
    global result
    #Cette fois si , on utilise l'alphabet inversé 
    alphabeti="zyxwvutsrqponmlkjihgfedcba"
    list_result=[]
    for i in result:
        list_result.append(i)
    for i in range(len(result)):
        a=alphabeti.index(result[i])
        b=a+key
        if b>25:
            b-=26  
        list_result[i]=alphabeti[b]
        result="".join(list_result)
    print("\nle mot déchiffré par Cesar decipher 26 lettres avec clé= ",key,"est: ",result)  
        

