## Data analysis using SQLite

Author's Note: This document can be subject to changes. Current work: building a relational database with all the information. 

In this file, I summarize the SQL queries that would be necessary to perform the same data analysis as the one performed with **python (pandas)**. The free [SQL OnLine IDE](https://sqliteonline.com/) was used to easily load data and query it using SQL lite commands. Due to the limitations on the upload size of the data, a reduced version of the data files was used. This reduced version can be found in: 

     DataFiles/ReducedFiles_forMysql 

Using this data does not provide a full description of the exploratory analysis, however, the query commands would be the same when analyzing the full database. 

The .csv files were loaded as tables, with the first column being the table name. 

### 1. Organizational Data

Firstly, we want to obtain the amount of population per territory, as well as the population per basic police area. 

    SELECT regio_c, regio_pob FROM Regions_policials_Poblacio
    SELECT abp_d, abp_pob from Arees_Basiques_Policials_Poblacio

To determine the number of police offices per region, we only need to change the name of the region (regio_c) in the following query.  

    SELECT COUNT(*) from Comissaries_de_districte WHERE regio_c = "Metro Barcelona"

To calculate the amount of population per police station we divide the population by the number of police stations in each region: 

    SELECT (SELECT regio_pob FROM Regions_policials_Poblacio WHERE Regions_policials_Poblacio.REGIO_C = "MetroBarcelona") / (SELECT COUNT(*) from Comissaries_de_districte WHERE regio_c = "Metro Barcelona")

This section also includes a study of the number of police officers per territorial area and its demographical study. For that, the  PersonalOperatiu file was used. First, we obtain the total number of police officers per region, adding all the different cathegories:

    SELECT  "Mosso/a" + "Caporal/a" + "sergent/a" + "sotsinspector/a" + "inspector/a" + "comissari/ària" + "Major" FROM Personal_operatiu WHERE any = 2022 AND Àmbit_territorial = "RP Central"

    






SELECT * from Personal_operatiu where Personal_operatiu.any = 2022




Now we do the same as before but separating between female and male police officers: 





