import pandas


def dict_dataset():
    data = pandas.read_csv('installed-geothermal-capacity.csv')
    Dict_dataset=data.to_dict(orient='records')
    print(Dict_dataset)




def Courbe_dataset():
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv('installed-geothermal-capacity.csv')
    x = data['Entity']  
    y1 = data['Year']  
    y2 = data['Geothermal energy capacity'] 

    plt.plot(x, y1, label='Courbe 1')
    plt.plot(x, y2, label='Courbe 2')

    plt.xlabel('Entity')
    plt.ylabel('Geothermal energy capacity/Years')
    plt.title('Graphique avec Courbes')
    plt.legend()
    plt.grid(True)

    plt.show()