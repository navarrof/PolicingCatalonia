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

To determine the number of police offices per region. 



Amount of population per police office. 