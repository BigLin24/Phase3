#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fuert die Abfragen auf SQL aus
Bearbeiter: Daniel
"""
import pymysql as mc

"""import sqlite3
conn = sqlite3.connect('database.db')"""



connection = mc.connect (host = "localhost",
                         user = "DBphase3",
                         passwd = "phase3DB",
                         db = "projectBitcoin")

"""cursor.execute ("SELECT VERSION()")
row = cursor.fetchone()
print("server version:", row[0])
cursor.close()
connection.close()"""

def openConnection():
	curser = connection.cursor()
	return curser

def closeConnection( curser ):
	curser.close()

def writeToDatabase( curser, insertString ):
    curser.execute( insertString )
    connection.commit()
    

def getFromDatabase( curser, selectString ):
    curser.execute( selectString )
    results = curser.fetchall()
    for i in results:
    	print(i)
    return results
    
    
def getObjectByID( curser, table, idField, idTable ):
    curser.execute( 'SELECT * FROM ' + table + ' WHERE ' + idField + ' = "' + idTable +'"')
    results = curser.fetchall()    
    return results

