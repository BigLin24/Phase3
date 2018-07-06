#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 19:32:26 2018

@author: biglin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:08:24 2018

@author: biglin
"""



# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import driverWallet
import driverTransactions

G = nx.Graph()

def getDataframe2():
    resultsTransactions = getAllTransactions()
    return resultsTransactions
    

    

# Plot it
def plotIt2( resultsTransactions ):
    n = 0
    
    for i in resultsTransactions:
        G.add_node(n)
        G.add_node(int(i[3], 16))
        G.add_edge(n, (i[3], 16))
        
        n = n +1
        
        G.add_node(n)
        G.add_node(int(i[3], 16))
        G.add_edge(n, (i[3], 16))
               
        print('Add: ' + i[0] + "," + i[1] + "," + str(i[2]))
        
        n = n +1
    
    nx.draw(G,node_size=2,font_size=8, with_labels=False)
    plt.show()
    plt.savefig("path1.png")


"""uild a dataframe with 4 connections
df = pd.DataFrame({ 'from':['A', 'B', 'C','A'], 'to':['D', 'A', 'E','C']})
df
 
# Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to')


"""
