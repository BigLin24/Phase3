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

 
resultsTransactions = getAllTransactions()

for i in resultsTransactions:
    G.add_node(i[0])
    G.add_node(i[1])
     
    sotasis = i[2] / 10000000

    G.add_edge(i[0], i[1], {'weight': sotasis})
    
    print('Add: ' + i[0] + "," + i[1] + "," + str(i[2]))



# Plot it
plt.savefig("path.png")
nx.draw(G, with_labels=True)
plt.show()


"""uild a dataframe with 4 connections
df = pd.DataFrame({ 'from':['A', 'B', 'C','A'], 'to':['D', 'A', 'E','C']})
df
 
# Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to')


"""
