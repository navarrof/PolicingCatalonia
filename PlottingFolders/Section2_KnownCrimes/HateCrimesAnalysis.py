import pandas as pd
import matplotlib.pyplot as plt

# ---------- Folder with data ----------- # 

Folder_DadesPolicials = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/FetsPenals/"
Folder_DadesOrgan = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/DadesOrganitzatives/"
Folder_RegionsPolicials = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/GeoJsonFiles/"

# ----------------------------------------- #

df_fets_0 = pd.read_csv(Folder_DadesPolicials+ "Fets_delictius_OdiTotal.csv")
df_fets = df_fets_0[ df_fets_0["Any"] == 2022]

n_sexisme, n_lgtbi, n_racism,n_disability = 0,0,0,0
n_religion,  n_politics,n_social = 0,0,0

empty_d = {'RP Metropolitana Barcelona': 0, "RP Metropolitana Sud":0,"RP Metropolitana Nord":0,
                 "RP Girona":0, "RP Camp de Tarragona":0, "RP Central":0, 
                    "RP Pirineu":0, "RP Terres de l'Ebre":0, "RP Ponent":0}

d_sexisme = empty_d.copy(); d_lgtbi = empty_d.copy(); d_disability = empty_d.copy()
d_religion = empty_d.copy(); d_racism = empty_d.copy(); d_politics = empty_d.copy()
d_social = empty_d.copy()




for k in range(0,len(df_fets["Mes"].values)): 
    try:
        if df_fets["Àmbit fet"].values[k] == "Sexisme":
            n_sexisme += df_fets["Nombre fets o infraccions"].values[k]
            d_sexisme[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]

        elif df_fets["Àmbit fet"].values[k] == "LGTBI-fòbia":
            n_lgtbi += df_fets["Nombre fets o infraccions"].values[k]
            d_lgtbi[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]
            

        elif df_fets["Àmbit fet"].values[k] == "Etnic/origen nacional/origen racial":
            n_racism += df_fets["Nombre fets o infraccions"].values[k]
            d_racism [df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]
        elif df_fets["Àmbit fet"].values[k] == "Antigitanisme":
            n_racism += df_fets["Nombre fets o infraccions"].values[k]
            d_racism[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]
        elif df_fets["Àmbit fet"].values[k] == "Antisemita":
            n_racism += df_fets["Nombre fets o infraccions"].values[k]
            d_racism[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]

        elif df_fets["Àmbit fet"].values[k] == "Discapacitat físic/sensorial":
            n_disability += df_fets["Nombre fets o infraccions"].values[k]
            d_disability[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]
        elif df_fets["Àmbit fet"].values[k] == "Discapacitat intel·lectual/mental":
            n_disability += df_fets["Nombre fets o infraccions"].values[k]
            d_disability[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]
        elif df_fets["Àmbit fet"].values[k] == "Malaltia":
            n_disability += df_fets["Nombre fets o infraccions"].values[k]
            d_disability[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]


        elif df_fets["Àmbit fet"].values[k] == "Orientació política":
            n_politics += df_fets["Nombre fets o infraccions"].values[k]
            d_politics[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]
        
        elif df_fets["Àmbit fet"].values[k] == "Aporofòbia":
            n_social += df_fets["Nombre fets o infraccions"].values[k]
            d_social[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]

        elif df_fets["Àmbit fet"].values[k] == "Islamofòbia":
            n_religion += df_fets["Nombre fets o infraccions"].values[k]
            d_religion[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]
        elif df_fets["Àmbit fet"].values[k] == "Religiós":
            n_religion += df_fets["Nombre fets o infraccions"].values[k]
            d_religion[df_fets["Regió Policial (RP)"].values[k]] += df_fets["Nombre fets o infraccions"].values[k]
        
        else: print("Crime Not there: ", df_fets["Àmbit fet"].values[k])
    except: continue


# --------------- Plot total type of hate --------------------- # 

labels = ["LGTBI", "Sexism", "Racism", "Disability", "Politics", "Aporophobia", "Religion"]
colors = ["darkorange","teal","navy","darkblue","darkturquoise","slategrey","deepskyblue"]

figure, ax = plt.subplots()
ax.pie([n_lgtbi,n_sexisme, n_racism, n_disability, n_politics, n_social, n_religion],labels=labels,textprops={'size': 'large'} )
ax.pie([n_lgtbi,n_sexisme, n_racism, n_disability, n_politics, n_social, n_religion], 
                    autopct='%1.1f%%',textprops={'size': 'large','color':'white'}, colors=colors,
                    radius=1.0
                    )
