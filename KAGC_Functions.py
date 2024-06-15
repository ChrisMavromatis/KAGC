# KAGC Stratiraphic Functions v2
# Chris Mavromatis 2023

"""
This moduel contains a range of helper function for the analysis of the cemetery's stratigraphy.
The functions are divisible into several groups that deal 
with conection and selecttion, calculation, and plotting. 

# File Metadata
* Associated Publication: Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volumes 76 & 77, ASOR).

    * Main Publication Chapter(s) that use or mention these functions: 
    
    Mavromatis, Christopher. Michae Given (2024) Chapter 3 Methodology. Pp: 21-34. In Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volume 76 ASOR)

    Mavromatis, Christopher _et al_ (2024). Chapter 7 Deposition and Dumping in Area A. Pp: 97-126. In  Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. (2024) City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volume 76 ASOR).

    Mavromatis, Christopher _et al_. (2024) Chapter 9 The cist Tombs. Pp: 147-200. In  Given, Michael, Chris Mavromatis, and R. Smadar Gabrieli, ed. City and Cemetery: Excavations at Kourion’s Amathous Gate Cemetery, Cyprus. The Excavations of Danielle A. Parks (Annual of the American Society of Overseas Research, Volumes 76 ASOR).
    
* File Name: KAGC_Functions.py

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


# Connection and Selection Functions
## Connect to Sqlite DB
def DB_Con(DB_path:str):
    """
    Generates an connection to the project SQlite database and returns all rows as an object called df.

    Arguments:
        * A string or object containing the path to the database

    Requires:
        * sqlite3
        * pandas
   
     """
    # Connect to project databse and retuns a dataframe
    import sqlite3 as sql3
    import pandas as pd

    conn = sql3.connect(DB_path)
    cur = conn.cursor()
    df = pd.read_sql_query("select * from art", conn)
    conn.close()
    return df


def data(db, DU, du):
    # Connect to project database and return a filtered dataframe
        import sqlite3 as sql3
        import pandas as pd
        import numpy as np

        conn = sql3.connect(db)
        cur = conn.cursor()
        df = pd.read_sql_query('Select * From art', conn)
        conn.close()
        
        df = df[df.cxn.isin(DU)]
        df['DU'] = du
        df["MPDate"] = df.loc[:, 'date3':'date4'].apply(np.median, axis =1)
        return df


## DU selection for context object
def DU_Select(DF, DU, du):
    """
    Selects a specific DU from the project database and append the DU name to the new dataframe. 
    Also serves as main input for the ContextObject.

    Arguments:
        * DF = dataframe you are working with (usually a dataframe for the  entire the project)
        * DU = the DU value from the KAGC_DUS module - eg KAGC_DUS.A015
        * du = a string value which servers as the value for the new variable 'DU'
    
    Returns: 
    a data frame if it is not used as input for ContextObject

    """

    import numpy as np
    x = DF.loc[DF['cxn'].isin(DU)]
    x['DU'] = du
    x["MPDate"] = x.loc[:, 'date3':'date4'].apply(np.median, axis =1)
    return x

# Calculation Functions
## CC material class ubiquity
def UBQ_MCLS(DU, CC):
    """
    Calculates ubiquity of material classes for DUs' with contributing contexts.

    Parameters:
        * DU: ContextObject cdu, eg  b503.cdu
        * CC: contributing contexts from the KAGC_DUS module. eg KAGC_DUS.B503

    Requires:
        * numpy
        * pandas

    returns:
        a dictionary

    """

    import numpy as np
    import pandas as pd

    x = pd.crosstab([DU.cxn], [DU.mcls]).reset_index()

    avgs = round(x.mean(), 2)
    ConCx = len(CC)

    ArtU = []

    for i,j in x.iteritems():
        z = (np.count_nonzero(j)) / len(CC)
        ArtU.append((i, round(z, 2)))
    return {'DU CC': ConCx,
        'Artifact Ubiquity':ArtU}


def Jaccard_Similarity(L1, L2):
    """
    Generates the Jaccard similarity for two lists of artifacts from two contexts or DUs.

    Parameters:
        * L1 = a list of artifacts form a context or DU
        * L2 = a list of artifacts form a context or DU

    """
    intersection_cardinality = len(set.intersection(*[set(L1), set(L2)]))
    union_cardinality = len(set.union(*[set(L1), set(L2)]))
    return intersection_cardinality/float(union_cardinality)


def CommonSubtypes(L1, L2):
    """
    Returns the common artifact and the number of common sub-types between two lists of artifacts.

    Parameters:
        * L1 = a list of artifacts for a context or DU
        * L2 = a list of artifacts for a context or DU

    """

    x = set(L1) & set(L2)
    x1 = len(x)
    return{'Common subtypes:': x,
           'Number of common subtypes:': x1}

def MMDate(x):
   """
   Returns the unweighted median date from a context class.
   
   """

   import pandas as pd
   import numpy as np
    
   z=  x.MCLS_Grps().MPDate.mean().reset_index().sort_values(by= 'mcls')
   return z

# Conversion functions
## convert counts to present absence for wide data
def to_binary():
    """
    Converts count data in tabular form to presence - absence (0,1) via .applymap().

    eg: x1.iloc[:, 3:7].applymap(to_binary)

    """

    return lambda x: 0 if x<1 else 1 

# Plot Functions

## Date Span Plots
## Single context, DU CC TPQ, DU FCount, DU MCLS TPQ, Generic

# Single context
def SC_DSpanPlt(df, save_plot, out_ti, fext, start, stop):
    """
    Plots the date spans of unique items from a single context or material class;
    also context or DU TPQs items. 
    Dates must be numbers and B.C. dates must be expressed as a negative number e.g.  100 B.C. -> -100 

    Parameters:
        * df = dataframe of DU material class
        * TITLE = text plot title
        * out_ti = figure title
        * save _plot = save the plot 'Y' or 'N'
        * fext = output file extension (eg '.png')
        * start = earliest opening date depicted on  x axis
        * stop = latest closing date  on x axis

    Requires:
        seaborn, matplotlib.pyplot and numpy

    """

    import  matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    df['idn'] = df.mcls +'-'+ df.diag +'-'+ df.date3.astype(str) + '-' + df.date4.astype(str)

    df['lbl'] = df.mcls + '-' + df.Cat.fillna(df.mcls)

    x1 = df.dropna(subset = ['diag', 'date3', 'date4'])

    x1 = x1.drop_duplicates(['idn'])

    x1['PDMedian'] = x1.loc[:, 'date3':'date4'].apply(np.median, axis =1)

    x2 = x1.sort_values(by=['date3', 'date4'])

    my_range = range(1, len(x1.index)+1)

    x_ticks = []
    for i in range(start, stop, 100):
        x_ticks.append(i)

    # Plot variables
    sns.set_style("white", rc= {"xtick.bottom": True, "ytick.left": True,})
    sns.set_context("paper", font_scale = 0.9)
    plt.hlines(y=my_range, xmin=x2['date3'], xmax=x2['date4'], color='black', alpha= 1)
    plt.scatter(x2['date3'], my_range, color='black', alpha= 1, label='date3', s = 10)

    # PLot lables
    plt.yticks(my_range, x2.lbl, fontname = "Sans Serif", fontsize=10)
    plt.xticks(x_ticks, fontname = "Sans Serif", fontsize=10)
    plt.tick_params(axis = 'x', rotation = 0)    
    plt.tick_params(axis = 'y', rotation = 0, labelsize = 10)

    if len(str(stop)) > 4 or len(str(start)) >4:
        plt.xticks(rotation=45)
    else: pass 

    #plt.title("Times New Roman 18", fontname = "Times New Roman", fontsize=18)
    plt.xlabel('Production Spans', fontname = "Sans Serif", fontsize=12)
    plt.ylabel('Type-Form', fontname = "Carlito", fontsize=12)
    plt.tight_layout()



    # save options
    if save_plot == 'Y':
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass


# Contributing Context 
def CC_DSpanPlt(df, save_plot, out_ti,  fext, start, stop):

    """
    Plots the date spans of unique material class or Contributing Context. 
    Dates must be numbers and B.C. dates must be expressed as a negative number e.g.  100 B.C. -> -100. 

    Parameters:
        * df = DU class object
        * TITLE = text plot title
        * out_ti = figure title
        * save _plot = save the plot 'Y' or 'N'
        * fext = output file extension (eg '.png')
        * start = earliest opening date depicted on  x axis
        * stop = latest closing date  on x axis

    Requires: seaborn, matplotlib.pyplot and numpy

    """

    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np


    x1 = df.CC_TPQS()
    x2 = x1.sort_values(by=['date3', 'date4'])

    x1['lbl'] = x1.name +'-'+ x1.Cat.fillna(x1.mcls)

    x1['lbl'] = x1.lbl.replace('(TR)','Tr', regex=True, inplace=False)

    my_range = range(1, len(x1.index)+1)

    x_ticks = []
    for i in range(start, stop, 100):
        x_ticks.append(i)


    # Plot style
    sns.set_style("white", rc= {"xtick.bottom": True, "ytick.left": True,})
    sns.set_context("paper", font_scale = 0.9)
    plt.hlines(y=my_range, xmin=x2['date3'], xmax=x2['date4'], color='black', alpha= 1)
    plt.scatter(x2['date3'], my_range, color='black', alpha= 1, label='date3', s = 10)


    # PLot lables
    plt.yticks(my_range, x1.lbl, fontname = "Sans Serif", fontsize=10)
    plt.xticks(x_ticks, fontname = "Sans Serif", fontsize=10)
    plt.tick_params(axis = 'x', rotation = 0)
    plt.tick_params(axis = 'y', rotation = 0, labelsize = 10)

    if len(str(stop)) > 4 or len(str(start)) >4:
        plt.xticks(rotation=45)
    else: pass 

    #plt.title("Times New Roman 18", fontname = "Times New Roman", fontsize=18)
    plt.xlabel('Production Spans', fontname = "Sans Serif", fontsize=12)
    plt.ylabel('Type-Form', fontname = "Sans Serif", fontsize=12)
    plt.tight_layout()



    #save options
    if save_plot == 'Y':
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass


# FCounts Filtered
def FC_DatePlt_Filtered(df, save_plot, out_ti,  fext, start, stop):

    """
    Plots the date spans of the FCounts method from the DU class.
    Dates must be numbers and B.C. dates must be expressed as a negative number e.g.  100 B.C. -> -100. 

    Parameters:
        * df =  DU class object
        * Vlines = add mean and TPQ lines 'Y' or 'N'
        * out_ti = figure title
        * save _plot = save the plot 'Y' or 'N'
        * fext = output file extension (eg '.png')
        * start = earliest opening date depicted on  x axis
        * stop = latest closing date  on x axis

    Requires: seaborn, matplotlib.pyplot and numpy

    """

    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np


    x = df.sort_values(by=['date3', 'date4'])

    my_range = range(1, len(x.index)+1)

    x_ticks = []
    for i in range(start, stop, 100):
        x_ticks.append(i)

    # Plot style
    sns.set_style("white", rc= {"xtick.bottom": True, "ytick.left": True,})
    sns.set_context("paper", font_scale = 0.9)

    if len(x) > 20:
        plt.figure(figsize=(10,6))
    else:
        pass


    plt.hlines(y=my_range, xmin=x['date3'], xmax=x['date4'], color='black', alpha= 1)
    plt.scatter(x['date3'], my_range, color='black', alpha= 1, label='date3', s = 11)

    # Plot lables
    if len(x) > 20:
        plt.yticks(my_range, x.Seq, fontname = "Sans Serif", fontsize=12)
    else:
        plt.yticks(my_range, x.mcls +"-"+ x.Seq.astype(str), fontname = "Sans Serif", fontsize=12)
        plt.tick_params(axis = 'y', rotation = 0, labelsize = 11)
        

    plt.xticks(x_ticks, fontname = "Sans Serif", fontsize=10)
    plt.tick_params(axis = 'x', rotation = 0)
    plt.tick_params(axis = 'y', rotation = 0, labelsize = 8)

    if len(str(stop)) > 4 or len(str(start)) >4:
        plt.xticks(rotation=45)
    else: pass 
   
    #plt.title("Times New Roman 18", fontname = "Times New Roman", fontsize=18)
    plt.xlabel('Production Spans', fontname = "Sans Serif", fontsize=12)
    plt.ylabel('Type-Form', fontname = "Sans Serif", fontsize=12)
    plt.tight_layout()

    # Additinal 

    #if Vlines == 'Y':
        # Mean Median
        #plt.vlines(x = df.cdu.MPDate.mean(), ymin= 0, ymax = len(x.diag), color='blue', alpha= 1, linestyles=['--'])
        #plt.text(df.cdu.MPDate.mean() + 1, len(x.diag)+1, "MD", rotation= 0, color = 'blue')

        # TPQ
        #plt.vlines(x = x.date3.max(), ymin= 0, ymax = len(x.diag), color='red', alpha= 1, linestyles=['--'])
        #plt.text(x.date3.max() + 1, len(x.diag)+1, "TPQ", rotation= 0, color ='red')
    #else:
        #pass

    if len(str(stop)) > 4 or len(str(start)) >4:
        plt.xticks(rotation=45)
    else: pass 
    
    # Save
    if save_plot == 'Y':
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass



# FCounts 
def FC_DatePlt(df, Vlines, save_plot, out_ti,  fext, start, stop):
    """
    Plots the date spans of the FCounts method from the DU class.
    Dates must be numbers and B.C. dates must be expressed as a negative number e.g.  100 B.C. -> -100. 
    
    Parameters:
        * df = = DU class object
        * Vlines = add mean and TPQ lines 'Y' or 'N'
        * out_ti = figure title
        * save _plot = save the plot 'Y' or 'N'
        * fext = output file extension (eg '.png')
        * start = earliest opening date depicted on  x axis
        * stop = latest closing date  on x axis

    Requires: seaborn, matplotlib.pyplot and numpy

    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np


    x = df.FCounts().sort_values(by=['date3', 'date4'])

    my_range = range(1, len(x.index)+1)

    x_ticks = []
    for i in range(start, stop, 100):
        x_ticks.append(i)

    # Plot style
    sns.set_style("white", rc= {"xtick.bottom": True, "ytick.left": True,})
    sns.set_context("paper", font_scale = 0.9)

    if len(x) > 20:
        plt.figure(figsize=(10,6))
    else:
        pass
    
    #if Vlines == "Y":
        #plt.figure(figsize=(10,6))

    plt.hlines(y=my_range, xmin=x['date3'], xmax=x['date4'], color='black', alpha= 1)
    plt.scatter(x['date3'], my_range, color='black', alpha= 1, label='date3', s = 11)

    # Plot lables
    if len(x) > 20:
        plt.yticks(my_range, x.Seq, fontname = "Sans Serif", fontsize=12)
    else:
        plt.yticks(my_range, x.mcls +"-"+ x.Seq.astype(str), fontname = "Sans Serif", fontsize=12)
        plt.tick_params(axis = 'y', rotation = 0, labelsize = 11)
        



    plt.xticks(x_ticks, fontname = "Sans Serif", fontsize=10)
    plt.tick_params(axis = 'x', rotation = 0)
    plt.tick_params(axis = 'y', rotation = 0, labelsize = 8)

    if len(str(stop)) > 4 or len(str(start)) >4:
        plt.xticks(rotation=45)
    else: pass 


    #plt.title("Times New Roman 18", fontname = "Times New Roman", fontsize=18)
    plt.xlabel('Production Spans', fontname = "Sans Serif", fontsize=12)
    plt.ylabel('Type-Form', fontname = "Sans Serif", fontsize=12)
    

    # Additinal 

    if Vlines == 'Y':
        # Mean Median
        MMD = plt.vlines(x = df.cdu.MPDate.mean(), ymin= 0, ymax = len(x.diag), color='blue', alpha= 1, linestyles=['--'], label="Mean Median Date")
        #plt.text(df.cdu.MPDate.mean() + 1, len(x.diag)+1, "MD", rotation= 0, color = 'blue')

        # TPQ
        TPQ = plt.vlines(x = x.date3.max(), ymin= 0, ymax = len(x.diag), color='red', alpha= 1, linestyles=['--'], label="Terminus Post Quem")
        #plt.text(x.date3.max() + 1, len(x.diag)+1, "TPQ", rotation= 0, color ='red')

        plt.legend(loc ="lower center", bbox_to_anchor= (0.5, -0.3), ncol = 2, handles = [MMD, TPQ], fontsize = 10)

        
    else:
        pass

    
    # Save
    if save_plot == 'Y':
         plt.tight_layout()
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass


