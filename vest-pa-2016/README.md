# vest-pa-2016 

Our final validation report for this dataset is available [here](https://redistrictingdatahub.org/dataset/vest-2016-pennsylvania-precinct-and-election-results/). 

We do not have the raw data sources available on this Github due to file constraints, but we are happy to share them if needed. 

Please reach out to info@redistrictingdatahub.org to reach our support team if you have any questions.

## **Raw from source:**
- File: VEST PA 16 data file
  - Online: [Harvard Dataverse Link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/NH5S2I)
  - AWS: `pa_2016.zip` (available upon request)
  - Accessed: 04/22/21
  - Note:

- File: VEST PA 16 documentation file
  - Online: [Harvard Dataverse Link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/NH5S2I)
  - AWS: `documentation.txt` (available upon request)
  - Accessed: 04/22/21
  - Note:

- File: PA Precinct-Level Election Results
  - Online: [Open Elections Github Link](https://github.com/openelections/openelections-data-pa)
  - AWS: `openelections-data-pa-master` (available upon request)
  - Accessed: 04/02/21
  - Note: I downloaded the entire notebook and filtered down to just the 2016 results.

- File: U.S. Census Bureau's 2020 Redistricting Data Program Phase 2 release
  - Online: [PA Page](https://www.census.gov/geo/partnerships/pvs/partnership19v2/st42_pa.html)
  - AWS: `Census` (available upon request)
  - Accessed: 04/21/21
  - Note: These can only be downloaded 5 at a time, I downloaded the data for all counties and put all the counties into one folder.

- File: Northampton Canvass Report
  - Online: [Northampton County](https://www.northamptoncounty.org/CTYADMN/ELECTNS/Election%20Results/Archives/Nov%208,%202016%20Results%20by%20Precinct.pdf)
  - AWS: `Northampton` (available upon request)
  - Accessed: 05/05/21

- File: Susquehanna Canvass Report
  - Online: [Susquehanna County](http://www.susqco.com/Dept/Voter/Pages/Election-Results.aspx)
  - AWS: `Susquehanna` (available upon request)
  - Accessed: 05/05/21
  - Note: Click on "2016 General Unofficial Canvass Report"

- File: PA 2011-2018 Congressional District Shapefile
  - Online: [Redistricting Data Hub](https://redistrictingdatahub.org/dataset/pennsylvania-congressional-districts-2011-to-2018/)
  - AWS: `pa_cong_2011_to_2018` (available upon request)
  - Accessed: 05/05/21
  
## **File processing:**

- 'VEST_PA_16_replication.ipynb' - documentation in comments and markdown cells