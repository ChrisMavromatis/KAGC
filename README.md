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

![Aplha Phase Data Wrangling](/Images/AlphaPhaseDataWrangling.png)

![Beta Phase Data Wrangling](/Images/BetaPhaseDataWrangling.png)

![Split Variables](/Images/SplittingVariables.png)


## Analysis Tools
After establishing the relative sequence in each trench we look for  basic correlations between deposits in each area's trenches. This  process  involved  comparing the deposits and aggregating them into larger units in  terms of their color, compaction, interface properties, inclusions, and assemblage compositions. Our research goals for the stratigraphic analysis also required us to examine individual and aggregated deposits and their assemblages at different spatial resolutions.  We also need a standard way to compare, contrast,  and visualize different aspects of these deposits' assemblages,  especially their chronological distribution.  Given our goals, our approach to stratigraphic interpretation centered on establishing and analyzing deposit assemblage profiles.

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