# DU Material Class TPQ
def DU_MCLS_TPQ_Plt(df, save_plot, out_ti,  fext, start, stop):
    """
    Plots the date spans of unique material class or Contributing Context using the DU class's .MCS_TPQS method.
    Dates must be numbers and B.C. dates must be expressed as a negative number e.g.  100 B.C. -> -100. 

    Parameters:
        * df = DU class object
        * TITLE = text plot title
        * out_ti = figure title
        * save_plot = save the plot 'Y' or 'N'
        * fext = output file extension (eg '.png')
        * start = earliest opening date depicted on  x axis
        * stop = latest closing date  on x axis

    Requires: seaborn, matplotlib.pyplot and numpy
    
    """

    import  matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np


    x1 = df.MCLS_TPQS()
    x2 = x1.sort_values(by=['date3', 'date4'])

    x2['lbl'] = x2.name +'-'+ x2.Cat.fillna(x2.mcls)
    x2['lbl'] = x2.lbl.replace('(TR)','Tr', regex=True, inplace=False)

    my_range = range(1, len(x1.index)+1)

    x_ticks = []
    for i in range(start, stop, 100):
        x_ticks.append(i)

    # Plot style
    sns.set_style("white", rc= {"xtick.bottom": True, "ytick.left": True,})
    sns.set_context("paper", font_scale = 0.9)
    plt.hlines(y=my_range, xmin=x2['date3'], xmax=x2['date4'], color='black', alpha= 1)
    plt.scatter(x2['date3'], my_range, color='black', alpha= 1, label='date3', s = 10)

    if len(str(stop)) > 3 or len(str(start)) >3:
        plt.xticks(rotation=45)
    else: pass 

    # PLot lables
    plt.yticks(my_range, x2.lbl, fontname = "Sans Serif", fontsize=10)
    plt.xticks(x_ticks, fontname = "Sans Serif", fontsize=10)
    plt.tick_params(axis = 'x', rotation = 0)
    plt.tick_params(axis = 'y', rotation = 0, labelsize = 10)

    if len(str(stop)) > 3 or len(str(start)) >3:
        plt.xticks(rotation=45)
    else: pass

    #plt.title("Times New Roman 18", fontname = "Times New Roman", fontsize=18)
    plt.xlabel('Production Spans', fontname = "Sans Serif", fontsize=12)
    plt.ylabel('Type-Form', fontname = "Sans Serif", fontsize=12)
    plt.tight_layout()


    #save options
    if save_plot == 'Y':
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass


