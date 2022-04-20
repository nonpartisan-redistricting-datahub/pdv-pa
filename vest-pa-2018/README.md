# vest-pa-2018

Our final validation report for this dataset is available [here](https://redistrictingdatahub.org/dataset/vest-2018-pennsylvania-precinct-and-election-results/). 

We do not have the raw data sources available on this Github due to file constraints, but we are happy to share them if needed. 

Please reach out to info@redistrictingdatahub.org to reach our support team if you have any questions.


## **Raw from source:**
- File: VEST PA 18 data file
  - Online: [Harvard Dataverse Link](https://dataverse.harvard.edu/file.xhtml?fileId=4195269&version=33.0)
  - AWS: `pa_2018.zip` (available upon request)
  - Accessed: 04/02/21
  - Note:

- File: VEST PA 18 documentation file
  - Online: [Harvard Dataverse Link](https://dataverse.harvard.edu/file.xhtml?fileId=4366213&version=33.0)
  - AWS: `documentation.txt` (available upon request)
  - Accessed: 04/02/21
  - Note:

- File: PA Precinct-Level Election Results
  - Online: [Open Elections Github Link](https://github.com/openelections/openelections-data-pa)
  - AWS: `openelections-data-pa-master` (available upon request)
  - Accessed: 04/02/21
  - Note: I downloaded the entire notebook and filtered down to just the 2018 results.

- File: U.S. Census Bureau's 2020 Redistricting Data Program Phase 2 release
  - Online: [PA Page](https://www.census.gov/geo/partnerships/pvs/partnership19v2/st42_pa.html)
  - AWS: `Census` (available upon request)
  - Accessed: 04/02/21
  - Note: These can only be downloaded 5 at a time, I downloaded the data for all counties and put all the counties into one folder.

- File: Allegheny County Shapefile
  - Online: [Allegheny County GIS](https://openac-alcogis.opendata.arcgis.com/datasets/faaf42d7eaa041cb9fa623ac7b42f475_0?geometry=-81.009%2C40.251%2C-79.031%2C40.617)
  - AWS: `Allegheny_County_Voting_District_Boundaries-shp` (available upon request)
  - Accessed: 04/13/21
  - Note:

- File: Cambria Canvass Report
  - Online: [Cambria County](http://elections.cambriacountypa.gov/Elections.Webclient/Default.aspx?PageLayout=BYPRECINCT&Election=28&Precinct=232)
  - AWS: `Cambria` (available upon request)
  - Accessed: 04/27/21

- File: Northumberland Canvass Report
  - Online: [County of Northumberland](https://www.norrycopa.net/index.php/2018-results/)
  - AWS: `Northumberland` (available upon request)
  - Accessed: 04/27/21

- File: Crawford Canvass Report
  - Online: [Crawford County](https://www.crawfordcountypa.net/VoterServices/Documents/GeneralArchives/2018_General_Results.pdf)
  - AWS: `Crawford` (available upon request)
  - Accessed: 04/27/21

- File: Elk Canvass Report
  - Online: [Elk County](https://www.co.elk.pa.us/images/Elections/2018_General_Election.pdf)
  - AWS: `Elk` (available upon request)
  - Accessed: 04/27/21

- File: Forest Canvass Report
  - Online: [Forest County](http://cms6.revize.com/revize/forestcounty/departments/docs/November%202018%20Election%20Results.pdf)
  - AWS: `Forest` (available upon request)
  - Accessed: 04/27/21

- File: Lawrence Canvass Report
  - Online: [Lawrence County](https://lawrencecountypa.gov/wp-content/uploads/2018/12/nov2018pre-official.pdf)
  - AWS: `Lawrence` (available upon request)
  - Accessed: 04/27/21

- File: Lycoming Canvass Report
  - Online: [Lycoming County](http://www.lyco.org/Portals/1/VoterServices/Documents/2018%20General%20Election%20Precinct%20Results.pdf)
  - AWS: `Lycoming` (available upon request)
  - Accessed: 04/27/21

- File: Montgomery Canvass Report
  - Online: [Montgomery County](https://www.montcopa.org/ArchiveCenter/ViewFile/Item/4680)
  - AWS: `Montgomery` (available upon request)
  - Accessed: 04/27/21

- File: Susquehanna Canvass Report
  - Online: [Susquehanna County](http://www.susqco.com/Dept/Voter/Documents/2018-General-Unofficial-Precinct-Report.pdf)
  - AWS: `Susquehanna` (available upon request)
  - Accessed: 04/27/21

- File: Juniata Canvass Report
  - Online: [Juniata County](https://www.juniataco.org/wp-content/uploads/Precinct-Report-Nov2018.pdf)
  - AWS: `Juniata` (available upon request)
  - Accessed: 04/27/21

- File: Montour Canvass Report
  - Online: [Montour County](http://www.montourco.org/SiteCollectionDocuments/district.pdf)
  - AWS: `Montour` (available upon request)
  - Accessed: 04/27/21

- File: Northumberland Canvass Report
  - Online: [Northumberland County](https://www.norrycopa.net/index.php/2018-results/)
  - AWS: `Northumberland` (available upon request)
  - Accessed: 04/27/21

## **File processing:**

- `VEST_PA_18_replication.ipynb` - documentation in comments and markdown cells