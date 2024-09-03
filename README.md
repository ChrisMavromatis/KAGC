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
| area | KAGC excavation area | text | 30 | Extracted from ‘name’ during cleaning with three levels. A: Area A. B: Area B. E: Area E |
| name | trench or tomb name | text | 30 | Equivalent to ‘Trench/Tomb’ in old and some new specialist databases with minor reformatting, e.g., TRAV -> TRA05 |
| tb.tr | trench or tomb | text | 30 | Extracted from ‘name’ during cleaning with two levels: T: tomb. TR: trench |
|context| context number | text | 30 | Equivalent to ‘Level’ in old and some new specialist databases with minor reformatting, e.g., 1.0 -> 1 |
| cxn | context number | text | 30 | Extracted and generated from ‘name’ and ‘context’ (infra) during cleaning, e.g., TRA01-1 |
| mcls | material class type. : lmp:   lamp. gls: glass. num: coin. cer: non-fine ware ceramics. stn: stone. mtl:   non coin metal. amp: amphora. plst: plaster/stucco. fw: fine ware | text | 30 | |
| number | registration number | text | 30 | Equivalent to ‘Number’ in old database with post-2017 specialist updates |
| diag | diagnostic item type | text | 30 | Extracted from ‘Type1’ if diagnostic form is known, e.g., LRA1 |
| Cat | catalog number | text | 30 | |
| date1 | AD, BC, AD-BC | text | 30 | Extracted during cleaning with 3 levels: BC; BC–AD; AD |
| date2 | concatenation of date1, date3,   and date4 | text | 30 | Generated from Date1, Date3, and Date4 during cleaning |
| date3 | opening production date | integer | 30 | Extracted during cleaning: opening production date with BC dates expressed as a negative number |
| date4 | closing production date | integer | 30 | Extracted during cleaning: closing production date with BC dates expressed as a negative number |
| type1 | object type | text | 30 | |
| type2 | object part | text | 30 | Fragment type or part, e.g., rim |
| type3 | gross functional class | text | 30 | e.g., transport-storage |
| type4 | method of manufacture | text | 30 | e.g., mold-made |
| type5 | item color(s) | text | 30 | |
| type6 | item material or fabric   description | text | 30 | |
| cond | condition | text | 30 | e.g., weathered, pitted, abraded, etc. |
| burnt | evidence for burning | boolean | 1 | Y or N |
| join | join with other item | boolean | 1 | Equivalent to ‘mended’ in new specialist and old databases |
| PL | preserved length | float | 30 |
| PW | preserved width | float | 30 |
| description | item description | text | variable |

## Usage Examples

