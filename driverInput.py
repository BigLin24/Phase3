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

def getSameUser( inputPublicKey, transID ):
    curser = openConnection()
    sqlQuery = 'SELECT Output.FKpublicKey as Output, Input.FKpublicKey as Input, Output.FKtransactionID \
    FROM projectBitcoin.Output, projectBitcoin.Input \
    WHERE Output.FKtransactionID = Input.FKtransactionID \
    AND Input.FKtransactionID = "'+ transID + '" \
    AND Input.FKpublicKey = "'+ inputPublicKey + '";'
    
    results = getFromDatabase( curser, sqlQuery )
    closeConnection(curser)
    return results



