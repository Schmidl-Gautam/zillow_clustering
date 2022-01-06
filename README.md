# Zillow Clustering Project
This repo contains my Zillow log error clustering project with Codeup.

## About

### Goal
## TO DO

### Description
## TO DO

### Initial Questions
## TO DO
1)
2)
3)
4)

### Data Dictionary

|Index | Column Name | Description | Row Count 
|---|---|---|---|
|0 |  parcelid                      | Unique identifier for parcels (lots)                                                  |69519
|1 |  bathroomcnt                   | Number of bathrooms in home including fractional bathrooms                            |69519
|2 |  bedroomcnt                    | Number of bedrooms in home                                                            |69519
|3 |  calculatedfinishedsquarefeet  | Calculated total finished living area of the home                                     |69519
|4 |  fips                          | Federal Information Processing Standard code                                          |69519
|5 |  latitude                      | Latitude of the middle of the parcel multiplied by 10e6                               |69519
|6 |  longitude                     | Longitude of the middle of the parcel multiplied by 10e6                              |69519
|7 |  lotsizesquarefeet             | Area of the lot in square feet                                                        |69519
|8 |  rawcensustractandblock        | Census tract and block ID combined - also contains blockgroup assignment by extension |69519
|9 |  regionidcity                  | City in which the property is located (if any)                                        |69519
|10|  regionidcounty                | County in which the property is located                                               |69519
|11|  regionidzip                   | Zip code in which the property is located                                             |69519
|12|  roomcnt                       | Total number of rooms in the principal residence                                      |69519
|13|  yearbuilt                     | The Year the principal residence was built                                            |69519
|14|  structuretaxvaluedollarcnt    | The assessed value of the built structure on the parcel                               |69519
|15|  taxvaluedollarcnt             | The total tax assessed value of the parcel                                            |69519
|16|  assessmentyear                | The year of the property tax assessment                                               |69519
|17|  landtaxvaluedollarcnt         | The assessed value of the land area of the parcel                                     |69519
|18|  taxamount                     | The total property tax assessed for that assessment year                              |69519
|19|  censustractandblock           | Census tract and block ID combined - also contains blockgroup assignment by extension |69519
|20|  logerror                      |log(zestimate) - log(sale price)                                                       |69519
|21|  transactiondate               |Transaction date for the property                                                      |69519
|22|  county                        |County the property is located.                                                        |69519


## TO DO
<table>
<thead><tr>
<th>Target</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>h</td>
<td>B</td>
</tr>
</tbody>
</table>

<table>
<thead><tr>
<th>Variable</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>b</td>
<td>H</td>
</tr>
<tr>
<td>b</td>
<td>H</td>
</tr>
<tr>
<td>s</td>
<td>S</td>
</tr>
<tr>
<td>y</td>
<td>Y</td>
</tr>
<tr>
<td>f</td>
<td>C</td>
</tr>
<tr>
<td>c</td>
<td>C</td>
</tr>
</tbody>
</table>

### Steps to Reproduce
## TO DO
You will need an env.py file that contains the hostname, username, and password of the MySQL database that contains the Zillow Housing data. The env.py file will need to be in the repository and filename verified or placed in the git ignore. Clone this repo and ensure acquire.py and prepare.py are on your local machine. Additionally, verify env.py is in the git ignore to ensure security of your login information. The technologies used in this project are Python 3.8.11, Pandas 1.3.4, MatPlotLib 3.5.0, Seaborn 0.11.2, Scipy 1.7.1, and SkLearn 1.0.1. The notebook named report.ipynb should run.

### Plan
## TO DO
The plan is to acquire the data either from a CSV or the MySQL database and perform some preparation steps. Then, I  will do some visualizations and compliment them with some statistical tests. Finally, I will do some clustering... I will fit on the training data and check for overfitting on with the validation data. I will then pick the best model to test and move into production. I will then discuss some recommendations and next steps I would like to do with this project.