# Generic 
def dateplot(df, save_plot, out_ti,  fext, start, stop):
    """
    Generic base for KAGC plots.
    Dates must be numbers and B.C. dates must be expressed as a negative number e.g.  100 B.C. -> -100. 


    Parameters:
        * df = dataframe of DU material class
        * TITLE = text plot title
        * out_ti = figure title
        * save_plot = save the plot 'Y' or 'N'
        * fext = output file extension (eg '.png')
        * start = earliest opening date depicted on  x axis
        * stop = latest closing date  on x axis

    Requires: seaborn, matplotlib.pyplot and numpy

    """

    import  matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    df['idn'] = df.name +'-'+df.mcls +'-'+ df.diag +'-'+ df.date3.astype(str) + '-' + df.date4.astype(str)

    df['lbl'] = df.name +'-'+ df.Cat.fillna(df.mcls)

    
    x1 = df.dropna(subset = ['diag', 'date3', 'date4'])

    x1 = x1.drop_duplicates(['idn'])

    x1['PDMedian'] = x1.loc[:, 'date3':'date4'].apply(np.median, axis =1)

    x2 = x1.sort_values(by=['date3', 'date4'])

    my_range = range(1, len(x1.index)+1)

    x_ticks = []
    for i in range(start, stop, 100):
        x_ticks.append(i)
    # Plot style
    sns.set_style("white", rc= {"xtick.bottom": True, "ytick.left": True,})
    sns.set_context("paper", font_scale = 0.9)
    plt.hlines(y=my_range, xmin=x2['date3'], xmax=x2['date4'], color='black', alpha= 1)
    plt.scatter(x2['date3'], my_range, color='black', alpha= 1, label='date3', s = 11)


    # PLot lables
    plt.yticks(my_range, x2.lbl, fontname = "Sans Serif", fontsize=10)
    plt.xticks(x_ticks, fontname = "Sans Serif", fontsize=10)
    plt.tick_params(axis = 'x', rotation = 0)
    plt.tick_params(axis = 'y', rotation = 0, labelsize = 10)

    if len(str(stop)) > 4 or len(str(start)) >4:
        plt.xticks(rotation=45)
    else: pass 

    #plt.title("Times New Roman 18", fontname = "Times New Roman", fontsize=18)
    plt.xlabel('Production Spans', fontname = "Sans Serif", fontsize=12)
    plt.ylabel('Type-Form', fontname = "Sans Serif", fontsize=12)
    plt.tight_layout()

    #save options
    if save_plot == 'Y':
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass

