import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import plotly.express as px

# ------- Folders with data ------------- # 

Folder_DadesPolicials = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/FetsPenals/"
Folder_DadesOrgan = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/DadesOrganitzatives/"
Folder_RegionsPolicials = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/GeoJsonFiles/"

# ----- Load Criminal data ----- #

df_fets = pd.read_csv(Folder_DadesPolicials+ "Fets_penals_coneguts.csv")

print(df_fets["Regió Policial (RP)"].values)

df_fets = df_fets[df_fets["Regió Policial (RP)"] == "RP Terres de l'Ebre"]
print(df_fets)

Anys_v = np.arange(2011, 2023, 1)
Crime_v, Solved_v = [], []
for year in Anys_v: 
    df_year = df_fets[df_fets["Any"] == year]
    Crimes = np.sum(df_year["Coneguts"].values)
    Solved = np.sum(df_year["Resolts"].values)
    Crime_v += [Crimes]; Solved_v += [Solved]

df_poblacio = pd.read_csv(Folder_DadesOrgan+ "Regions_policials_Poblacio.csv")

pob = df_poblacio[df_poblacio["REGIO_C"] ==  "Ebre"]["REGIO_POB"].values[0]

print("2022 Crimes/Population: ", Crime_v[-1]/pob)

print("Solved Crimes 2023: ", 100*Solved_v[-1]/Crime_v[-1])

print("Diff Solved 2022 - 2018: ", 100*Solved_v[-4]/Crime_v[-4] - 100*Solved_v[-1]/Crime_v[-1])




# ----- Load Territorial data ------ # 

def PlotMainRegionsMapPopulation():

    df = pd.read_csv(Folder_DadesOrgan+ "Regions_policials_Poblacio.csv")
    f = open(Folder_RegionsPolicials+"Regions_policials/Regions_Policials.json")
    geojson  = json.load(f)

    f, ax = plt.subplots(1, figsize=(15,15))

    fig = px.choropleth(df, 
                        locations="REGIO_C",  # Name of the column
                        geojson=geojson,
                        featureidkey = "properties.REGIO_C", 
                        color="REGIO_POB",
                        color_continuous_scale="Blues")
    
    # Avoids showing the rest of the world map. 
    fig.update_traces( marker_line_width=2) 
    fig.update_geos(fitbounds="locations", visible=False)


    fig.show()
    return fig

# ----------------- Plotting ------------------------- # 

# Evolution per year
# 

width = 0.4

fig, ax = plt.subplots(figsize=(7,3))
ax2 = ax.twinx()

ax.bar(Anys_v + width/2, Crime_v, width, color="orange",alpha=0.8,label="Known Crimes")
ax2.bar(Anys_v - width/2, Solved_v, width, color="darkblue", alpha=0.8, label="Solved Crimes")

ax.tick_params(axis='y', colors='orange')
ax2.tick_params(axis='y', colors="darkblue")

ax.set_ylabel("Known Crimes", fontsize=10, color="orange")
ax2.set_ylabel("Solved Crimes", fontsize=10, color="darkblue")
ax2.set_ylim(10000,600000)
ax.set_ylim(10000,600000)

plt.tight_layout()
plt.show()
# Mapss 
#

#PlotMainRegionsMapPopulation()


