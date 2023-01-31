https://wgms.ch/data_databaseversions/

Ciao Jason,

for an overview of individual glacier timeseries, you best use the FoG browser:
https://experience.arcgis.com/experience/836c66d14c8b410f940355056ddb1bf8

for selecting your own subset of glaciers, it is best to download the latest version of the FoG database:
https://wgms.ch/data_databaseversions/
and combine the data from the different tables (stored as separate csv files). The table GLACIER contains the static information, e.g. NAME, LAT, LON, GLACIER_REGION_CODE. the primary key linking tables is the WGMS_ID (which is a historically grown numeric identifier with limited meaning).

a full description of all data fields of the FoG database is available here:
https://wgms.ch/downloads/FoG_Submission_instructions.pdf

this is all summarized under: https://wgms.ch/data-exploration/

you may just write to wgms@geo.uzh.ch and order your personal data subset for free.

cheers,
Michael Zemp