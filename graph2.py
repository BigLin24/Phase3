#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 19:32:26 2018

@author: biglin


vertex_text=g.vertex_properties['name'],
vertex_text_position=1,
vertex_font_size=2,
"""

# libraries
import pandas as pd
import numpy as np

from graph_tool.all import *

import driverWallet
import driverOutput
import driverInput
import driverTransactions
import matplotlib
import time

g = Graph()


def testing():
    g = Graph()
    v1 = g.add_vertex()
    v2 = g.add_vertex()
    e = g.add_edge(v1, v2)
    graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")


def getDataframe2():
    resultsTransactions = getAllTransactions()
    return resultsTransactions

def getDataTransaction():
    resultsTransactions = getTransactions()
    return resultsTransactions

def getAllUser():
    results = getAllUserIDs()
    return results


def getDataTransWithInput():
    results = getTransactionWithInput()
    return results

# Plot it
def plotIt( resultsTransactions ):
    red = (1,0,0,1)
    blue = (0,0,1,1)
    
    vprop = g.new_vertex_property("string")
    
    plot_color = g.new_vertex_property('vector<double>')
    g.vertex_properties['plot_color'] = plot_color
    
    
    for i in resultsTransactions:
        transactionsOutput = getOutputByTransID(i[0])
        transactionsInput = getInputByTransID(i[0])
        
        if len(transactionsOutput) + len(transactionsInput) > 10:
        
            v1 = g.add_vertex()
            vprop[v1] = i[0]
            plot_color[v1] = blue
            
            
            for n in transactionsOutput:
                v2 = g.add_vertex()
                
                vprop[v2] = n[0]
                plot_color[v2] = red
                
                g.add_edge(v2, v1)
                
                
            
            
            for n in transactionsInput:
                v2 = g.add_vertex()
                
                vprop[v2] = n[0]
                plot_color[v2] = red
                
                g.add_edge(v1, v2)
            
    
    g.vertex_properties["name"]=vprop

    graph_draw(g,
               graph_tool.draw.sfdp_layout(g),
               vertex_size=1, 
               vertex_color=g.vertex_properties['plot_color'],
               vertex_fill_color = g.vertex_properties['plot_color'],
               bg_color=[1,1,1,1],
               output_size=(1000, 1000),
               output="two-nodes.png")

def setNewSameUser( results ):
    maxUserIDtemp = getLastUserID()
    maxUserID = maxUserIDtemp[0][0]
    
    
    for i in results:
        inputPublicKey = i[0]        
        inputTransID = i[1]

        users = getOutputByInputAndTrans( inputPublicKey, inputTransID )
        
        maxUserID = maxUserID + 1
        writeNewUser(str(maxUserID))
        print (len(users))
        
        for n in users:
            print(n)
            writeNewUserWallet( n[0], str(maxUserID ))
        


def getDataTransWithInput():
    results = getTransactionWithInput()
    return results

# Plot it
def plotItAufgabe3( results ):
    red = (1,0,0,1)
    blue = (0,0,1,1)
    
    vprop = g.new_vertex_property("string")
    
    plot_color = g.new_vertex_property('vector<double>')
    g.vertex_properties['plot_color'] = plot_color
    
    
    for i in results:
        transOutput = getTransactionByUserID(str(i[0]))
        print(transOutput)
        
        if len(transOutput) > 0:
        
            v1 = g.add_vertex()
            vprop[v1] = transOutput[0][0]
            plot_color[v1] = red
            
            
            v2 = g.add_vertex()
            vprop[v2] = transOutput[0][3]
            plot_color[v2] = blue
                
            g.add_edge(v2, v1)

            v3 = g.add_vertex()
            vprop[v3] = getUserIDbyPublicKey(str(transOutput[0][2]))
            plot_color[v3] = red
            
            g.add_edge(v2, v3)
            
    
    g.vertex_properties["name"]=vprop

    graph_draw(g,
               graph_tool.draw.sfdp_layout(g),
               vertex_size=3, 
               vertex_color=g.vertex_properties['plot_color'],
               vertex_fill_color = g.vertex_properties['plot_color'],
               bg_color=[1,1,1,1],
               output_size=(1000, 1000),
               output="two-nodes.png")