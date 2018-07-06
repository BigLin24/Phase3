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

from graph_tool.all import *

import driverWallet
import driverTransactions

def testing():
    g = Graph()
    v1 = g.add_vertex()
    v2 = g.add_vertex()
    e = g.add_edge(v1, v2)
    graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")


def getDataframe2():
    resultsTransactions = getAllTransactions()
    for i in resultsTransactions:
        G.add_node(i[0])
        G.add_node(i[1])
        
        G.add_edge(i[0], i[1])
        
        print('Add: ' + i[0] + "," + i[1] + "," + str(i[2]))
    

# Plot it
def plotIt2():
    nx.draw(G,node_size=2,font_size=8, with_labels=False)
    plt.show()
    plt.savefig("path1.png")


"""uild a dataframe with 4 connections
df = pd.DataFrame({ 'from':['A', 'B', 'C','A'], 'to':['D', 'A', 'E','C']})
df
 
# Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to')


"""
