# Introduction
This repository contains the Python modules the Kourion Amathous Gate Cemetery Project (KAGC) used to analyze its stratigraphy for the site's final publication ([Publication](https://whitelevy.fas.harvard.edu/publications/city-and-cemetery-excavations-kourion%E2%80%99s-amathous-gate-cemetery-cyprusthe); [Project Webpage](https://www.gla.ac.uk/schools/humanities/research/archaeologyresearch/currentresearch/kourion/)). As a legacy project, the publication team faced several challenges. These included, among others, figuring out the best way to harmonize the multiple recording systems used during the project's field phase and incompletely processed artifact databases. This document outlines the KAGC's approach to dealing with legacy archaeological datasets and how we leveraged the power of Python, R, and Ipython Notebooks to prepare our data for publication (Kluyver2016 et al; Van Rossum & Drake 2022; R Core Team 2021). 

# The KAGC Project's approach to working with legacy archaeological datasets
Most researchers would agree that the reanalysis of legacy data sets has the potential to offer a range of new insights and augment our existing knowledge  (Allison 2008).  Most would also accept that incorporating legacy datasets into a contemporary research framework presents various technical and methodological challenges.  Developing an effective strategy for preparing these datasets for analysis can be daunting.  Arguably, data preparation, or wrangling, is one of the most important aspects of working with legacy and contemporary datasets.  To put it another way,  the more specific a project's research questions are, the more nuanced the data-wrangling and tool development are likely to be. 
In order to get the most out of what was available, the project used  a two-part data-wrangling strategy for preparing its digital data for analysis. We extensively used "Tidy Data" principles as a guide (Broman et al 2018; Ellis & Leek 2018; Wickham 2014; Wickham 2016; Wickham 2019). The "Tidy Data" principles are reasonably straightforward.  They focus on  making data internally consistent, more manageable, and comprehensible when sharing with colleagues.

## Data-Wrangling
The first part of this strategy, or the Alpha phase, is centered on what we can best describe as the generic cleaning of the specialists' databases.  This process primarily focused  on

* correcting spelling issues
* making  sure that  variable code abbreviations were consistent
* removing excess leading and trailing white space from each entry
* identifying compound variables

The second part of our strategy, the Beta phase, was designed to help us address our research questions more efficiently.  One of the project's goals for the stratigraphic analysis was to integrate the discussion of the stratigraphy with relevant information on features, spatial organization, material culture, and human skeletal remains.  We were also interested in how Kourion's inhabitants used the different areas of the  cemetery  over time.  During the Beta phase, the project's research goals directly influenced the data-wrangling process. Ultimately, this required re-coding,  splitting compound variables, aggregating, and reshaping various aspects of  the Alpha phase  "cleaned" datasets.  The results included  additional indexing,  provenience, and chronological  variables.

![Alpha](/Images/AlphaPhaseDataWrangling.png)

![Beta Phase Data Wrangling](/Images/BetaPhaseDataWrangling.png)

![Split Variables](/Images/SplittingVariables.png)


## Analysis Tools
After establishing the relative sequence in each trench we look for  basic correlations between deposits in each area's trenches. This  process  involved  comparing the deposits and aggregating them into larger units (Depositional Units, DUs) in  terms of their color, compaction, interface properties, inclusions, and assemblage compositions. Our research goals for the stratigraphic analysis also required us to examine individual and aggregated deposits and their assemblages at different spatial resolutions.  We also need a standard way to compare, contrast,  and visualize different aspects of these deposits' assemblages,  especially their chronological distribution.  Given our goals, our approach to stratigraphic interpretation centered on establishing and analyzing deposit assemblage profiles.

The Context-DU class' methods manipulate several core variables from the project database to generate additional data for the profile.  These actions range from simple database and spreadsheet filtering operations to more complex ones that involve linking several queries, filters, and mathematical operations together.  

* cdu: All artifacts from the context or Depositional Unit (DU)
* MCLS_Grps: Splits the context or  DU's assemblage into sub-assemblages based on material class
* MCLS_TPQS: TPQ items for each material class from A DU's assemblage
* CC_TPQS: The TPQ item for each of a given DU's Contributing Contexts (CCs)
* UniqueForms: Unique forms present in the DU's assemblage
* ResiualForms: Artifacts earlier than a user-provided cutoff point
* DUCatNos: Items for which the artifact specialists have assigned a catalog number. The catalog numbers 
          correspond to those found in the specialist reports presented in Volume 2 of the KAGC publication.
* DUSmry: Depositional Unit summary that contains 15 variables
  - DU: Depositional Unit (e.g., B503)
  - TPQ: Terminus Post Quen date for the DU's assemblage
  - MMDate: Mean Meadin Date for the DU's assemblage
  - Span: Chronological range of the DU's assemblage
  - TForms: Total number of unique forms from the DU
  - RForms: Residual forms, or the number of forms earlier than 
    the user-supplied res value in the DU's assemblage
  - NRForms: Non-Residual forms, or the number of forms later
    than the user-supplied res value from the DU's assemblage
  - NRF:RF: The ratio of non-residual forms to residual forms in the DU's assemblage
  - Dspan > 100: artifacts that have production spans greater than 100 years from the DU's assemblage
  - Arch: Presence of architectural material in the DU's assemblage
  - Display: Presence of display items in the DU's assemblage
  - P.items:  Presence of personal items in the DU's assemblage
  - P.adorn: Presence of personal adornments in the DU's assemblage
  - Tool:  Presence of tools in the DU's assemblage
  - Production: Presence of artifacts associated with production activities

