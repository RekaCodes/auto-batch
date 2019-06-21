# Auto Batch
Auto Batch groups (or batches) large amounts of data into separate files. There are only two parameters, data and group. Just give Auto Batch a data set and tell it how you would like to set up your groupings. 

## Required Dependencies
Auto Batch uses the <b>pandas</b> library to handle importing, indexing, and exporting data. It also uses the <b>os</b> library create an <i>/export</i> folder to house all outputs.

Real-world application of this app involves filtering and indexing a confidential data set into batches to disseminate to different audiences, such as batching department-specific data from confidential HR and Financial data to be sent only to the respective managers.

## Example
An example using the FIFA19 Player Data Set is included. Using Auto Batch, we can sort FIFA 19 players by Nationality and export unique CSV files for each of the 164 contained nationalities where each file contains only the data of the players from that nation. 


## Limitations
There are certain limitations in the current iteration. Using the FIFA data set, you cannot batch by team name as it would require converting all characters to ASCII and is beyond the scope of this apps intended use, so I don't have any plans to incorporate that functionality. Also, any date (or datetime) groupings would require an update. I may eventually find need of this and add it later.


