#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fraegt ueber SQldriver die DB ab und "verwandelt die Daten in ein Array
Bearbeiter: Daniel
"""
import SQLdriver

def getAllWallets():
    curser = openConnection()
    sqlQuery = 'SELECT PublicKey FROM Wallet'
    
    results = getFromDatabase( curser, sqlQuery )
    
    closeConnection(curser)
    
    return results
