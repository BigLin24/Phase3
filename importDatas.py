#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:12:27 2018

@author: Kmiotek
"""

import SQLdriver
import time

def writeWallet():
	curser = openConnection()
	fp = open("transactions_output.csv")
	for i, line in enumerate(fp):

		if i is not 0:

			s = ',,'
			r = '""'

			if s not in line and r not in line:
				a,b,c,publicKey,e = line.split(',')

				results = getObjectByID( curser, 'Wallet', 'PublicKey', publicKey)

				if not results:
					writeToDatabase( curser, 'INSERT INTO Wallet (PublicKey, FKuserID) \
					 values ("' + publicKey + '", (select userID FROM User WHERE userID = 1) );' )
					print("Written: " + publicKey)
				else:
					print("Not written: " + publicKey)

	closeConnection(curser)
	fp.close()



def writeInput():
	curser = openConnection()
	fp = open("transactions_input.csv")

	for i, line in enumerate(fp):
		if i is not 0:
			s = ',,'
			r = '""'

			if s not in line and r not in line:
				transID,inputScript,seqNumber,PublicKey,timestamp = line.split(',')

				timestamp1 = int(timestamp) / 1000
				timestampNew = int(round(timestamp1))

				selectString = 'SELECT FKpublicKey, FKtransactionID FROM Input \
				WHERE FKpublicKey = "' + PublicKey + '" \
				AND FKtransactionID = "' + transID + '";'

				results = getFromDatabase( curser, selectString )

				if not results:
					insertString = 'INSERT INTO Input ( scriptString, sequenceNumber, FKpublicKey, timestamp, FKtransactionID)\
					VALUES ("' + inputScript +'", ' + seqNumber +', \
					(SELECT PublicKey FROM Wallet WHERE PublicKey = "' + PublicKey +'"),\
					from_unixtime('+ str(timestampNew) + '), \
					(SELECT transactionID FROM Transaction WHERE transactionID = "' + transID +'"));'

					writeToDatabase( curser, insertString )
					print('Written: ' + PublicKey + ' & ' +  transID)
				else:
					print('Not Written: ' + PublicKey + ' & ' +  transID)

	closeConnection(curser)
	fp.close()


def writeOutput():
	curser = openConnection()
	fp = open("transactions_output.csv")

	for i, line in enumerate(fp):
		if i is not 0:
			s = ',,'
			r = '""'

			if s not in line and r not in line:
				transID,satoshis,inputScript,PublicKey,timestamp = line.split(',')

				timestamp1 = int(timestamp) / 1000
				timestampNew = int(round(timestamp1))

				selectString = 'SELECT FKtransactionID, FKpublicKey FROM Output \
				WHERE FKpublicKey = "' + PublicKey + '" \
				AND FKtransactionID = "' + transID + '";'

				results = getFromDatabase( curser, selectString )

				if not results:
					insertString = 'INSERT INTO Output ( FKtransactionID, satoshis, scriptString, FKpublicKey, timestamp)\
					VALUES ((SELECT transactionID FROM projectBitcoin.Transaction WHERE transactionID = "' + transID +'"),\
					' + satoshis + ', "' + inputScript + '",\
					(SELECT PublicKey FROM Wallet WHERE PublicKey = "' + PublicKey +'"),\
					from_unixtime('+ str(timestampNew) + '));'
					print(PublicKey)
					writeToDatabase( curser, insertString )
					print('Written: ' + PublicKey + ' & ' +  transID)
				else:
					print('Not Written: ' + PublicKey + ' & ' +  transID)

	closeConnection(curser)
	fp.close()



def writeBlocks():
	curser = openConnection()

	fp = open("transactions_blocks.csv")

	for i, line in enumerate(fp):

		if i is not 0:

			s = ',,'

			if s not in line:
				transID,BlockID,preBlock,merkleRoot,nonce,versionBC, timestamp = line.split(',')
				timestame1 = int(timestamp) / 1000
				timestampNew = int(round(timestame1))

				results = getObjectByID( curser, 'blocks', 'blockID', BlockID)

				if not results:
					sqlInsert = 'INSERT INTO blocks (blockID, previousBlock, merkleRoot, nonce, versionBC, timestamp) \
					VALUES ("'+ BlockID + '", "'+ preBlock + '", "'+ merkleRoot + '", '+ nonce + ', '+ versionBC + ', from_unixtime('+ str(timestampNew) + '));'

					writeToDatabase( curser, sqlInsert )
					print("Written: " + BlockID)
				else:
					print("Not written: " + BlockID)
	closeConnection(curser)
	fp.close()


def writeTransaction():
	curser = openConnection()

	fp = open("transactions_blocks.csv")

	for i, line in enumerate(fp):

		if i is not 0:

			s = ',,'

			if s not in line:
				transID,BlockID,preBlock,merkleRoot,nonce,versionBC, timestamp = line.split(',')

				results = getObjectByID( curser, 'Transaction', 'transactionID', transID)

				if not results:
					sqlInsert = 'INSERT INTO projectBitcoin.Transaction (transactionID, FKblockID) \
					VALUES ("'+ transID + '", (SELECT blockID FROM blocks WHERE blockID = "' + BlockID +'"));'

					writeToDatabase( curser, sqlInsert )
					print("Written: " + transID)
				else:
					print("Not written: " + transID)
	closeConnection(curser)
	fp.close()

