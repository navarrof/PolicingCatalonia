import pandas as pd


# ---------- Folder with data ----------- # 

Folder_DadesPolicials = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/FetsPenals/"
Folder_DadesOrgan = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/DadesOrganitzatives/"

# -------- Classification of types of crimes ------  # 

against_people = ['Lesions','Tracte degradant / vexatori','Homicidi','Amenaces','Coaccions', 'Homicidi per imprudència',
                  'Abusos sexuals','Contra els drets i deures familiars', 'Receptació i altres conductes afins',
                  'Segrest', 'Agressions sexuals','Assetjament sexual','Injúria','Contra exercici drets fonamentals i llibertats públiques', 'Contra la llibertat de consciència, religió i respecte als difunts',"Contra la comunitat internacional",
                    'Contra els drets dels treballadors',  'Contra els drets de ciutadans estrangers', 'Assassinat', 'Fals testimoni', 'Omissió del deure de socors',"Tràfic d'èssers humans",'Tortures', "Tràfic d'éssers humans",
                    'Faltes contra les persones', 'Infidelitat custòdia documents i violació secrets',"Frustració d'execució",
                    'Avortament' , 'Inducció i cooperació al suïcidi', 'Violació de secrets',"Calúmnia","Lesions al fetus"]

Murder = ['Homicidi','Assassinat','Inducció i cooperació al suïcidi','Homicidi per imprudència']
Sexual_Assault = ['Abusos sexuals','Agressions sexuals','Assetjament sexual']
FreedomHate = ['Injúria','Contra exercici drets fonamentals i llibertats públiques', "Contra la comunitat internacional",
               'Contra la llibertat de consciència, religió i respecte als difunts',
               'Contra els drets dels treballadors',  'Contra els drets de ciutadans estrangers','Faltes contra les persones' ]
InjuriesThreats = ['Lesions','Amenaces',"Lesions al fetus"]
KidnapingTorture = ['Segrest','Tortures']
#Others = ['Tracte degradant / vexatori','Receptació i altres conductes afins','Fals testimoni', 'Omissió del deure de socors',
#          'Infidelitat custòdia documents i violació secrets',"Frustració d'execució",
#                    'Avortament','Violació de secrets','Coaccions']


against_property = ["De la usurpació de l'estat civil",'Falsedats documentals','Apropiació indeguda',
                    'Prevaricació de funcionaris públics' , 'Suborn','Danys',"Contra les institucions de l'Estat i divisió de poders",
                    'Usurpació de funcions publiques i intrusisme','Furt','Ocupació immobles', 'Incendi',
                    'Estafes', 'Robatori amb força', 'Robatori amb violència i/o intimidació', 'Robatori i furt dus de vehicle',
                    'Calumnia', 'Entrada a vivenda aliena',"Usurpació de funcions públiques i intrusisme", "Fraus i exaccions il·legals",
                    "Contra l'ordenació del territori",'Propietat industrial', 'Contra el patrimoni històric',
                    'Propietat intel·lectual','Faltes contra el patrimoni', "Contra les institucions de l'estat i divisió de poders",
                    "Sostracció de cosa pròpia d'utilitat social",'Corrupció als negocis','Contra la corona',
                    "Contra l'administració de jústicia",'Defraudacions de fluïd elèctric i anàlogues','Falsificació de moneda i efectes timbrats', 'Robatori amb força interior vehicle','Usurpació', 'Malversació', 'Ultratges a espanya'
                    , 'Blanqueig de capitals', 'Contra els recursos naturals i el medi ambient', 'Extorsió',"Entrada a domicili aliè"
                    , "Robatori i furt d'us de vehicle","Defraudacions de fluid elèctric i anàlogues"]

RobberyBulgary = ['Robatori amb força', 'Robatori amb violència i/o intimidació', 'Robatori i furt dus de vehicle', 'Robatori amb força interior vehicle',"Robatori i furt d'us de vehicle"]
Theft = ['Furt']
Damage = ['Danys', 'Incendi']
Scams = ['Estafes']
#Others = ["De la usurpació de l'estat civil",'Falsedats documentals','Prevaricació de funcionaris públics',
#          'Suborn','Usurpació de funcions publiques i intrusisme' ,'Ocupació immobles','Entrada a vivenda aliena',
#            "Contra l'ordenació del territori"]


