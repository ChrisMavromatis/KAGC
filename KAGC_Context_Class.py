#!/usr/bin/env python3

# KAGC Stratiraphic Analysis DU Context class V3
# Christopher Mavromatis 2023

"""
Provides a mid-level framework for the analysis of a Dataframe comprised of either a KAGC context or a Depositional Unit. 

# File Metadata
* Associated Publication: Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volumes 76 & 77, ASOR).

    * Main Publication Chapter(s) that use or mention this class: 
    
    Mavromatis, Christopher. Michae Given (2024) Chapter 3 Methodology. Pp: 21-34. In Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volume 76 ASOR)

    Mavromatis, Christopher _et al_ (2024). Chapter 7 Deposition and Dumping in Area A. Pp: 97-126. In  Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volume 76 ASOR).

    Mavromatis, Christopher _et al_. (2024) Chapter 9 The cist Tombs. Pp: 147-200. In  Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volumes 76 ASOR).
    
* File Name: KAGC_Context_Class.py (ContextObjects)

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
    * pandas    : 1.5.3
    * numpy     : 1.23.5


* Other Project Moduels:
    * KAGC_Functions
    * KAGC_Marker_Artifacts
    * KAGC_Depositional_Units
"""


class Context():
    """
    The Context class played a crucial role in the KAGC's analysis framework 
    as it is the main way the project modeled stratigraphic contexts and Depositional Units.

    The Context class contains several main methods:
        * cdu: All artifacts from the context or Depositional Unit (DU)
        * MCLS_Grps: Splits the context of  DU's assemblage into sub-assemblages based on material class
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

    The Context Class contains three secondary methods:
        * MKG1: Returns a subset of the DU's assemblage comprised of items associated 
          with Marker Group 1 artifact (See, Vol. 1 Chapter 3 Fig. 3.3)
        * MKG2: Returns a subset of the DU's assemblage comprised of items associated 
          with Marker Group 2 artifacts (See, Vol. 1 Chapter 3 Fig. 3.3)
        * MKG3: Returns a subset of the DU's assemblage comprised of items associated 
          with Marker Group 3 artifacts (See, Vol. 1 Chapter 3 Fig. 3.3)          
    
    The Class requires
        Pandas
        Numpy
        KAGC_MarkerArts moduel
        KAGC_FUN moduel 
        KAGC_DUS moduel
        KAGC_KAGC_Marker_Artifacts moduel


    E.G.,  b503 = co.Context(KAGC_FUN.DU_Select(df, KAGC_DUS.B503, 'B503'), -24) 
    """
