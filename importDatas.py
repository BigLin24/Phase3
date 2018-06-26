#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:12:27 2018

@author: Kmiotek
"""

import SQLdriver
import time



def writeInput():
    fp = open("transactions_input.csv")
    for i, line in enumerate(fp):
       
        if i is not 0:
            
            s = ',,'
            
            if s not in line:
                a,b,c,d,e = line.split(',')
                
                e1 = int(e) / 1000
                eNew = int(round(e1))
                print(a + "," + b + "," + c + "," + d + "," + str(eNew)) 
                
            
    fp.close()



def writeBlocks():
    fp = open("transactions_blocks.csv")
    for i, line in enumerate(fp):        
        s = ',,'
        
        if s not in line:
            print (line)
            
    fp.close()