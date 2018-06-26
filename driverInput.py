#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fraegt ueber SQldriver die DB ab und "verwandelt die Daten in ein Array
Bearbeiter: Nikola
"""
import SQLdriver

def getAllInputTransactions():
    
    selectString = 'SELECT * FROM transactionsInput, wallet, transaction WHERE ftransactionID.FKtransactionID = ftransactionID.transactionID AND transactionsInput.FKpublicKey = wallet.publicKey;'
    
    getFromDatabase( selectString )
    