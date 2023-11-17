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


fig, ax = plt.subplots(1, figsize=(6,4))

ax.plot(total, marker="o", color="black", label="Total")
ax.plot(man, marker="s", color = "teal", label="Man")
ax.plot(woman, marker="^", color="crimson", label="Woman")
ax.set_ylabel("Number of Police Officers")
ax.legend()
ax.set_xticklabels(df_poblacio["REGIO_C"].values,rotation=45,fontsize=10)
plt.tight_layout()


#plt.xticks(np.arange(0,len(df_poblacio["REGIO_C"].values)+1, 1.0))

fig2, ax2 = plt.subplots(1, figsize=(6,4))

ax2.plot(ratio, marker="o", color="forestgreen", label="All Ranks")
ax2.plot(rank_ratio, marker="o", color = "orange", label="Rank > Caporal")
ax2.set_ylabel("Female proportion [%]")

ax2.set_xticklabels(df_poblacio["REGIO_C"].values,rotation=45,fontsize=10)
ax2.legend()
plt.tight_layout()

plt.show()  
