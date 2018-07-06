#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:48:46 2018

@author: biglin
"""
import SQLdriver

def getAllTransactions():
    curser = openConnection()
    sqlQuery = 'SELECT Output.FKpublicKey as Output, Input.FKpublicKey as Input, Output.satoshis, Output.FKtransactionID \
    FROM projectBitcoin.Output, projectBitcoin.Input \
    WHERE Output.FKtransactionID = Input.FKtransactionID;'
    
    results = getFromDatabase( curser, sqlQuery )
    
    closeConnection(curser)
    
    return results


def getTransactions():
    curser = openConnection()
    sqlQuery = 'SELECT transactionID FROM projectBitcoin.Transaction LIMIT 100000;'
    
    results = getFromDatabase( curser, sqlQuery )
    
    closeConnection(curser)
    
    return results

