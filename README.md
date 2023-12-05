# Catalonia Police Department


Author's note: This document might undergo modifications as it is not yet completed.  

### A quick overview: 



Catalonia is an autonomous community of Spain. It lies in the northeast of the Iberian Peninsula, to the south of the Pyrenees mountain range. The capital and largest city, Barcelona, is the second-most populated municipality in Spain and the fifth-most populous urban area in the European Union. The Mossos d’Escuadra is the police force of Catalonia, responsible for law enforcement in this autonomous area.

Here I present an exploratory analysis of the structure and organization of the Catalan police department as well as some insights into the criminality rates in the past 10 years. 



#### Tools used for the analysis: 

 The analysis has been primarily performed using **python** . The libraries used are the following:

    pandas, json, plotly.express, matplotlib.pyplot and numpy.

The data was also analyzed using SQL. In particular, SQL Little Online was used.

    Summary document under preparation, will be uploaded soon .... 

#### Data availability and structure

In this study, the public data available from the Catalonia police department has been collected, analyzed and evaluated. The data was collected from the open data catalog provided by the Catalan administration. All the data files (and more) can be found on the following website: 

[https://mossos.gencat.cat/ca/els_mossos_desquadra/indicadors_i_qualitat/dades_obertes/ ](https://mossos.gencat.cat/ca/els_mossos_desquadra/indicadors_i_qualitat/dades_obertes/ )

The data that was downloaded and used for this study corresponds to the website update of 17/05/2022. All the data files are provided in **.csv** and **.json** format. For this study, both formats are used, depending on the convenience. 



## 1. Organizational Information. 



Territorially, the Catalan police is divided into 9 regions (Girona, Ponent, Pirineu Occidental, Central, Metropolitana Nord, Barcelona, Metropolitana Sud, Camp de Tarragona i Terres de l'Ebre). Figure 1 (left) shows the geographical location of each of the regions as well as the population as of 2022. The basic police areas are different divisions of the Catalonia police that are in charge of a specific geographic area and provide the basic police services to the population of that area [1]. Figure 1 (right) shows the territorial division of these basic police areas as well as the population in each one of them. 

![Figure 1]("PlottingFolders/Section1_Maps/Map.png")

**Figure 1**: Left, territorial division of the Catalan police. A: Pirineu, B: Ponent, C: Central, D: Ebre, E: Tarragona, F: Metropolitana Sud, G: Metropolitana Nord, H: Metropolitana Barcelona, I: Girona. Right, Geographical description of the basic police areas in Catalonia. 




## References

[1] https://ca.wikipedia.org/wiki/%C3%80rea_B%C3%A0sica_Policial 