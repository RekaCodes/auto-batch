# Auto Batch
Auto Batch groups (or batches) large amounts of data into separate files. There are only two parameters, data and group. Just give Auto Batch a data set and tell it how you would like to set up your groupings. 

Auto Batch uses the pandas library to handle importing, indexing, and exporting data. It also uses the os library create an <i>/export</i> folder to house all outputs.

Real-world application of this app involves filtering and indexing a confidential data set into batches to disseminate to different audiences, such as batching department-specific data from confidential HR and Financial data to be sent only to the respective managers.

An example using the FIFA19 Player Data Set is included. Using Auto Batch, we can sort FIFA 19 players by Nationality and export unique CSV files for each of the 164 contained nationalities where each file contains only the data of the players from that nation. You could also use it to batch by team; however, that would require converting all characters to ASCII and is beyond the scope of this apps intended use.


