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
fromWallet = []
toWallet = []
edgeAttr = []

"""resultsWallets = getAllWallets()

for i in resultsWallets:
    notes.append(i[0])
    print('Add: ' + i[0])"""
 
resultsTransactions = getAllTransactions()

for i in resultsTransactions:
    fromWallet.append(i[0])
    toWallet.append(i[1])
    
    if i[2] == 0:
        satosis = 0
    else:
        satosis = i[2]
        
    
    edgeAttr.append(satosis)
    
    '''G.add_edge(i[0], i[1], weight=(i[2] / 10000000))'''
    print('Add: ' + i[0] + "," + i[1] + "," + str(i[2]))


df = pd.DataFrame({'from': fromWallet, 'to': toWallet, 'weight':edgeAttr})

G=nx.from_pandas_edgelist(df, 'from', 'to','weight')


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
