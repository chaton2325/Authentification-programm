import pandas


def dict_dataset():
    data = pandas.read_csv('installed-geothermal-capacity.csv')
    Dict_dataset=data.to_dict(orient='records')
    print(Dict_dataset)




def Courbe_dataset():
    import pandas as pd
    import matplotlib.pyplot as plt
    #Pour le choix entre graphique en bandes et graphiques linéaire
    


    #On définit les datas
    data = pd.read_csv('installed-geothermal-capacity.csv')
    x = data['Entity']    
    y2 = data['Geothermal energy capacity'] 

    #Concernant les titres (abcisses , ordonnées et titre de courbes)
    plt.title('Energie géothermique installé par continents (2000-2022)')
    plt.xlabel('Continents')
    plt.ylabel("Energies géothermique installé(Mégawatts)")

    while True:
        choix=int(input("\nEntrez 1 pour le diagramme en bandes et 2 pour le diagramme linéaire : "))
        if choix==1:
            #bar pour le diagramme en bandes
            plt.bar(x,y2,label="Energie en fonction des continents") #ca initialise le diagramme sous forme de bandes
            plt.legend() # Ca met la légende 
            plt.show() #On affiche le diagramme
            break
        elif choix==2:
            #plot pour le diagramme linéaire
            plt.plot(x,y2,label="Energie en fonction des continents")
            plt.legend()
            plt.show()
            break
        else:
            print("\nEntrez 1 ou 2 ")