other_types = ['Contra la salut pública','Detenció il·legal','Conduir sense permís','Trencament de condemna',
                'Originar un greu risc per la circulació','Terrorisme',"Reunió, manifestació il·lícita","Administració deslleial",
                'Conduir sota els efectes dalcohol i drogues', 'Conducció temerària', 'Velocitat penalment punible',"Atemptat a autoritat, agents de l' autoritat i resistència i desobediència", 'Descobriment i revelació de secrets',
                'Abandonament lloc accident', "Negativa a sotmetre's a les proves", 'Acusació, denúncia falsa i simulació de delictes', 'Obstrucció a la justícia i deslleialtat professional', 'Organitzacions i grups criminals',
                'Exhibicionisme i provocació sexual',  'Encobriment', "Conduir sota els efectes d'alcohol i drogues",
                'Realització arbitrària del propi dret', 'Societaris', 'Desordres públics',  "Omissió dels deures d'impedir delictes",
                'Protecció de la flora, fauna i animals domèstics','Hisenda pública i seguretat social',
                'Relatius a la prostitució', 'Insolvències punibles', 'Reunió, manifestació il·licita',
                'Risc catastròfic', 'Administració desleial',"Desobediència i denegació d'auxili", "Prevaricació"
                "Conduir sota els efectes d'alcohol i drogues", "Altres delictes contra l'ordre públic",
                'Matrimonis il.legals','Mercat i consumidors', "Tràfic d'influències", 'Contra la seguretat colectiva'
                ]

against_police = ["Atemptat a autoritat, agents de l' autoritat i resistència i desobediència",
                  'Obstrucció a la justícia i deslleialtat professional']
driving = ['Conduir sense permís','Originar un greu risc per la circulació','Conduir sota els efectes dalcohol i drogues', 
           'Conducció temerària', "Conduir sota els efectes d'alcohol i drogues"]
publicdisorder = ['Contra la salut pública', 'Terrorisme','Desordres públics','Reunió, manifestació il·licita',
                'Risc catastròfic','Contra la seguretat colectiva',"Altres delictes contra l'ordre públic"]
#Other = ['Detenció il·legal','Trencament de condemna','Descobriment i revelació de secrets',
#                'Abandonament lloc accident', "Negativa a sotmetre's a les proves", 'Acusació, denúncia falsa i simulació de delictes',
#                 'Organitzacions i grups criminals','Exhibicionisme i provocació sexual',  
#                 'Encobriment','Realització arbitrària del #propi dret', 'Societaris',"Omissió dels deures d'impedir delictes",
#                'Protecció de la flora, fauna i animals domèstics','Hisenda pública i seguretat social',
#                'Relatius a la prostitució', 'Insolvències punibles']

'''

against_people = ['De l’homicidi i les seves formes', 'De les lesions', 'De les tortures i altres delictes contra la integritat moral',
                  'Delictes contra la intimitat, el dret a la pròpia imatge i la inviolabilitat del domicili','Delictes contra la llibertat','Delictes contra la llibertat i la indemnitat sexuals',  'Delictes contra les relacions familiars',
                     'Faltes contra les persones', 'Dels delictes contra els drets dels treballadors', 'Del tràfic d’éssers humans',
                      'Delictes contra els drets dels ciutadans estrangers', 'De les lesions al fetus', 'De l’avortament', 'Delictes contra la comunitat internacional' ]

Murder = ['De l’homicidi i les seves formes']
Sexual = ['De les lesions','De les lesions al fetus']
Injuries = ['De les tortures i altres delictes contra la integritat moral', ]
HomeViolence = ['Delictes contra les relacions familiars']
Odi = ['Delictes contra la llibertat','Delictes contra la llibertat i la indemnitat sexuals', 
           'Delictes contra els drets dels ciutadans estrangers','Delictes contra la comunitat internacional' ]
Others = ['Delictes contra la intimitat, el dret a la pròpia imatge i la inviolabilitat del domicili',
          'Faltes contra les persones', 'Del tràfic d’éssers humans']
Workers = [ 'Dels delictes contra els drets dels treballadors', 'De l’avortament' ]

against_property = ['Delictes contra el patrimoni i contra l’ordre socioeconòmic',"Delictes contra l'Administració de justícia",
                    "Delictes contra l'ordre públic", 'Delictes contra la Constitució', "Delictes contra l'Administració pública",
                    'Delictes contra l’honor', 'Dels delictes relatius a l’ordenació del territori i l’urbanisme, la protecció del patrimoni històric i el medi ambient','Faltes contra el patrimoni']

other_types = ['Delictes contra la seguretat viària','Dels delictes contra la seguretat col·lectiva',
               'Faltes contra els interessos generals', "Faltes contra l'ordre públic",'De l’omissió del deure d’auxili',
               'Dels delictes contra la hisenda pública i contra la Seguretat Social','De les falsedats']

'''
               
