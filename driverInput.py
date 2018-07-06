#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fraegt ueber SQldriver die DB ab und "verwandelt die Daten in ein Array
Bearbeiter: Nikola
"""
import SQLdriver

def getInputByTransID( transID ):
    curser = openConnection()
    sqlQuery = 'SELECT FKpublicKey FROM projectBitcoin.Input \
    WHERE FKtransactionID = "' + transID + '";'
    
    results = getFromDatabase( curser, sqlQuery )
    closeConnection(curser)
    return results

def getTransactionWithInput():
    curser = openConnection()
    sqlQuery = 'SELECT FKpublicKey, transactionID \
    FROM projectBitcoin.Transaction, projectBitcoin.Input \
    WHERE Transaction.transactionID= Input.FKtransactionID;'
    
    results = getFromDatabase( curser, sqlQuery )
    closeConnection(curser)
    return results



