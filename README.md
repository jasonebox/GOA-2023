# Arctic InSitu versus GRACE (ArcticInSituvGRACE) 2023
updated Arctic land ice mass balance output after:

	Box, J. E., Colgan, W. T., Wouters, B., Burgess, D. O., O’Neel, S., Thomson, L. I., & Mernild, S. H. (2018). Global sea-level contribution from Arctic land ice: 1971–2017. Environmental Research Letters: ERL [Web Site], 13(12), 125012. https://doi.org/10.1088/1748-9326/aaf2ed 

The base data is from the WGMS compilation https://wgms.ch/data_databaseversions/ adding 'latest values' from https://wgms.ch/latest-glacier-mass-balance-data/

## GLAMBIE info
Lead Author - First Name, Surname*
Jason,Box
Lead Author - Email Address*
jeb@geus.dk
Co-author - Name(s). Please separate multiple names with ","
William T Colgan, Bert Wouters, David O Burgess, Shad O'Neel, Laura I Thomson
Co-author - Email Address(es). Please separate multiple addresses with ","
wic@geus.dk,b.wouters@uu.nl,david.burgess@nrcan-rncan.gc.ca,shad.oneel@gmail.com,l.thomson@queensu.ca

Group Name
ArcticInSituvGRACE
Danish Energy Agency and AMAP

Sponsoring Agency (project sponsor)

## Regional Notes
Russian High Arctic (RHI) is here estimated based on regression with Svalbard (Svalbard vs RHI slope 1.1236, that is RHI mass balance is estimated to be 12% more negative than that of Svalbard) after RHI −22 GT/y from the 2000 to 2017 period (Sommer et al 2022):
Sommer, C., Seehaus, T., Glazovsky, A., and Braun, M. H.: Brief communication: Increased glacier mass loss in the Russian High Arctic (2010–2017), The Cryosphere, 16, 35–42, https://doi.org/10.5194/tc-16-35-2022, 2022.

Iceland can be extended before 1988

## Methods
From Box et al. 2018: 
"Semi-empirical regional total mass balance assessment
Akin to Dowdeswell et al (1997) and Meier et al (2007), we aggregate in situ glacier mass balance time series to upscale to regional values. We enhance the approach by an absolute calibration to GRACE estimates and by representing a later time period (the 2000s onward) with more pronounced climate change impacts on glacier mass balance.
For each in situ mass balance record (i) having at least 80% of available data 1971–2017 (47 years), we calculate the 2003–2015 average (DBa) and standard deviation (s) and 1971–2017 anomalies (DBa’) rela- tive to the W08 (years 2003–2015) baseline. Each record is divided by the standard deviation, i.e. stan- dardized as:
DBa-prime i,y = (DBa i,y - DBa i,2003-2015) /sBa i,2003-2015
The individual glacier DBa¢i values are averaged over six regions (all but Greenland is) (table 1) and multiplied by the W08 regional GRACE mass balance averages (table 1). By this approach, we estimate mass balance totals for each region and year in the 1971–2017 interval in a way that is scaled to the GRACE mass balance retrievals. Lacking in situ mass balance record from Arctic Canada South, table 1 Arc- tic Canada North and South mass balance values are summed into a single regional value and thus the com- bined region is represented by four Arctic in situ mass balance records."
The in-situ data are available for a longer period than GRACE, so the regional mass balance can be estimated for the period before GRACE using the regression parameters.

Update of GRACE data processing in J Box files : /GRACE/Wouters/GRACE_Arctic_Wouters/GRACE_Arctic.py

Arctic Canada, North and South are separated based on the average GRACE mass balance ratio (r) between 2002 and 2015, r = 0.6557, i.e. South = all Arctic Canada * r, and North = all Arctic Canada * 1-r

### GRACE data notes
The approach could be updated by making regressions vs regional z-scores and a longer GRACE time series


## Greenland
Greenland mass balance is from:

	Mankoff, Ken; Fettweis, Xavier; Solgaard, Anne; Langen, Peter; Stendel, Martin; Noël, Brice; van den Broeke, Michiel R.; Karlsson, Nanna; Box, Jason E.; Kjeldsen, Kristian, 2021, "Greenland ice sheet mass balance from 1840 through next week", https://doi.org/10.22008/FK2/OHI23Z, GEUS Dataverse, V449

	Mankoff, K. D., Fettweis, X., Langen, P. L., Stendel, M., Kjeldsen, K. K., Karlsson, N. B., Noël, B., van den Broeke, M. R., Solgaard, A., Colgan, W., Box, J. E., Simonsen, S. B., King, M. D., Ahlstrøm, A. P., Andersen, S. B., and Fausto, R. S.: Greenland ice sheet mass balance from 1840 through next week, Earth Syst. Sci. Data, 13, 5001–5025, https://doi.org/10.5194/essd-13-5001-2021, 2021. doi: 10.5194/essd-13-5001-2021
