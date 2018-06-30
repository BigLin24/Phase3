#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:12:27 2018

@author: Kmiotek
"""

from SQLdriver import getObjectByID, writeToDatabase
import time



def writeInput():
    fp = open("transactions_input.csv")
    for i, line in enumerate(fp):
       
        if i is not 0:
            
            s = ',,'
            r = '""'
            
            if s not in line and r not in line:
                a,b,c,d,e = line.split(',')
                
                e1 = int(e) / 1000
                eNew = int(round(e1))
                
                
                results = getObjectByID( 'wallet', 'PublicKey', d)
                
                for row in results:
                    print('None')
                    PublicKey = row[0]
                    FKuserID = row[1]
                    
                    print (PublicKey, FKuserID )
                    

                
            
    fp.close()



def writeBlocks():
    fp = open("transactions_blocks.csv")
    for i, line in enumerate(fp):        
        s = ',,'
        
        if s not in line:
            print (line)
            
    fp.close()