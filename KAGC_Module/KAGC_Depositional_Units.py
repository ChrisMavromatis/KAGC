# KAGC Depositional Units V2
# Chris Mavromatis 2023

"""
This moduel contains the Contributing Contexts (CC) for each Depositional Unit (DU) studied by the KAGC project for the final publication. See KAGC final publication Chapter 3 Methodology for a full description of the prpject organised and determined these stratigraphic units.

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

# Area A 

A001 = ['TRA03-0', 'TRA04-0']

A002 = ['TRA09-0',
        'TRA09-51.1',
         'TRA10-0',
         'TRA10-55.1',
         'TRA12-52.2',
         'TRA12-0',
         'TRA13-0',
         'TRA13-51.2',
         'TRA13-51.3',
         'TRA13-51.1']

A003 = ['TRA13-52.1']

A004 = ['TRA09-52.1', 'TRA13-53.1']

A005 = ['TRA12-52.2', 'TRA12-1', 'TRA13-54.1']

A006 = ['TRA09-56.1']

A007 = ['TRA05-0', 'TRA05-BLK-0']

A008 = ['TRA12-2', 'TRA12-52.1', 'TRA12-52.3']

A009 = ['TRA01-EE-037',
        'TRA01-EE-038',
         'TRA01-EE-039',
         'TRA01-EE-041',
         'TRA01-EE-042',
         'TRA01-EE-043',
         'TRA01-EE-045',
         'TRA01-EE-046',
         'TRA01-EE-047',
         'TRA01-EE-048',
         'TRA01-EE-049',
         'TRA01-EE-053']

A010 = ['TRA01-EE-040', 'TRA01-EE-044']

A011 = ['TRA01-EE-051', 'TRA01-EE-054']

A012 = ['TRA10-51.1', 'TRA10-51.2']

A013 = ['TRA10-1']

A014 = ['TRA02-0',
        'TRA02-0.1',
         'TRA02-0.2',
         'TRA02-0.3',
         'TRA02-0.4',
         'TRA02-0.5',
         'TRA02-0.6',
         'TRA07-0',
         'TRA07-0',
         'TRA08-0']

A015 = ['TRA02-1.1',
         'TRA02-1.2',
         'TRA02-1.3',
         'TRA02-1.5',
         'TRA02-1.6',
         'TRA07-1',
         'TRA08-1']

A016 = ['TRA11-0']

A017 = ['TRA07-2', 'TRA08-3']

A018 = ['TRA09-1.1', 'TRA09-1.2', 'TRA09-1.3', 'TRA09-1.4']

A019 = ['TRA05-2', 'TRA05-2.1', 'TRA05-2.2', 'TRA05-2.3']

A020 = ['TRA05-3', 'TRA05-3.1']

A021 = ['TRA05-4']

A022 = ['TRA09-54.1']

A501 = ['TA01-0']

A601 = ['TRA01-0']

A602 = ['TRA01-1']

A603 = ['TRA01-2']

A801 = ['TRA02-0.7', 'TRA07-3']

A901 = [ 'TRA01-EE-011',
         'TRA01-EE-015',
         'TRA01-EE-050',
         'TRA01-EE-007',
         'TRA01-EE-023',
         'TRA01-EE–0.200',
         'TRA01-EE-024',
         'TRA01-EE-025',
         'TRA06-1',
         'TRA06-2',
         'TRA06-3',
         'TRA06-3.3',
         'TRA06-4',
         'TRA06-4.1',
         'TRA06-5',
         'TRA06-5.2',
         'TRA06-5.3',
         'TRA06-6',
         'TRA06-6.3',
         'TRA06-7',
         'TRA06-8',
         'TRA06-9',
         'TRA06-10',
         'TRA06-11']

A902 = [ 'TRA01-EE-001',
         'TRA01-EE-002',
         'TRA01-EE-003',
         'TRA01-EE-010',
         'TRA01-EE-013',
         'TRA01-EE-016',
         'TRA01-EE-019',
         'TRA01-EE-004',
         'TRA01-EE-005',
         'TRA01-EE-006',
         'TRA01-EE-008',
         'TRA01-EE-009']

A903 = ['TRA01-EE-026',
         'TRA01-EE-027',
         'TRA01-EE-028',
         'TRA01-EE-029',
         'TRA01-EE-029',
         'TRA01-EE-031']




# Area B

# B001 =

B002 = ['TRB01-0',
         'TRB02-0',
         'TRB03-0',
         'TRB04-0',
         'TRB05-0',
         'TRB06-0',
         'TRB07-0',
         'TRB08-0',
         'TRB08-0.1',
         #'TRB08-0.1',
         'TRB09-1',
         'TRB13-0',
         'TRB17-1',
         'TRB19-0']

B501 = ['TB01-0',
         'TB02-0',
         'TB03-0',
         'TB04-0',
         'TB05-0',
         'TB06-0',
         'TB06-0.1',
         'TB09-0',
         'TB10-0',
         'TB11-0',
         'TB12-0',
         'TB13-0',
         'TB14-0',
         'TB15-0',
         'TB16-0',
         'TB17-0',
         'TB18-0',
         'TB19-0',
         'TB20-0',
         'TB21-0']

B502 = ['TB08-3.2',
         'TB05-1',
         'TB10-1',
         'TB11-1',
         'TB15-1',
         'TB17-1',
         'TB18-1',
         'TB20-1',
         'TB21-1']

B503 = [ 'TB05-2',
        'TB08-4',
         'TB09-0.1',
         'TB10-2',
         'TB11-2',
         'TB12-1',
         'TB13-1',
         'TB14-1',
         'TB15-2',
         'TB16-1',
         'TB17-2',
         'TB18-2',
         'TB20-2',
         'TB21-2']

B504 = ['TB08-1.0']

B505 = ['TB08-2.1']

B506 = ['TB08-2.2']

B507 = ['TB08-3.1']

B599 = ['TB08-0', 'TB07-0']

B901 = ['TRB09-0',
         'TRB10-0',
         'TRB11-0',
         'TRB11-0.1',
         'TRB11-1.6',
         'TRB12-0',
         'TRB14-0',
         'TRB15-0',
         'TRB16-0',
         'TRB17-0',
         'TRB18-0',
         'TRB20-0',
         'TRB15-BLK-0', 
         'TRB11-BLK-0',
         'TRB12-BLK-0',
         'TRB10-BLK-0',
         'TRB14-BLK-0',
         'TRB17-BLK-0']

# Area E

E501 = ['TE20-0', 
         'TE21-0', 
         'TE22-0']

E502 = ['TE20-1', 'TE22-1']

E503 = ['TE20-2', 'TE22-2']


# Individual contexts

A09_002 = ['TRA09-1.1', 
           'TRA09-1.2', 
           'TRA09-1.3', 
           'TRA09-1.4']

# work surface?
A09_003 = ['TRA09-52.1']

# FA001 kiln plaster and bisection
A09_004 = ['TRA09-55.1']

A09_005 = ['TRA09-57.1']

A09_008 = ['TRA09-53.1']

A12_002 = ['TRA12-51.1']

A10_003 = ['TRA10-52.1',
           'TRA10-54.1', 
           'TRA10-2']


# FA001 Super Structure
FA001_SS = [
        'TRA09-57.1',
        'TRA12-51.1']

FA001_BS = ['TRA09-0.750']

# FA004

FA004 = ['TRA08-3.1']

# fill in pry holes
A12_005 = ['TRA12-60.1']

A13_005 = ['TRA13-60.1']

# TRA01 spoil tip
A01SP = ['TRA01-ST--99', 
         'TRA01-SP-0', 
         'TRA01-ST-nan']

# TRA02 overhang
A02OH = ['TRA02-OH-0', 
         'TR02-OH-nan']

# Surface finds
A_S = ['A-Surf--1']


# Drain around TB06
TB06DR = ['TRB07-TB06-DR-0']

# Baulks
blk = ['TRA01-BLK-nan', 
       'TRA03-BLK-0', 
       'TRA03-BLK-nan',
       'TRA01-BLK-0', 
       #'TRA05-BLK-0',
       'TRA07-BLK-0',
       'TRA08-BLK-0',
      #'TRB15-BLK-0', 
      #'TRB11-BLK-0', 
       'TRB07-BLK-0', 
      #'TRB12-BLK-0',
      #'TRB10-BLK-0', 
       'TRB05-BLK-0', 
      #'TRB14-BLK-0',
      #'TRB17-BLK-0'
      ]
       
       
       
#Excluded

#Have to look at TB01, TB06, and TRA05-? which is a TC#

exc = ['TRA01-EE-?', 
       'TR07-nan', 
       'TRA05-?', 
       'TB12-nan', 
       'TRA01-EE-BLK-nan', 
       'TB01-nan',
       'TB06-nan',
       'TRA04-nan',
       'TRA02-nan',
       'TRA01-nan', 
       'TRA02-nan', 
       'TRA01-EE-nan']

#Area B Depositional Sequence 1

BDS1 =['TRB01-0',
         'TRB02-0',
         'TRB03-0',
         'TRB04-0',
         'TRB05-0',
         'TRB06-0',
         'TRB07-0',
         'TRB08-0',
         'TRB08-0.1',
         #'TRB08-0.1',
         'TRB09-1',
         'TRB13-0',
         'TRB17-1',
         'TRB19-0', 
         'TB01-0',
         'TB02-0',
         'TB03-0',
         'TB04-0',
         'TB05-0',
         'TB06-0',
         'TB06-0.1',
         'TB09-0',
         'TB10-0',
         'TB11-0',
         'TB12-0',
         'TB13-0',
         'TB14-0',
         'TB15-0',
         'TB16-0',
         'TB17-0',
         'TB18-0',
         'TB19-0',
         'TB20-0',
         'TB21-0']
