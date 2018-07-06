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

def getUserIDbyPublicKey( PublicKey ):
    curser = openConnection()
    sqlQuery ='SELECT Wallet.FKuserID, Input.FKpublicKey \
        FROM projectBitcoin.Input, projectBitcoin.Wallet \
        WHERE Input.FKpublicKey = Wallet.PublicKey \
        AND Input.FKpublicKey = "' + PublicKey + '";'
    
    results = getFromDatabase( curser, sqlQuery )
    closeConnection(curser)
    
    if not results:
        return 1
    else:
        return results[0][0]
    