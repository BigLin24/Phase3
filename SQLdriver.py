#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fuert die Abfragen auf SQL aus
Bearbeiter: Daniel
"""


import sqlite3
conn = conn = sqlite3.connect('database.db')
c = conn.cursor()

def writeToDatabase( insertString ):
    c.execute( insertString )
    conn.commit()
    conn.close()

def getFromDatabase( selectString ):
    c.execute( selectString )
    conn.close()