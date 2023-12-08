


## Catalonia Police Department

Author's note: This document might undergo modifications as it is not yet completed.  

## A quick overview: 


Catalonia is an autonomous community of Spain. It lies in the northeast of the Iberian Peninsula, to the south of the Pyrenees mountain range. The capital and largest city, Barcelona, is the second-most populated municipality in Spain and the fifth-most populous urban area in the European Union. The Mossos d’Escuadra is the police force of Catalonia, responsible for law enforcement in this autonomous area.

Here I present an exploratory analysis of the structure and organization of the Catalan police department as well as some insights into the criminality rates in the past 10 years. 



## Tools used for the analysis: 

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

![Map](https://github.com/navarrof/PolicingCatalonia/assets/54847307/f2473838-1d3f-4d89-ba69-9596682b5d50)
![ABP](https://github.com/navarrof/PolicingCatalonia/assets/54847307/556fd18a-e512-4d2e-9447-fabc89436d06)

*Figure 1: Top, territorial division of the Catalan police. A: Pirineu, B: Ponent, C: Central, D: Ebre, E: Tarragona, F: Metropolitana Sud, G: Metropolitana Nord, H: Metropolitana Barcelona, I: Girona. Bottom, Geographical description of the basic police areas in Catalonia.*


Some of the basic police areas are very complex or have to deal with a big amount of population. For this reason, the district police stations provide service to their corresponding basic police area. In [2] one can find the location of the various police offices in Catalunya as well as the necessary contact information. Figure 2 shows the number of police stations and the population in each of the 9 territorial regions in 2022. As expected, there is a significant correlation between the population in a territory and the number of police stations. The green line in Figure 2 indicates the average population that lies under the control of a given police station. For example, in the Ebre region, there are 5 police stations. Each of them is assigned to an amount of population. The average amount of population that needs to be handled for the police stations in Ebre is around 5000 people per police station. This representation might not be the best to assess the resources assigned to each of the regions, as the police stations can vary in size, that is, the amount of personnel assigned to that station. 

![PoliceStations_Popuplation](https://github.com/navarrof/PolicingCatalonia/assets/54847307/7be22ecd-7a30-4b23-98c7-3e4e7907f4da)

*Figure 2: For each of the territorial regions, population, number of police stations, and (in green) average population under the control of a given police station.*

In figure 3, the amount of police personal assigned to each area in 2022 is shown. Unfortunatelly, there was no available data for the Metropolitana nord area. This figure reveals that the majority of the police personnel is stationed in the Metro Barcelona area, aligning with the concentration of the population in this region. The available information includes details on the rank of personnel and their gender, enabling a small gender study of the Catalan police. Additionally, in Figure 3, the number of police officers is presented, categorized by gender. It is unsurprising to note that female officers constitute a minority. The proportion of female officers seems to be consistent among the various areas, with a maximum of 25% representation in the Metro Barcelona, Central and Girona. 

![PoliceOfficersLocation](https://github.com/navarrof/PolicingCatalonia/assets/54847307/eed9262d-7305-4f9a-9df0-634e1e6206da)

*Figure 3: Number of police officers per area, categorized by gender.*

The Catalonia police divides its officials into the following ranks: Mosso, Caporal, Sergent, Sotsinspector, Inspector, Intendent, and Major. With Mosso being the first basic level and Major being the maximum official degree in the scale. Figure 4 shows the proportion of female officers when considering their rank. From this figure we observe that the average of female representation when considering ranks superior to Capporal decreases even further, averaging a 10%. The biggest difference is when looking at the Metro politana sud area, where the percentage of female officers in high-ranking positions is significantly lower compared to the overall representation of women in the force.

![FemaleProportion](https://github.com/navarrof/PolicingCatalonia/assets/54847307/20fb3cbf-0abd-4aff-b3fc-75f0e8727b89)

*Figure 4: Percentage of women in the police force across various areas, both overall and when accounting for different ranks.*

## 2. Information on Criminality Rates

### 2.1 Evolution of the crimes known by the Catalan Police. 

Figure 5 shows the evolution of known and solved crimes since 2011. The number of crimes appears to exhibit fluctuations from year to year. . We observe a minimum on the crime rates in 2020 and 2021. However, these numbers are evidently influenced by the impacts of the COVID-19 pandemic and should be taken with care. If one compares the solved crimes in 2019 and 2022, we see an overall improvement of a 3.45% in the rate of solved crimes. However, in this figure, variations in population along the years have not be considered.

A more detailed study of the criminality in 2022 is shonw in Figure 6. The coloring lightness variation indicates qualitatively the population in each of the eareas in 2022. From this figure we can also see that the criminality rate (that is, number of known crimes divided by number of population) is the highest in the Metro nord area, and the lowest in the Pirineus area. In 2022 an average of 34.65% of the crimes were solved. The highest proportion of solved crimes took place in the Pirineus area with almost 50% of the crimes solved. It is unfair however to compare the number of solved crimes per area without considering what types of crimes were commited. This will be treated with more detail in the following sections. In red, the comparison between the rate of solved crimes in 2019 and 2022 is shownd. In all the cases there has been an increase in the proportion of solved crimes, indicating the increasing efforts of the police department. 

![SolvedCrimes_year](https://github.com/navarrof/PolicingCatalonia/assets/54847307/c51929bf-f32a-48c9-9265-427f305bd13f)

*Figure 5: Evolution of known and solved crimes in Catalunya since 2011.*

![Regions](https://github.com/navarrof/PolicingCatalonia/assets/54847307/4c563c87-bd63-46fc-8cb4-726ea8a1e973)

*Figure 6: Criminality rate of the different regions of catalonia. The numbers indicate (from top to bottom): number of known crimes divided by number of people living in that area, proportion of solved crimes, comparison of the rate of solved crimes between 2019 and 2022.* 

### 2.2 Types of Crimes in Catalunya.  

Author's note: The results presented in this section should be approached with caution. The classification of the different crimes has been done following the official summaries presented by the Catalan police department [3]. However, in certain instances, the classification of the particular crime was unclear. I relied on my own judgment to classify it, recognizing that my classification may not be entirely accurate. 

The details of the crime classification used in this analysis can be found in:

    “…/PlottingFolders/Section2_KnownCrimes/TypesOfCrimes.py”

Criminal acts in Catalonia are categorized into three different types: Crimes against people, crimes against property and other type of crimes. At the same time, each one of this type of crime has a series of subtypes that one could consider. The following schema shows how the crimes have been clasified for this analysis. In this schema one can also observe some percentages. This percentages indicate the proportion of crimes of this type in 2022 (blue) and 2019 (orange). 

We can observe how the majority of the crimes are against the property, meaning, thefs, robberies, damages, etc. For the crimes against the people, we see that the majority of them are injuries or threats, while the minority are kidnappings, murders or freedom crimes. The other type of crime cathegory include a large variety of crims, for example crimes against the authority, driving related crimes and public security crimes. Among them, the most relevant crimes are the driving crimes and offenses. 

When comparing the 2022 results to the 2019 results, we can observe a reduction on the crimes against the property, while an increase in the crimes against people and the other types of crimes. In particular, we observe an increase in the crimes of sexual nature and the driving related crimes. 

![TypeCrime](https://github.com/navarrof/PolicingCatalonia/assets/54847307/6484ed37-e7b6-4eab-a700-5bba84f1e457)


In order to see if there was any region iin catalonia more prompt to a certain type of crime, a geoghraphical analysis was performed. As a figure of merit, the proportion of crimes per population was used (number of crimes per person). In the following tables we show the areas where the majority and the minority of the crims of a certain type have been comitted. 

## References

[1] https://ca.wikipedia.org/wiki/%C3%80rea_B%C3%A0sica_Policial 

[2] https://mossos.gencat.cat/.content/home/dadesobertes/comissaries/index.html?lang=en 

[3] https://mossos.gencat.cat/ca/els_mossos_desquadra/indicadors_i_qualitat/estadistica/

