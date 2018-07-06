#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:37:51 2018

@author: biglin
"""

import SQLdriver


def getLastUserID():
    curser = openConnection()
    sqlQuery = 'SELECT MAX(userID) FROM projectBitcoin.User;'
    results = getFromDatabase( curser, sqlQuery )
    closeConnection(curser)
    return results

def writeNewUser( userID ):
    curser = openConnection()
    sqlQuery = 'INSERT INTO projectBitcoin.User (userID) VALUES (' + userID +');'
    results = writeToDatabase( curser, sqlQuery )
    closeConnection(curser)
    return results

    