```Python
#Context-DU Class instance for DU B503
b503 =df.pipe(KAGC_FUN.DU_Select, KAGC_DUS.B503, "B503").pipe(co.Context, res= -50)
```
```
╒════╤═════════╤════════╤════════╤═════════╤════════╤════════╤══════════╤══════════╤═══════╤═════════╤══════════════╤═════════╤═════════╤══════════╤═════════╤═════════════╤═════════╤═════════╤════════════════╤══════════╤═════════╤════════╤══════╤══════╤═════════╤═════════════════════════════════════════════════╤══════╤══════════╕
│    │   index │ area   │ name   │ tb.tr   │ cxn    │ mcls   │ number   │ diag     │ Cat   │ date1   │ date2        │   date3 │   date4 │ type1    │ type2   │ type3       │ type4   │ type5   │ type6          │ cond     │ burnt   │ join   │   PL │ PW   │ date5   │ description                                     │ DU   │   MPDate │
╞════╪═════════╪════════╪════════╪═════════╪════════╪════════╪══════════╪══════════╪═══════╪═════════╪══════════════╪═════════╪═════════╪══════════╪═════════╪═════════════╪═════════╪═════════╪════════════════╪══════════╪═════════╪════════╪══════╪══════╪═════════╪═════════════════════════════════════════════════╪══════╪══════════╡
│  1 │       1 │ B      │ TB10   │ T       │ TB10-2 │ jwl    │ 1476A,B  │ bead     │       │ UnID    │ UnID nan-nan │     nan │     nan │ bead     │         │ p.adornment │         │         │ glass          │ fragment │         │        │      │      │         │                                                 │ B503 │    nan   │
├────┼─────────┼────────┼────────┼─────────┼────────┼────────┼──────────┼──────────┼───────┼─────────┼──────────────┼─────────┼─────────┼──────────┼─────────┼─────────────┼─────────┼─────────┼────────────────┼──────────┼─────────┼────────┼──────┼──────┼─────────┼─────────────────────────────────────────────────┼──────┼──────────┤
│ 10 │      10 │ B      │ TB10   │ T       │ TB10-2 │ jwl    │ TB10/1   │ bead     │ JW15  │ AD      │ AD 1-600     │       1 │     600 │ bead     │ ridged  │ p.adornment │         │         │ gold foil      │          │         │        │      │      │         │                                                 │ B503 │    300.5 │
├────┼─────────┼────────┼────────┼─────────┼────────┼────────┼──────────┼──────────┼───────┼─────────┼──────────────┼─────────┼─────────┼──────────┼─────────┼─────────────┼─────────┼─────────┼────────────────┼──────────┼─────────┼────────┼──────┼──────┼─────────┼─────────────────────────────────────────────────┼──────┼──────────┤
│ 11 │      11 │ B      │ TB10   │ T       │ TB10-2 │ jwl    │ TB10/10  │ hairpin  │       │ UnID    │ UnID nan-nan │     nan │     nan │ hairpin  │ shaft   │ p.adornment │         │         │ bone           │ fragment │         │        │    2 │      │         │ Shaft fragment; circular shaft; d 0.27, pl 2.00 │ B503 │    nan   │
├────┼─────────┼────────┼────────┼─────────┼────────┼────────┼──────────┼──────────┼───────┼─────────┼──────────────┼─────────┼─────────┼──────────┼─────────┼─────────────┼─────────┼─────────┼────────────────┼──────────┼─────────┼────────┼──────┼──────┼─────────┼─────────────────────────────────────────────────┼──────┼──────────┤
│ 13 │      13 │ B      │ TB10   │ T       │ TB10-2 │ jwl    │ TB10/14  │ hairring │       │ UnID    │ UnID nan-nan │     nan │     nan │ hairring │         │ p.adornment │         │         │ elephant ivory │ fragment │         │        │      │      │         │ 14 fragments; plain; h 0.99                     │ B503 │    nan   │
├────┼─────────┼────────┼────────┼─────────┼────────┼────────┼──────────┼──────────┼───────┼─────────┼──────────────┼─────────┼─────────┼──────────┼─────────┼─────────────┼─────────┼─────────┼────────────────┼──────────┼─────────┼────────┼──────┼──────┼─────────┼─────────────────────────────────────────────────┼──────┼──────────┤
│ 14 │      14 │ B      │ TB10   │ T       │ TB10-2 │ jwl    │ TB10/2   │ bead     │       │ UnID    │ UnID nan-nan │     nan │     nan │ bead     │         │ p.adornment │         │         │ glass          │ intact   │         │        │      │      │         │ Intact; sphere; l 0.59, w 0.59                  │ B503 │    nan   │
╘════╧═════════╧════════╧════════╧═════════╧════════╧════════╧══════════╧══════════╧═══════╧═════════╧══════════════╧═════════╧═════════╧══════════╧═════════╧═════════════╧═════════╧═════════╧════════════════╧══════════╧═════════╧════════╧══════╧══════╧═════════╧═════════════════════════════════════════════════╧══════╧══════════╛
```

```Python
#DU Summary
b503.DUSmry()
```
```
╒════╤══════╤═══════╤══════════╤════════╤══════════╤══════════╤═══════════╤══════════╤═══════════════╤════════╤═══════════╤═══════════╤═══════════╤════════╤══════════════╕
│    │ DU   │   TPQ │   MMDate │   Span │   TForms │   RForms │   NRForms │   NRF:RF │   Dspan > 100 │ Arch   │ Display   │ P.items   │ P.adorn   │ Tool   │ Production   │
╞════╪══════╪═══════╪══════════╪════════╪══════════╪══════════╪═══════════╪══════════╪═══════════════╪════════╪═══════════╪═══════════╪═══════════╪════════╪══════════════╡
│  0 │ B503 │   401 │      366 │   1200 │       56 │        7 │        49 │        7 │            40 │ True   │ False     │ True      │ True      │ False  │ True         │
╘════╧══════╧═══════╧══════════╧════════╧══════════╧══════════╧═══════════╧══════════╧═══════════════╧════════╧═══════════╧═══════════╧═══════════╧════════╧══════════════╛
```

