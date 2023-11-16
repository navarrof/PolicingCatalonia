import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib as mpl

Folder_DadesOrganitzatives = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/DadesOrganitzatives/"

df_poblacio = pd.read_csv(Folder_DadesOrganitzatives+ "Regions_policials_Poblacio.csv")
df_policia = pd.read_csv(Folder_DadesOrganitzatives+ "Personal_operatiu.csv")

df_policia = df_policia[df_policia["Any"] == 2022]

names, man, woman, total = [], [], [], []
ratio, ranked_man, ranked_woman, rank_ratio = [], [], [], []

for k in range(0,len(df_poblacio["REGIO_D"].values)):
    names += [df_poblacio["REGIO_D"].values[k]]

    asd = df_policia[(df_policia["Àmbit territorial"] == names[-1]) & (df_policia["Sexe"] == "Dona")]
    qwe = df_policia[(df_policia["Àmbit territorial"] == names[-1]) & (df_policia["Sexe"] == "Home")]

    if (len(qwe["Mosso/a"].values) > 0) and (len(asd["Mosso/a"].values)>0):
        man += [qwe["Mosso/a"].values[0] + qwe["Caporal/a"].values[0] + qwe["Sergent/a"].values[0]+ 
                qwe["Sotsinspector/a"].values[0]+qwe["Inspector/a"].values[0] + qwe["Intendent/a"].values[0] +
                qwe["Comissari/ària"].values[0] + qwe["Major"].values[0]]
        woman += [asd["Mosso/a"].values[0] + asd["Caporal/a"].values[0] + asd["Sergent/a"].values[0]+ 
                asd["Sotsinspector/a"].values[0]+asd["Inspector/a"].values[0] + asd["Intendent/a"].values[0] +
                asd["Comissari/ària"].values[0] + asd["Major"].values[0]]
        
        ranked_man += [ qwe["Sergent/a"].values[0]+ 
                qwe["Sotsinspector/a"].values[0]+qwe["Inspector/a"].values[0] + qwe["Intendent/a"].values[0] +
                qwe["Comissari/ària"].values[0] + qwe["Major"].values[0]]
        ranked_woman += [ asd["Sergent/a"].values[0]+ 
                asd["Sotsinspector/a"].values[0]+asd["Inspector/a"].values[0] + asd["Intendent/a"].values[0] +
                asd["Comissari/ària"].values[0] + asd["Major"].values[0]]
        
        total += [man[-1]+woman[-1]]
        ratio += [100*woman[-1]/(man[-1]+woman[-1])]
        rank_ratio += [100*ranked_woman[-1]/(ranked_man[-1]+ranked_woman[-1])]

plt.figure(1)
plt.plot(total)
plt.plot(man)  
plt.plot(woman)


plt.figure(2)
plt.plot(ratio)
plt.plot(rank_ratio)

plt.show()  
