#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:12:27 2018

@author: Kmiotek
"""

from SQLdriver import getObjectByID, writeToDatabase
import time

def writeWallet():
    fp = open("transactions_input.csv")
    for i, line in enumerate(fp):
       
        if i is not 0:
            
            s = ',,'
            r = '""'
            
            if s not in line and r not in line:
                a,b,c,publicKey,e = line.split(',')

                results = getObjectByID( 'Wallet', 'PublicKey', publicKey)
                
                if not results:
                	writeToDatabase('INSERT INTO Wallet (PublicKey, FKuserID) \
                	 values ("' + publicKey + '", (select userID FROM User WHERE userID = 1) );' )
                	print("Written: " + publicKey)
          		else:
            		print("Not written: " + publicKey)

    fp.close()



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

                results = getObjectByID( 'Wallet', 'PublicKey', d)
                
                if not results:
                	writeToDatabase('INSERT INTO Wallet (PublicKey) values ("' + d + '");' )
                	print("Written: " + d)
            	else:
            		print("Not written: " + d)


    fp.close()



def writeBlocks():
    fp = open("transactions_blocks.csv")
    for i, line in enumerate(fp):        
        s = ',,'
        
        if s not in line:
            transID,BlockID,preBlock,merkleRoot,nomce,versionBC, timestamp = line.split(',')

            timestamp = int(e) / 1000
            timestampNew = int(round(e1))

            results = getObjectByID( 'blocks', 'blockID', BlockID)

            if not results:
            	writeToDatabase('INSERT INTO blocks (blockID, previousBlock, merkleRoot, nonce, timestamp) \
            		values ("' + blockID + '","' + previousBlock + '","' + merkleRoot + '","' + nonce + '", FROM_UNIXTIME(' + timestampNew + ');' )
            	print("Written: " + d)
            else:
            	print("Not written: " + d)
            
    fp.close()