plt.title("Type of Hate Crimes", fontsize=14)


# ---------------------- Plot per region ------------------ # 

import json 
import plotly.express as px

def UpdateDictionary(d): 


    df_info = pd.read_csv(Folder_DadesOrgan+ "Regions_policials_Poblacio.csv")

    pob_metrobar = df_info[df_info["REGIO_D"] == "RP Metropolitana Barcelona"]["REGIO_POB"].values[0]
    pob_metronord =df_info[df_info["REGIO_D"] == "Regió Policial Metropolitana Nord"]["REGIO_POB"].values[0]
    pob_metrosud = df_info[df_info["REGIO_D"] == "RP Metropolitana Sud"]["REGIO_POB"].values[0]
    pob_girona = df_info[df_info["REGIO_D"] == "RP Girona"]["REGIO_POB"].values[0]
    pob_tarragona =df_info[df_info["REGIO_D"] == "RP Camp de Tarragona"]["REGIO_POB"].values[0]
    pob_central = df_info[df_info["REGIO_D"] == "RP Central"]["REGIO_POB"].values[0]
    pob_pirineu = df_info[df_info["REGIO_D"] == "RP Pirineu Occidental"]["REGIO_POB"].values[0]
    pob_ebre = df_info[df_info["REGIO_D"] == "RP Terres de l'Ebre"]["REGIO_POB"].values[0]
    pob_ponent = df_info[df_info["REGIO_D"] == "RP Ponent"]["REGIO_POB"].values[0]


    d["MetroBarcelona"] = d["RP Metropolitana Barcelona"]/pob_metrobar
    d["Metropolitana Nord"] = d["RP Metropolitana Nord"]/pob_metronord
    d["Metropolitana"] = d["RP Metropolitana Sud"]/pob_metrosud
    d["Girona"] = d["RP Girona"]/pob_girona
    d["Tarragona"] = d["RP Camp de Tarragona"]/pob_tarragona
    d["Central"] = d["RP Central"]/pob_central
    d["Pirineu"] = d["RP Pirineu"]/pob_pirineu
    d["Ebre"] = d["RP Terres de l'Ebre"]/pob_ebre
    d["Ponent"] = d["RP Ponent"]/pob_ponent
    
    del d["RP Metropolitana Barcelona"]; del d["RP Metropolitana Nord"]; del d["RP Metropolitana Sud"]
    del d["RP Girona"]; del d["RP Camp de Tarragona"]; del d["RP Central"]
    del d["RP Pirineu"]; del d["RP Terres de l'Ebre"]; del d["RP Ponent"]

    return d



d_lgtbi = UpdateDictionary(d_lgtbi)
df_lgtbi = pd.DataFrame.from_dict(d_lgtbi.items())
df_lgtbi.columns = ['RP Name','Number of Crimes']


d_sexisme = UpdateDictionary(d_sexisme)
df_sexisme = pd.DataFrame.from_dict(d_sexisme.items())
df_sexisme.columns = ['RP Name','Number of Crimes']


d_racism = UpdateDictionary(d_racism)
df_racism = pd.DataFrame.from_dict(d_racism.items())
df_racism.columns = ['RP Name','Number of Crimes']

d_religion = UpdateDictionary(d_religion)
df_religion = pd.DataFrame.from_dict(d_religion.items())
df_religion.columns = ['RP Name','Number of Crimes']

d_politics = UpdateDictionary(d_politics)
df_politics = pd.DataFrame.from_dict(d_politics.items())
df_politics.columns = ['RP Name','Number of Crimes']

d_social = UpdateDictionary(d_social)
df_social = pd.DataFrame.from_dict(d_social.items())
df_social.columns = ['RP Name','Number of Crimes']


f = open(Folder_RegionsPolicials+"Regions_policials/Regions_Policials.json")
geojson  = json.load(f)


f, ax = plt.subplots(1, figsize=(15,15))

figtitle = "social_2022.png"

fig = px.choropleth(df_social, 
                        locations="RP Name",  # Name of the column
                        geojson=geojson,
                        featureidkey = "properties.REGIO_C",
                        color="Number of Crimes",
                        color_continuous_scale="Reds")
fig.update_traces(marker_line_width=4) 
fig.update_layout(
        autosize=False,
        margin = dict( l=0,  r=0,   b=0,    t=0,    pad=4,   autoexpand=True  ) , width = 1200)
    
# Avoids showing the rest of the world map. 
fig.update_geos(fitbounds="locations", visible=False)
fig.write_image("C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/PlottingFolders/Section2_KnownCrimes/"+figtitle)
