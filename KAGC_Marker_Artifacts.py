# KAGC Marker Artifacts 2020
"""
This moduel contains lists of KAGC artifacts corresponding to Marker Groups 1, 2, and 3.  See KAGC final publication Chapter 3 Methodology for a full description of these artifact groupings. 

# File Metadata
* Associated Publication: Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volumes 76 & 77, ASOR).

    * Main Publication Chapter(s) that use or mention these Marker Groups: 
    
    Mavromatis, Christopher. Michae Given (2024) Chapter 3 Methodology. Pp: 21-34. In Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volume 76 ASOR)

    Mavromatis, Christopher _et al_ (2024). Chapter 7 Deposition and Dumping in Area A. Pp: 97-126. In  Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volume 76 ASOR).

    Mavromatis, Christopher _et al_. (2024) Chapter 9 The cist Tombs. Pp: 147-200. In  Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volumes 76 ASOR).
    
* File Name: KAGC_Marker_Artifacts.py

* File Format: text

* Software: 
    * Python (3.10.10), Ipython (8.12.0), 
        * Python Distibution: Anaconda 3
    * Visual Studio Code (1.79.2) 

* Hardware: 
    * MacBook Air 10, M1
        * 8 GIG RAM
        * CPU: Apple M1
        * GPU: Apple M1
    * Lennovo IdeaPad 3
        * 12 GIG RAM
        * CPU: 11th Gen Intel i5
        * GPU: Intel TigerLake-LP G2

* Operating System Used to Create File: 
    * Ubuntu Linux 22.04.02 LTS (Kernal 6.8.0-31)
        * 64 bit, X86
    * MacOS 14.5 (Kernel Darwin 23.5.0)
        * 64 bit,  Arm64

* Date of Creation/Last File Update: 
    * Creation:  02 January 2021
    * Last File Update: 01 May 2023

* Processing History: 
    * Analysis of cleaned artifact datasets by Depositional Unit (DU). 

* Required Python Packages:
    * matplotlib: 3.7.1 
    * pandas    : 1.5.3
    * seaborn   : 0.12.2
    * re        : 2.2.1
    * numpy     : 1.23.5
    * sqlite3   : 2.6.0


* Other Project Moduels:
    * KAGC_Context_Class
    * KAGC_Marker_Artifacts
    * KAGC_Depositional_Units
"""

# Marker Group 1
MG1 =  [
    'architectural',
    'architectural',
    'architectural element',
    'reduction',
    'raw material',
    'display',
    'production',
    'production?',
    'inlay',
    'tool']

# Marker Group 2
MG2 = [
    'special purpose',
    'p.item',
    'p.adornment',
    'commemoration']

# Marker Group 3
MG3 =[
    'illumination',
    'storage-processing',
    'transport-storage',
    'tableware',
    'ung',
    'utensil',
    'domestic'
]
