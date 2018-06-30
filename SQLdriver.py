#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fuert die Abfragen auf SQL aus
Bearbeiter: Daniel
"""
import pymysql as mc

"""import sqlite3
conn = sqlite3.connect('database.db')"""



connection = mc.connect (host = "87.106.6.161",
                         user = "DBphase3",
                         passwd = "phase3DB",
                         db = "projectBitcoin")

"""cursor.execute ("SELECT VERSION()")
row = cursor.fetchone()
print("server version:", row[0])
cursor.close()
connection.close()"""




def writeToDatabase( insertString ):
    curser = connection.cursor() 
    curser.execute( insertString )
    connection.commit()
    curser.close()

def getFromDatabase( selectString ):
    curser = connection.cursor() 
    curser.execute( selectString )
    results = curser.fetchall()
    for i in results:
    	print(i)
    curser.close()
    return results
    
    
def getObjectByID( table, idField, idTable ):
    curser = connection.cursor() 
    curser.execute( 'SELECT * FROM ' + table + ' WHERE ' + idField + ' = "' + idTable +'"')
    results = curser.fetchall()    
    curser.close()
    return results

