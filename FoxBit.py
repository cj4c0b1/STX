# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| FoxBit Robot                  |#'
print '| ------------                  |#'
print '|                               |#'
print '| By.: Prof. Carlo R. da Cunha  |#'
print '|                               |#'
print '|                     Set/2018  |#'
print '\'-------------------------------\'#'
print '  ################################'
print ''
print 'Importing Libraries:'

from websocket import create_connection
import json

print 'Simulating...'
print ''

wsAddress = "wss://apifoxbitprodlb.alphapoint.com/WSGateway/"

messageFrame = {
	"m":0,	#0:Request, 1:Reply, 2:Subscribe, 3:Event, 4:Unsubscribe, Error
	"i":0,	#Sequence number (long integer)
	"n":"",	#Endpoint -> function name (integer)
	"o":""	#Payload (string)
}

def PayLoad():
	requestPayLoad = {
		"OMSId": 1,
		"InstrumentId": 1
	}
	payLoadString = json.dumps(requestPayLoad, separators=(',',':'))
	messageFrame["o"] = payLoadString
	messageFrame["n"] = "GetInstrument"
	msgFrame = json.dumps(messageFrame)
	ws.send(msgFrame)
	
def Ticker():
	requestPayLoad = {
		"OMSId": 1,
		"InstrumentId": 1
	}
	payLoadString = json.dumps(requestPayLoad, separators=(',',':'))
	messageFrame["o"] = payLoadString
	messageFrame["n"] = "SubscribeLevel1"
	msgFrame = json.dumps(messageFrame)
	ws.send(msgFrame)
	result = ws.recv()
	tk = json.loads(Tresult)
	tx = json.loads(tk["o"])
	return tx

#############################################
##                 MAIN                    ##
#############################################
print "Creating connection..."
ws = create_connection(wsAddress)

tk = json.loads(Ticker())
tx = json.loads(tk["o"])
print tx["LastTradedPx"]
