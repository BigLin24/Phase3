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
    sqlQuery = 'SELECT transactionID FROM projectBitcoin.Transaction;'
    
    results = getFromDatabase( curser, sqlQuery )
    
    closeConnection(curser)
    
    return results

def getTransactionByUserID( userID ):
    curser = openConnection()
    sqlQuery = 'SELECT Wallet.FKuserID, Output.FKpublicKey, Input.FKpublicKey, Output.FKtransactionID, Wallet.FKuserID \
        FROM projectBitcoin.Output, projectBitcoin.Input, projectBitcoin.Wallet \
        WHERE Output.FKpublicKey = Wallet.PublicKey \
        AND Input.FKtransactionID = Output.FKtransactionID \
        AND Wallet.FKuserID = ' + userID + ';'
    results = getFromDatabase( curser, sqlQuery )
    
    closeConnection(curser)
    
    return results



