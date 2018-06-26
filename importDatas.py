#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:12:27 2018

@author: Kmiotek
"""

import SQLdriver
import re
import time



def writeInput():
    fp = open("transactions_input.csv")
    for i, line in enumerate(fp):
        #print(line)
        
        s = ',,'
        
        if s not in line:
            a,b,c,d,e = line.split(',')
            
            print(e)

           
            
            #print (str(e), str(eNew))

            
    fp.close()



def writeBlocks():
    fp = open("transactions_blocks.csv")
    for i, line in enumerate(fp):        
        s = ',,'
        
        if s not in line:
            print (line)
            
    fp.close()