df_fets_0 = pd.read_csv(Folder_DadesPolicials+ "Fets_penals_coneguts.csv")
df_fets = df_fets_0[ df_fets_0["Any"] == 2022]


n_persones, n_property, n_other = 0.0,0.0,0.0
n_murder, n_sexual, n_FreedomHate, n_InjuriesThreats, n_KidnapingTorture = 0.0, 0.0, 0.0, 0.0, 0.0
n_RobberyBulgary, n_Theft, n_damage, n_scam = 0,0,0,0
n_against_police, n_driving, n_publicdisorder = 0,0,0
total = 0


for k in range(0,len(df_fets["Mes"].values)): 
    try:
        if df_fets["Tipus de fet"].values[k] in against_people:        
            n_persones += df_fets["Coneguts"].values[k]
            if df_fets["Tipus de fet"].values[k] in Murder: 
                n_murder += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in Sexual_Assault:
                n_sexual += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in FreedomHate: 
                n_FreedomHate += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in InjuriesThreats: 
                n_InjuriesThreats += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in KidnapingTorture: 
                n_KidnapingTorture += df_fets["Coneguts"].values[k]

        elif df_fets["Tipus de fet"].values[k] in against_property:     
            n_property += df_fets["Coneguts"].values[k]
            if df_fets["Tipus de fet"].values[k] in RobberyBulgary: 
                n_RobberyBulgary += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in Theft:
                n_Theft += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in Damage:
                n_damage += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in Scams:
                n_scam += df_fets["Coneguts"].values[k]


        elif df_fets["Tipus de fet"].values[k] in other_types:         
            n_other += df_fets["Coneguts"].values[k]
            if df_fets["Tipus de fet"].values[k] in against_police:
                n_against_police += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in driving:
                n_driving += df_fets["Coneguts"].values[k]
            elif df_fets["Tipus de fet"].values[k] in publicdisorder:
                n_publicdisorder += df_fets["Coneguts"].values[k]

        else: print("Not there: "+ df_fets["Tipus de fet"].values[k])

        total += df_fets["Coneguts"].values[k]
    except: continue
    

#type_of_crime = list(dict.fromkeys(df_fets["Títol Codi Penal"].values))
print("Total Crimes: ", total)
print()
print("Contra Persones: ", n_persones, "Proportion total: ", 100*n_persones/total)
print("Murder: ", 100*n_murder/n_persones)
print("Sexual: ", 100*n_sexual/n_persones)
print("Freedom Hate: ", 100*n_FreedomHate/n_persones)
print("Injuries Threats: ", 100*n_InjuriesThreats/n_persones)
print("Kidnaping Torture: ", 100*n_KidnapingTorture/n_persones)
print("Other: ", 100*(n_persones-n_murder-n_sexual-n_FreedomHate-n_InjuriesThreats-n_KidnapingTorture)/n_persones)

print()
print("Contra_Patrimoni: ", 100*n_property/total)
print("Theft: ",100*n_Theft/n_property)
print("Robbery: ",100*n_RobberyBulgary/n_property)
print("Damage: ",100*n_damage/n_property)
print("Scams: ",100*n_scam/n_property)
print("Others: ",100*(n_property-n_Theft-n_RobberyBulgary-n_damage-n_scam)/n_property)
print()