![Context-DU Class](/Images/Context_DU_Class.png)

# Software and Requirements
The Python class and functions we created for the project used

* Python (3.10.10), Ipython (8.12.0),
  * Python Distibution: Anaconda 3
* Visual Studio Code (1.79.2)
    
## Python Libraries

* scipy: 1.10.0
* matplotlib: 3.7.1
* watermark: 2.4.3
* pandas: 1.5.3
* seaborn: 0.12.2
* re: 2.2.1
* numpy: 1.23.5
* sqlite3: 2.6.0
* gower: 0.1.2


# Usage Instructions
The table below describes the naming convention for the variables used in the project's database. To use the functions and Context-DU class for a different project, either adapt the function and class code to the new database or modify the new database's variable names. Some of the project's functions also extend the Context-DU's methods. For example, the Context-DU's MCLS_TPQS method produces a table that presents the latest opening and closing production dates for each material in the assemblage, among other data. It also serves as the preferred input for the DU_MCLS_TPQ_Plt function, which plots the production spans for the latest item for each artifact type in the assemblage. 


| Field   Name | Field   Description | Field Data Type | Field Length | Comment |
|---|---|---|---|---|
| area | KAGC excavation area | text | 30 |
| name | trench or tomb name | text | 30 |
| tb.tr | trench or tomb number | text | 30 |
| cxn | context number | text | 30 |
| mcls | material class type. : lmp:   lamp. gls: glass. num: coin. cer: non-fine ware ceramics. stn: stone. mtl:   non coin metal. amp: amphora. plst: plaster/stucco. fw: fine ware | text | 30 |
| number | registration number | text | 30 |
| diag | diagnostic item type | text | 30 |
| Cat | catalog number | text | 30 |
| date1 | AD, BC, AD-BC | text | 30 |
| date2 | concatenation of date1, date3,   and date4 | text | 30 |
| date3 | opening production date | integer | 30 |
| date4 | closing production date | integer | 30 |
| type1 | item type | text | 30 |
| type2 | item part | text | 30 |
| type3 | gross functional class | text | 30 |
| type4 | method of manufacture | text | 30 |
| type5 | item color(s) | text | 30 |
| type6 | item material or fabric   description | text | 30 |
| cond | condition | text | 30 |
| burnt | evidence for burning | boolean | 1 |
| join | join with other item | boolean | 1 |
| PL | preserved length | float | 30 |
| PW | preserved width | float | 30 |
| description | item description | text | variable |



# Works Cited
Allison, P. (2008). Dealing with Legacy Data - an introduction. Internet archaeology, (24). [https://doi.org/10.11141/ia.24.8](https://doi.org/10.11141/ia.24.8)

Broman, K. W. and Woo, K. H. (2018). Data organization in spreadsheets. The American Statistician, 72 (1), Taylor & Francis., pp.2-10. [https://doi.org/10.1080/00031305.2017.1375989](https://doi.org/10.1080/00031305.2017.1375989)

Ellis, S. E. and Leek, J. T. (2018). How to share data for collaboration. The American Statistician, 72 (1), Taylor & Francis., pp.53-57. [https://doi.org/10.1080/00031305.2017.1375987](https://doi.org/10.1080/00031305.2017.1375987)

Kluyver, T. et al. (2016). Jupyter Notebooks – a publishing format for reproducible computational workflows. In: Loizides, F. and Schmidt, B. (Eds). 2016. IOS Press. pp.87–90.

R Core Team. (2021). R: A language and environment for statistical computing. Vienna, Austria : R Foundation for Statistical Computing. [https://www.R-project.org/](https://www.R-project.org/)

Van Rossum, G. and Drake, F. L. (2022). Python 3.10 reference manual. Scotts Valley, CA : CreateSpace.

Wickham, H. (2014). Tidy Data. Journal of Statistical Software, 59 (10), pp.1–23.

Wickham, H. (2016). Data analysis. In: Ggplot2: Elegant graphics for data analysis. Cham : Springer International Publishing. pp.189–201. [https://doi.org/10.1007/978-3-319-24277-4_9](https://doi.org/10.1007/978-3-319-24277-4_9)

Wickham, H. et al. (2019). Welcome to the Tidyverse. Journal of Open Source Software, 4 (43), p.1686. [https://doi.org/10.21105/joss.01686](https://doi.org/10.21105/joss.01686)

# Links
* [Project Webpage](https://www.gla.ac.uk/schools/humanities/research/archaeologyresearch/currentresearch/kourion/)
* [Publication](https://whitelevy.fas.harvard.edu/publications/city-and-cemetery-excavations-kourion%E2%80%99s-amathous-gate-cemetery-cyprusthe)
