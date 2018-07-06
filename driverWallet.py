#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:31:59 2018

@author: biglin
"""
import SQLdriver

def writeNewUserWallet( publicKey, userID ):
    curser = openConnection()
    sqlQuery ='UPDATE projectBitcoin.Wallet \
    SET FKuserID = (SELECT userID FROM projectBitcoin.User WHERE userID = ' + userID +' ) \
    WHERE PublicKey = "' + publicKey + '";'
    
    results = writeToDatabase( curser, sqlQuery )
    closeConnection(curser)
    return results