import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib as mpl

Folder_DadesOrganitzatives = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/DadesOrganitzatives/"


df_poblacio = pd.read_csv(Folder_DadesOrganitzatives+ "Regions_policials_Poblacio.csv")
df_comisaries = pd.read_csv(Folder_DadesOrganitzatives + "Comissaries_de_districte.csv")

names = ["Ebre", "Girona", "Metro Barcelona", "Metropolitana", "Metropolitana Nord", "Pirineu","Ponent", "Tarragona","Central"]
n_comisaries, poblacio, ratio = [],[], []

for k in range(0,len(df_poblacio["REGIO_C"].values)):
    cond = df_comisaries["REGIO_C"].values == names[k]
    n_comisaries += [len(df_comisaries["REGIO_C"].values[cond])]
    poblacio += [df_poblacio["REGIO_POB"].values[k]]


    ratio += [np.mean(df_comisaries["COMISSARIA_POB"].values[cond])]




fig, ax = plt.subplots(figsize=(7,3))
y = np.arange(len(df_poblacio["REGIO_C"].values))  # Label locations

ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines['right'].set_position(('outward', 60))


ax3.plot(ratio, color="limegreen", marker="o")

width = 0.4
ax.bar(y + width/2, n_comisaries, width, color="teal",alpha=0.8,label="Number Police Stations")
ax2.bar(y - width/2, poblacio, width, color="crimson", alpha=0.8, label="Region Population")

#Format ticks
ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
ax.set_xticklabels(names,rotation=45,fontsize=10)
plt.xticks(np.arange(min(y), max(y)+1, 1.0))
ax.tick_params(axis='y', colors='teal')
ax2.tick_params(axis='y', colors="crimson")
ax3.tick_params(axis='y', colors="limegreen")

ax.set_ylabel("Number of Police Stations", fontsize=10, color="teal")
ax2.set_ylabel("Region Population", fontsize=10, color="crimson")

ax.legend(loc='upper left')
ax2.legend(loc = 'upper right')



plt.tight_layout()
plt.show()