## Heat Maps
def HeatMapUF(df, save_plot, out_ti, fext):
    """
    Plots a heatmap of the number of unique forms by mcls. Designed to work with a Context object's .ResidualForms and Fcounts methods.
    and assumes "idn" variable is present in the data frame.

    Parameters:
        * df: DU class .ResidualForms method
        * TITLE: DU's name eg "B503" (string)
        * out_ti: figure title (string)
        * save_plot: "Y" or "N"  (string)
        *fext: file extension, eg ".pdf" (string)

    Requires:
        * pandas
        * seaborn
        * numpy

    """

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    x = df.groupby(['mcls', 'date3'])['idn'].nunique().reset_index()
    x1 = pd.pivot_table(x, values = 'idn', index=['mcls'], columns='date3',  aggfunc = np.sum)

    #bw = sns.palplot(sns.cubehelix_palette(50, hue=0.05, rot=0, light=0.9, dark=0))

    sns.heatmap(x1, annot= True, linewidth = 0.5)

    #plot lables and style
    sns.set_style("white", rc= {"xtick.bottom": True, "ytick.left": True,})
    sns.set_context("paper", font_scale = 0.9)
    plt.xticks(rotation=45, fontname = "Sans Serif", fontsize=10)
    plt.yticks(rotation=0, fontname = "Sans Serif", fontsize=10)
    plt.xlabel("Opening Production Dates", fontname = "Sans Serif", fontsize=12)
    plt.ylabel('Material Class', fontname = "Sans Serif", fontsize=12)
    plt.tight_layout()

    #save options
    if save_plot == 'Y':
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass


