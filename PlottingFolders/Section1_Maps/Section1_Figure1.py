import pandas as pd
import json 
import plotly.express as px
import matplotlib.pyplot as plt


Folder_RegionsPolicials = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/GeoJsonFiles/"
Folder_DadesOrganitzatives = "C:/Users/naar/Desktop/Araceli_NF/OtherStuff/AraceliNF_Portfolio/PolicingCatalonia/DataFiles/CSVFiles/DadesOrganitzatives/"

def ReadFile(filename): 
    f = open(filename)
    for k,l in enumerate(f,start=0): 
        print(l.split(","))
        if k == 5: break

    return 0


def PlotMainRegionsMapPopulation():
    df = pd.read_csv(Folder_DadesOrganitzatives+ "Regions_policials_Poblacio.csv")
    f = open(Folder_RegionsPolicials+"Regions_policials/Regions_Policials.json")
    geojson  = json.load(f)

    f, ax = plt.subplots(1, figsize=(15,15))

    title = 'Territorial Separation'

    fig = px.choropleth(df, 
                        locations="REGIO_C",  # Name of the column
                        geojson=geojson,
                        featureidkey = "properties.REGIO_C",
                        color="REGIO_POB",
                        color_continuous_scale="Reds")
  
    #fig.add_scattergeo(
    #                    geojson=geojson,
    #                    locations=df["REGIO_C"],
    #                    text=df['REGIO_C'],
    #                    featureidkey="properties.REGIO_C",
    #                    mode='text+markers', 
    #                    textposition="top center",
    #                    textfont=dict( family="Arial", size=20, color="blue" ),
    #                    fillcolor = "blue"
    #                    )

    
    # Avoids showing the rest of the world map. 
    fig.update_geos(fitbounds="locations", visible=False)

    # Formats the colorbar
    fig.layout.coloraxis.colorbar.title = ''
    #fig.update_coloraxes(colorbar_title_font_size=40)
    fig.update_coloraxes(colorbar_title_side="top")
    fig.layout.coloraxis.colorbar.orientation = 'h'
    fig.layout.coloraxis.colorbar.len = 0.2
    fig.update_coloraxes(colorbar_tickfont_size=16)
  
    fig.update_layout(coloraxis_colorbar_x=0.7)
    fig.update_layout(coloraxis_colorbar_y=0.1)

    # Formats the tile of the image.
    #fig.update_layout(title = {
    #     'text': title,
    #     'y':0.9, # new
    #     'x':0.52,
    #     'xanchor': 'center',
    #     'yanchor': 'top' # new
    #    })
    #fig.update_layout(title_font_size=40)
    
    return fig


def PlotAreesBasiquesMapPopulation():


    #df = pd.read_csv(Folder_DadesOrganitzatives + "Arees_Basiques_Policials_Poblacio.csv")

    df = pd.read_csv(Folder_DadesOrganitzatives+ "Arees_Basiques_Policials_Poblacio.csv")

    f = open(Folder_RegionsPolicials+"Arees_Basiques_Policials/Arees_Basiques_Policials.json")
    geojson_Girona  = json.load(f)

    # We need to create some mapping between the geojson file and de df. We need an id key that will be associated with the id feature of the dframe. 

    
    title = 'Basic Police Areas'

    fig = px.choropleth(df, 
                        locations="ABP_D",  # Name of the column
                        geojson=geojson_Girona,
                        featureidkey = "properties.ABP_D",
                        color="ABP_POB",
                        color_continuous_scale="Reds")
    
    
    #fig.add_scattergeo(
    #                    geojson=geojson_Girona,
    #                    locations=df["ABP_D"],
    #                    text=df['ABP_C'],
    #                    featureidkey="properties.ABP_D",
    #                    mode='text', 
    #                    textposition="top center",
    #                    textfont=dict( family="Arial", size=30, color="Blue" )
    #                    )
  
    # Avoids showing the rest of the world map. 
    fig.update_geos(fitbounds="locations", visible=False)

    # Formats the colorbar
    fig.layout.coloraxis.colorbar.title = ''
    #fig.update_coloraxes(colorbar_title_font_size=40)
    fig.update_coloraxes(colorbar_title_side="top")
    fig.layout.coloraxis.colorbar.orientation = 'h'
    fig.layout.coloraxis.colorbar.len = 0.2
    fig.update_coloraxes(colorbar_tickfont_size=16)
  
    fig.update_layout(coloraxis_colorbar_x=0.7)
    fig.update_layout(coloraxis_colorbar_y=0.1)

    # Formats the tile of the image.
    #fig.update_layout(title = {
    #     'text': title,
    #     'y':0.9, # new
    #     'x':0.52,
    #     'xanchor': 'center',
    #     'yanchor': 'top' # new
    #    })
    #fig.update_layout(title_font_size=40)


    return fig

# ----------------------------------------------------------------------- # 

if __name__ == '__main__': 
    fig = PlotMainRegionsMapPopulation()
    #fig = PlotAreesBasiquesMapPopulation()
    fig.write_image("AreesBasiques.pdf")
    fig.show()