## Main Methods
    import pandas as pd

    def __init__(self, cdu, res):
        self.cdu = cdu
        self.res = res


    def MCLS_Grps(self):
        """
        e.g., B503.MCLS_Grps().get_groups("amp")
        """
        x = self.cdu
        x['idn'] = x.mcls +'-'+ x.diag.fillna('UnID') +'-'+ x.date3.astype(str) + '-' + x.date4.astype(str)
        x = self.cdu.groupby(['mcls'])
        return x


    def MCLS_TPQS(self):
        """
        e.g., B503.MCLS_TPQS()
        """
        import numpy as np
        x = self.cdu[['DU','name','cxn', 'mcls', 'Cat','diag','type1', 'type2', 
                      'date1','date3', 'date4']].dropna(subset=['date3'])
        x1 = x.loc[x.groupby(['mcls'])['date3'].idxmax()].sort_values(by=['date3'])
        x1['Dspan'] = x1.date4 - x1.date3
        #x1['TPQ_25%'] = x1.Dspan*.25 + x1.date3
        x1['MPDate'] = x1.loc[:, 'date3':'date4'].apply(np.median, axis = 1)
        #x1['TPQ_75%'] = x1.Dspan*.75 + x1.date3
        x1['EAAD'] = x1.date3.max() - x1.date3
        x1['EAAD-M'] = x1.MPDate.max() - x1.MPDate
        return x1

    def CC_TPQS(self):
        """
        e.g., B503.CC_TPQS()
        """
        import numpy as np

        x = self.cdu[['DU','name','cxn', 'mcls', 'Cat','number', 
                      'diag', 'type1', 'date3', 'date4']].dropna(subset=['date3'])
        x1 = x.loc[x.groupby(['cxn'])["date3"].idxmax()].sort_values(by=['date3'])
        x1['Dspan'] = x1.date4 - x1.date3
        #x1['TPQ_25%'] = x1.Dspan*.25 + x1.date3
        x1['MPDate'] = x1.loc[:, 'date3':'date4'].apply(np.median, axis = 1)
        #x1['TPQ_75%'] = x1.Dspan*.75 + x1.date3
        return x1

    def UniqueForms(self):
        """
        e.g., B503.UniqueForms()
        """
        x = self.cdu
        x['idn'] = x.mcls +'-'+ x.diag.fillna('UnID') +'-'+ x.date3.astype(str) + '-' + x.date4.astype(str)
        x1 = x.drop_duplicates('idn')
        x2 = x1.groupby(['mcls']).diag.unique()
        return x2

    def ResidualForms(self):
        """
        e.g., B503.ResidualForms()
        """
        x = self.cdu
        x.drop_duplicates('idn')
        x1 = x.sort_values(['mcls', 'date3'])
        x1 = x[x.date3 < self.res]
        return x1


    def FCounts(self):
        """
        e.g., B503.FCounts()
        """
        import numpy as np
        import pandas as pd

        x = self.cdu
        x['Dspan'] = x['date4'] - x['date3']
        x['MPDate'] = x.loc[:, 'date3':'date4'].apply(np.median, axis = 1)
        x['EAAD'] = x.date3.max() - x.date3
        x['idn'] = x.mcls +'-'+ x.diag.fillna('UnID') +'-'+ x.date3.astype(str) + '-' + x.date4.astype(str)
        x1 = pd.crosstab([x.DU, x.mcls, x.diag, x.date3, x.date4, 
                          x.Dspan, x.MPDate, x.EAAD, x.idn], [0], 
                          margins= False).reset_index().rename(columns={0:'freq'})
        x1 = x1.sort_values(['mcls', 'date3']).reset_index()
        x1["Seq"] = x1.index +1
        return x1

    def DUCatNos(self):
        """
        e.g., B503.DUCatNos()
        """
        import pandas as pd
        import numpy as np

        x=self.cdu[['cxn', "mcls", 'diag', 'Cat', 'type1', 'date3', 'date4']]
        x = x.dropna(subset=['Cat']).sort_values(by=['mcls', 'Cat'], ascending = True )
        return x

    def DUSmry(self):
        """
        B503.DUSmry()
        """
        import pandas as pd
        dta = pd.DataFrame()

        dta['DU'] = self.cdu.DU.unique()
        dta['TPQ'] = [self.MCLS_TPQS().date3.max()]
        dta['MMDate'] = [round(self.cdu.MPDate.mean(),)]
        dta['Span'] = [self.cdu.date4.max() - self.cdu.date3.min()]
        dta['TForms'] = [self.FCounts().idn.count()]
        dta['RForms'] = [self.FCounts().loc[self.FCounts().date3 < self.res].idn.count()]
        dta['NRForms'] = [self.FCounts().loc[self.FCounts().date3 > self.res].idn.count()]
        dta['NRF:RF'] = round(dta.NRForms/dta.RForms,2)
        dta['Dspan > 100'] = [sum(self.FCounts().Dspan > 100)]
        #presence - absence
        dta['Arch'] = [(['architectural']) in self.cdu.type3.values]
        dta['Display'] = [(['display']) in self.cdu.type3.values]
        dta['P.items'] = [(['p.item']) in self.cdu.type3.values]
        dta['P.adorn'] = [(['p.adornment']) in self.cdu.type3.values]
        dta['Tool'] = [(['tool']) in self.cdu.type3.values]
        dta['Production'] = [(['production' or 'reduction']) in self.cdu.type3.values]

        return dta

## Secondary Methods
    def MKG1(self):
        """
        e.g., B503.MKG1()
        """
        import pandas as pd
        import KAGC_MarkerArts

        x= pd.crosstab([self.cdu[self.cdu.type3.isin(KAGC_MarkerArts.MG1)].cxn], 
                       [self.cdu[self.cdu.type3.isin(KAGC_MarkerArts.MG1)].type1], margins= True)

        return x

    def MKG2(self):
        """
        e.g., B503.MKG2()
        """
        import pandas as pd
        import KAGC_MarkerArts

        x= pd.crosstab([self.cdu[self.cdu.type3.isin(KAGC_MarkerArts.MG2)].cxn], 
                       [self.cdu[self.cdu.type3.isin(KAGC_MarkerArts.MG2)].type1], margins= True)

        return x

    def MKG3(self):
        """
        e.g., B503.MKG3()
        """
        import pandas as pd
        import KAGC_MarkerArts

        x= pd.crosstab([self.cdu[self.cdu.type3.isin(KAGC_MarkerArts.MG3)].cxn], 
                       [self.cdu[self.cdu.type3.isin(KAGC_MarkerArts.MG3)].type1], margins= True)

        return x