print("Others: ", 100*n_other/total)
print("Against the police: ",100*n_against_police/n_other )
print("Driving: ", 100*n_driving/n_other)
print("Public Disorder: ", 100*n_publicdisorder/n_other)
print("Others: ",100*(n_other-n_against_police-n_driving-n_publicdisorder)/n_other)


# --------------------------- ANalysis of each area --------------------- # 
import numpy as np 

MetroBarcelona, MetroNord, MetroSud, Ebre, Pirineu= 0,0,0,0,0
Ponent, Central, Girona, Tarragona = 0,0,0,0


for crime in InjuriesThreats: 
    df = df_fets[df_fets["Tipus de fet"] == crime]
    df_metrobar = df[df["Regió Policial (RP)"] == "RP Metropolitana Barcelona"]
    df_metrosud = df[df["Regió Policial (RP)"] == "RP Metropolitana Sud"]
    df_metronord = df[df["Regió Policial (RP)"] == "RP  Metropolitana Nord"]
    df_girona = df[df["Regió Policial (RP)"] == "RP Girona"] 
    df_tarragona = df[df["Regió Policial (RP)"] == "RP Camp de Tarragona"]
    df_central = df[df["Regió Policial (RP)"] == "RP Central"]
    df_pirineu =  df[df["Regió Policial (RP)"] == "RP Pirineu Occidental"]
    df_ebre = df[df["Regió Policial (RP)"] == "RP Terres de l'Ebre"]
    df_ponent = df[df["Regió Policial (RP)"] == "RP Ponent"]

    MetroBarcelona += np.sum(df_metrobar["Coneguts"].values)
    MetroNord += np.sum(df_metronord["Coneguts"].values)
    MetroSud += np.sum(df_metrosud["Coneguts"].values)
    Girona += np.sum(df_girona["Coneguts"].values)
    Tarragona += np.sum(df_tarragona["Coneguts"].values)
    Central += np.sum(df_central["Coneguts"].values)
    Pirineu += np.sum(df_pirineu["Coneguts"].values)
    Ebre += np.sum(df_ebre["Coneguts"].values)
    Ponent += np.sum(df_ponent["Coneguts"].values)

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



print()
print("Crime Per area")
print()

vec = [MetroBarcelona/pob_metrobar, MetroSud/pob_metrosud, 
                            MetroNord/pob_metronord, 
                            Girona/pob_girona, Tarragona/pob_tarragona,
                            Central/pob_central, Pirineu/pob_pirineu,
                            Ebre/pob_ebre, Ponent/pob_ponent]
total = np.sum(vec)

print("Metro Barcelona: ", MetroBarcelona, 100/total * MetroBarcelona/pob_metrobar)
print("Metro Sud: ", MetroSud, 100/total * MetroSud/pob_metrosud)
print("Metro Nord: ", MetroNord,  100/total *MetroNord/pob_metronord)
print("Girona: ",Girona, 100/total * Girona/pob_girona)
print("Tarragona: ",Tarragona,  100/total *Tarragona/pob_tarragona)
print("Central: ",Central,  100/total *Central/pob_central)
print("Pirineu: ",Pirineu,  100/total * Pirineu/pob_pirineu)
print("Ebre: ",Ebre, 100/total * Ebre/pob_ebre)
print("Ponent: ",Ponent,  100/total *Ponent/pob_ponent)
print()
print("    Max: ", 100/total * np.max(vec), "    Min: ", 100/total * np.min(vec))


# ----------------- Time evolution of Crimes ---------------------- # 

yearv = [ 2016, 2017, 2018, 2019, 2020, 2021, 2022]

v_people, v_murder, v_sex, v_hate, v_injury = [],[],[],[],[]
v_property, v_Theft, v_robbery, v_damage, v_scam = [],[],[],[],[]
v_other, v_police, v_driving, v_public = [],[],[],[]

