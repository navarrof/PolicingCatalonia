import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# ---------- Folder with data ----------- # 

Folder_DadesPolicials = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/FetsPenals/"

df_fets_0 = pd.read_csv(Folder_DadesPolicials+ "Fets_delictius_OdiAnalysis.csv")
df_fets = df_fets_0[ df_fets_0["Any"] == 2022]

n_sexisme, n_lgtbi, n_racism,n_disability = 0,0,0,0
n_religion,  n_politics,n_social = 0,0,0

victim_sexisme, victim_lgtbi, victim_racism = [],[],[]
victim_religion,  victim_politics,victim_social = [],[],[]

perpetrator_sexisme, perpetrator_lgtbi, perpetrator_racism = [],[],[]
perpetrator_religion,  perpetrator_politics,perpetrator_social = [],[],[]


for k in range(0,len(df_fets["Núm. Mes"].values)): 
    try:
        # --------------------- Sexisme ----------------------------------- # 
        if df_fets["Àmbit fet"].values[k] == "Sexisme":
            n_sexisme += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_sexisme += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_sexisme += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]

        # --------------------- LGTNO ----------------------------------- # 
        elif df_fets["Àmbit fet"].values[k] == "LGTBI fòbia":
            n_lgtbi += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_lgtbi += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_lgtbi += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
        elif df_fets["Àmbit fet"].values[k] == "LGTBI-fòbia":
            n_lgtbi += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_lgtbi += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_lgtbi += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]

        # --------------------- Racisme  ----------------------------------- # 
        elif df_fets["Àmbit fet"].values[k] == "Etnic/origen nacional/origen racial":
            n_racism += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_racism += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_racism += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
        elif df_fets["Àmbit fet"].values[k] == "Antigitanisme":
            n_racism += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_racism += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_racism += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
        elif df_fets["Àmbit fet"].values[k] == "Antisemita":
            n_racism += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_racism += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_racism += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]

        # --------------------- Politics ----------------------------------- # 
        elif df_fets["Àmbit fet"].values[k] == "Orientació política":
            n_politics += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_politics += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_politics += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
        
        # --------------------- Social  ----------------------------------- # 
        elif df_fets["Àmbit fet"].values[k] == "Aporofòbia":
            n_social += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_social += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_social += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]

        # --------------------- Religion ----------------------------------- # 
        elif df_fets["Àmbit fet"].values[k] == "Islamofòbia":
            n_religion += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_religion += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor': 
                perpetrator_religion += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
        elif df_fets["Àmbit fet"].values[k] == "Religiós":
            n_religion += df_fets["Nombre víctimes"].values[k]
            if df_fets['Rol'].values[k] == 'Víctima':
                victim_religion += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
            elif df_fets['Rol'].values[k] == 'Autor':
                perpetrator_religion += [ [df_fets['Sexe'].values[k],df_fets['Edat'].values[k]] ]
        
        else: print("Crime Not there: ", df_fets["Àmbit fet"].values[k])
    except: continue



# ---------------------- Analysis of victims ---------------- # 
import numpy as np 

def Analysis(vec):
    n_w, n_m, av_age = 0,0,0
    for k in range(0,len(vec)): 
        sex = vec[k][0]; age = vec[k][1]
        if sex == 'HOME': n_m += 1
        elif sex == "DONA": n_w += 1

        av_age += age/len(vec)

    return n_w, n_m, av_age

# Victims
#
n_w_racism, n_m_racism, av_age_racism = Analysis(victim_racism)
n_w_lgtbi, n_m_lgtbi, av_age_lgtbi = Analysis(victim_lgtbi)
n_w_sexisme, n_m_sexisme, av_age_sexisme = Analysis(victim_sexisme)
n_w_religion, n_m_religion, av_age_religion = Analysis(victim_religion)
n_w_politics, n_m_politics, av_age_politics = Analysis(victim_politics)
n_w_aporophobia, n_m_aporophobia, av_age_aporophobia = Analysis(victim_social)

Man_Victim = [n_m_sexisme,n_m_lgtbi,n_m_racism,n_m_religion,n_m_politics,n_m_aporophobia]
Woman_Victim = [n_w_sexisme,n_w_lgtbi,n_w_racism,n_w_religion,n_w_politics,n_w_aporophobia]
AGE_Victim = [av_age_sexisme,av_age_lgtbi,av_age_racism,av_age_religion,av_age_politics,av_age_aporophobia]

#Perpetrators
#

print(perpetrator_racism)
n_w_racism, n_m_racism, av_age_racism = Analysis(perpetrator_racism)
n_w_lgtbi, n_m_lgtbi, av_age_lgtbi = Analysis(perpetrator_lgtbi)
n_w_sexisme, n_m_sexisme, av_age_sexisme = Analysis(perpetrator_sexisme)
n_w_religion, n_m_religion, av_age_religion = Analysis(perpetrator_religion)
n_w_politics, n_m_politics, av_age_politics = Analysis(perpetrator_politics)
n_w_aporophobia, n_m_aporophobia, av_age_aporophobia = Analysis(perpetrator_social)

Man_Perpetrator = [n_m_sexisme,n_m_lgtbi,n_m_racism,n_m_religion,n_m_politics,n_m_aporophobia]
Woman_Perpetrator = [n_w_sexisme,n_w_lgtbi,n_w_racism,n_w_religion,n_w_politics,n_w_aporophobia]
AGE_Perpetrator = [av_age_sexisme,av_age_lgtbi,av_age_racism,av_age_religion,av_age_politics,av_age_aporophobia]


# ----------------------------------------- PLOT ----------------------------------  #

TypeCrime = ["0","Sexism","LGTBI","Racism","Religion","Politics","Aporophobia"]



width = 0.4
y = np.arange(1,len(TypeCrime))  # Label locations

fig, ax = plt.subplots(2, figsize=(8,8))
ax2 = ax[0].twinx()
ax3 = ax[1].twinx()

bar1 = ax[0].bar(y + width/2, Man_Victim, width, color="teal",alpha=0.8,label="Man")
bar2 = ax[0].bar(y - width/2, Woman_Victim, width, color="crimson",alpha=0.8,label="Woman")

ax2.plot(y,AGE_Victim,marker="s", color="orange")
ax2.tick_params(axis='y',color="orange", labelsize=14,labelcolor="orange")

ax2.set_ylabel("Average Age [years]", fontsize=14, color="orange")

ax[0].tick_params(axis='both', labelsize=14)
ax[0].legend(fontsize=14,loc="upper left")
ax[0].set_xticklabels(TypeCrime,rotation=45,fontsize=14)
ax[0].set_title("Hate crimes victims", fontsize=14)


bar3= ax[1].bar(y + width/2, Man_Perpetrator, width, color="teal",alpha=0.8,label="Man")
bar4 = ax[1].bar(y - width/2, Woman_Perpetrator, width, color="crimson",alpha=0.8,label="Woman")

ax3.plot(y,AGE_Perpetrator,marker="s", color="orange")
ax3.tick_params(axis='y',color="orange", labelsize=14,labelcolor="orange")

ax3.set_ylabel("Average Age [years]", fontsize=14, color="orange")

ax[1].tick_params(axis='both', labelsize=14)
ax[1].legend(fontsize=14,loc="upper left")
ax[1].set_xticklabels(TypeCrime,rotation=45,fontsize=14)
ax[1].set_title("Hate crimes perpetrators", fontsize=14)

plt.tight_layout()
plt.show()

        