def DU_UniqueItemPlot(cdu, save_plot, out_ti, fext):
    """
    Returns a custom barplot depicting the number of unique items from the CCs for a given DU. Also includes a mean value
    line. Also returns a PNG of the graph.

    Arguments:
        * cdu = DU context class .cdu method
        * save_plot = "Y" or "N" (string)
        * out_ti = output file name; eg "du503_unique_items" (string)
        * fext = file extention; eg ".png" (string)

    Requires:
        * seaborn
        * matplotlib.pyplot
        * pandas

    """

    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    x = cdu.groupby('name').diag.nunique().reset_index()
    z = sum(x.diag)/len(x)
    z1 = x.diag.mean()

    # Plot variables and custom seaborn stype
    sns.set_style("white", rc= {"xtick.bottom": True})
    sns.set_context("paper", font_scale = 0.9)

    x1 = sns_plot = sns.barplot(x = "name", data= x, y = x.diag, color = "gray")
    x1.axhline(x.diag.mean(), ls='--', color = 'black')
    #x1.text(0.5, x.diag.mean(), round(x.diag.mean(),1))
    x1.set_ylabel("Number of Unique Items")
    x1.set_xlabel("")
    #x1.set_title(du)
    x1.set_xticklabels(x1.get_xticklabels(),rotation=90)

    # Save
    if save_plot == 'Y':
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass

    return x, z1
    



