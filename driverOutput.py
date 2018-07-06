#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fraegt ueber SQldriver die DB ab und "verwandelt die Daten in ein Array
Bearbeiter: Adrian
"""
import SQLdriver


def getOutputByTransID( transID ):
    curser = openConnection()
    sqlQuery = 'SELECT FKpublicKey FROM projectBitcoin.Output \
    WHERE FKtransactionID = "' + transID + '";'
    
    results = getFromDatabase( curser, sqlQuery )
    
    closeConnection(curser)
    
    return results
    
    

def getOutputByInputAndTrans( publicKey, transID ):
    curser = openConnection()
    sqlQuery = 'SELECT Output.FKpublicKey, Input.FKpublicKey, Input.FKtransactionID \
        FROM projectBitcoin.Output, projectBitcoin.Input \
        WHERE Output.FKtransactionID = Input.FKtransactionID \
        AND Input.FKtransactionID = "' + transID + '"\
        AND Input.FKpublicKey = "' + publicKey + '";'
        
    results = getFromDatabase( curser, sqlQuery )
    
    closeConnection(curser)
    
    return results