```Python
#Latest items from DU B503 by material type
b503.MCLS_TPQS()
```
```
╒══════╤══════╤════════╤════════╤════════╤═══════╤═════════════════════════╤════════════════╤════════════════════╤═════════╤═════════╤═════════╤═════════╤══════════╤════════╤══════════╕
│      │ DU   │ name   │ cxn    │ mcls   │ Cat   │ diag                    │ type1          │ type2              │ date1   │   date3 │   date4 │   Dspan │   MPDate │   EAAD │   EAAD-M │
╞══════╪══════╪════════╪════════╪════════╪═══════╪═════════════════════════╪════════════════╪════════════════════╪═════════╪═════════╪═════════╪═════════╪══════════╪════════╪══════════╡
│   84 │ B503 │ TB13   │ TB13-1 │ trc    │ TC23  │ figurine                │ figurine       │ horse torso        │ BC      │    -300 │    -250 │      50 │   -275   │    701 │    825.5 │
├──────┼──────┼────────┼────────┼────────┼───────┼─────────────────────────┼────────────────┼────────────────────┼─────────┼─────────┼─────────┼─────────┼──────────┼────────┼──────────┤
│ 3074 │ B503 │ TB11   │ TB11-2 │ fw     │ FW184 │ african red slip form 5 │ Plate          │ rim                │ AD      │      50 │     150 │     100 │    100   │    351 │    450.5 │
├──────┼──────┼────────┼────────┼────────┼───────┼─────────────────────────┼────────────────┼────────────────────┼─────────┼─────────┼─────────┼─────────┼──────────┼────────┼──────────┤
│ 1689 │ B503 │ TB18   │ TB18-2 │ num    │ CN16  │ Arcadius, Honorius      │ coin           │ intact             │ AD      │     395 │     401 │       6 │    398   │      6 │    152.5 │
├──────┼──────┼────────┼────────┼────────┼───────┼─────────────────────────┼────────────────┼────────────────────┼─────────┼─────────┼─────────┼─────────┼──────────┼────────┼──────────┤
│ 1821 │ B503 │ TB14   │ TB14-1 │ amp    │ AM63  │ LRA 1                   │ LRA 1          │ HW                 │ AD      │     401 │     450 │      49 │    425.5 │      0 │    125   │
├──────┼──────┼────────┼────────┼────────┼───────┼─────────────────────────┼────────────────┼────────────────────┼─────────┼─────────┼─────────┼─────────┼──────────┼────────┼──────────┤
│ 2155 │ B503 │ TB14   │ TB14-1 │ gls    │       │ stemmed goblet          │ stemmed goblet │ base               │ AD      │     401 │     600 │     199 │    500.5 │      0 │     50   │
├──────┼──────┼────────┼────────┼────────┼───────┼─────────────────────────┼────────────────┼────────────────────┼─────────┼─────────┼─────────┼─────────┼──────────┼────────┼──────────┤
│   27 │ B503 │ TB14   │ TB14-1 │ jwl    │ JW29  │ buckle                  │ buckle         │ ogival with tongue │ AD      │     401 │     600 │     199 │    500.5 │      0 │     50   │
├──────┼──────┼────────┼────────┼────────┼───────┼─────────────────────────┼────────────────┼────────────────────┼─────────┼─────────┼─────────┼─────────┼──────────┼────────┼──────────┤
│  640 │ B503 │ TB18   │ TB18-2 │ lmp    │ LP51  │ Egyptian?               │ lamp           │ half preserved     │ AD      │     401 │     700 │     299 │    550.5 │      0 │      0   │
╘══════╧══════╧════════╧════════╧════════╧═══════╧═════════════════════════╧════════════════╧════════════════════╧═════════╧═════════╧═════════╧═════════╧══════════╧════════╧══════════╛
```

```Python
#Plotting production spans for the latest artifact types from DU B503
KAGC_FUN.DU_MCLS_TPQ_Plt(b503, save_plot="N", out_ti=" ", fext=" ", start= -500, stop=1000)
```
![Production Span Graph](/Images/ProductionSpanGraph.png)

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