def HeatMapFC(df, save_plot, out_ti, fext):
    """
    Plots a heatmap of the number fragments-items by mcls. Designed to work with a Context object's FCounts method.
    It assumes "freq" variable is present in the data frame.

    Parameters:
        * df: DU context class .ResidualForms dataframe
        * TITLE: DU's name eg "B503" (string)
        * out_ti: figure title (string)
        * save_plot: "Y" or "N"  (string)
        *fext: file extension, eg ".pdf" (string)

    Requires:
        * pandas
        * seaborn
        * numpy
    """

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    x1 = pd.pivot_table(df, values = 'freq', index=['mcls'], columns='date3',  aggfunc = np.sum)

    #bw = sns.palplot(sns.cubehelix_palette(50, hue=0.05, rot=0, light=0.9, dark=0))

    sns.heatmap(x1, annot= True, linewidth = 0.5)

    #plot lables and style
    sns.set_style("white", rc= {"xtick.bottom": True, "ytick.left": True,})
    sns.set_context("paper", font_scale = 0.9)
    plt.xticks(rotation=45, fontname = "Sans Serif", fontsize=10)
    plt.yticks(rotation=0, fontname = "Carlito", fontsize=10)
    plt.xlabel("Opening Production Dates", fontname = "Sans Serif", fontsize=12)
    plt.ylabel('Material Class', fontname = "Sans Serif", fontsize=12)
    plt.tight_layout()

    #save options
    if save_plot == 'Y':
         plt.savefig(out_ti + fext, dpi = 1200)
    else:
        pass