for year in yearv: 
    df_fets = df_fets_0[ df_fets_0["Any"] == year]

    # ---------- Against people ---------------- # 
    ncrimes = 0
    for crime in against_people: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_people += [ncrimes]

    ncrimes = 0
    for crime in Murder: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_murder += [ncrimes]

    ncrimes = 0
    for crime in Sexual_Assault: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_sex += [ncrimes]

    ncrimes = 0
    for crime in InjuriesThreats: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_injury += [ncrimes]
    
    ncrimes = 0
    for crime in FreedomHate: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_hate += [ncrimes]

    # ---------- Against property ---------------- # 
    
    ncrimes = 0
    for crime in against_property: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_property += [ncrimes]

    ncrimes = 0
    for crime in RobberyBulgary: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_robbery += [ncrimes]

    ncrimes = 0
    for crime in Theft: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_Theft += [ncrimes]

    for crime in Damage: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_damage += [ncrimes]
    
    ncrimes = 0
    for crime in Scams: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_scam += [ncrimes]

    # ---------- Other Crimes ---------------- # 
    
    ncrimes = 0
    for crime in other_types: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_other += [ncrimes]

    ncrimes = 0
    for crime in against_police: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_police += [ncrimes]

    ncrimes = 0
    for crime in driving: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_driving += [ncrimes]

    ncrimes = 0
    for crime in publicdisorder: 
        df = df_fets[df_fets["Tipus de fet"] == crime]
        ncrimes += np.sum(df["Coneguts"].values)
    v_public += [ncrimes]


# Plotting
#

import matplotlib.pyplot as plt
print()
print("Crimes with time: ")

fig, ax = plt.subplots(3, figsize=(9,9))

# Poeple
# 
ax[0].set_title("Crimes against people", fontsize=14)
ax[0].plot(yearv, v_people, marker="s", ms=6, label="Total", color="darkred")
ax[0].plot(yearv, v_murder, marker="o",ms=8,label="Murder", color="indianred")
ax[0].plot(yearv, v_sex, marker="^",ms=8,label="Sexual",color="tomato")
ax[0].plot(yearv, v_hate, marker=">",ms=8,label="Hate", color="darkorange")
ax[0].plot(yearv, v_injury,marker="<",ms=8, label= "Injuries and Threats", color="gold")
ax[0].set_xlabel("Years", fontsize=14)
ax[0].legend(bbox_to_anchor=(1.1, 1.05), fontsize=14)
ax[0].set_ylabel("Number of Crimes", fontsize=14)
ax[0].tick_params(axis='both', labelsize=14)

ax[1].set_title("Crimes against property", fontsize=14)
ax[1].plot(yearv, v_property, marker="s",ms=6,label="Total", color="darkolivegreen")
ax[1].plot(yearv, v_Theft, marker="o",ms=8,label="Theft", color="forestgreen")
ax[1].plot(yearv, v_robbery,marker="^", ms=8,label="Robbery", color="mediumseagreen")
ax[1].plot(yearv, v_damage, marker=">",ms=8,label="Damage", color="limegreen")
ax[1].plot(yearv, v_scam, marker="<",ms=8,label="Scam", color="springgreen")
ax[1].set_xlabel("Years", fontsize=14)
ax[1].legend(bbox_to_anchor=(1.1, 1.05), fontsize=14)
ax[1].set_ylabel("Number of Crimes", fontsize=14)
ax[1].tick_params(axis='both', labelsize=14)

ax[2].set_title("Other Crimes", fontsize=14)
ax[2].plot(yearv, v_other,marker="s",ms=6, label="Total", color="navy")
ax[2].plot(yearv, v_police, marker="o",ms=8,label="Against Police", color="royalblue")
ax[2].plot(yearv, v_driving, marker="^",ms=8,label="Driving",color="dodgerblue")
ax[2].plot(yearv, v_public,marker=">", ms=8,label="Public Disorder",color="aqua")
ax[2].set_xlabel("Years", fontsize=14)
ax[2].legend(bbox_to_anchor=(1.1, 1.05), fontsize=14)
ax[2].set_ylabel("Number of Crimes", fontsize=14)
ax[2].tick_params(axis='both', labelsize=14)
plt.tight_layout()
plt.show()