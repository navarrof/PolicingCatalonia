import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Folder_DadesPolicials = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/FetsPenals/"
Folder_DadesOrgan = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/DadesOrganitzatives/"

df_fets = pd.read_csv(Folder_DadesPolicials+ "Fets_penals_coneguts.csv")

Anys_v = np.arange(2011, 2023, 1)
Crime_v = []
for year in Anys_v: 
    df_year = df_fets[df_fets["Any"] == year]
    Crimes = np.sum(df_year["Coneguts"].values)
    Crime_v += [Crimes]

plt.plot(Anys_v,Crime_v)
plt.show()
