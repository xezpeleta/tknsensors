#!/usr/bin/python

'''
+-------------------------------------------------------------------------+
| Copyright (C) 2009: TKNIKA - Xabi Ezpeleta <xezpeleta _at_ tknika.net>  |
|                                                                         |
| This program is free software; you can redistribute it and/or           |
| modify it under the terms of the GNU General Public License             |
| as published by the Free Software Foundation; either version 2          |
| of the License, or (at your option) any later version.                  |
|                                                                         |
| This program is distributed in the hope that it will be useful,         |
| but WITHOUT ANY WARRANTY; without even the implied warranty of          |
| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           |
| GNU General Public License for more details.                            |
+-------------------------------------------------------------------------+
'''



import sys
import serial

USB_PORT='/dev/ttyUSB0'
BAUD = 9600

SENSOR_TEMP = 1
SENSOR_ACPOWER = 2
SENSOR_ACFILTER = 3
# Sensore berria?
#SENSOR_EXAMPLE = 4

def getSensorValue(sensor):
	ser = serial.Serial(USB_PORT,BAUD, timeout=1)
	# Hasieratze bytea bidali
	ser.write (chr(255))
	# Burutu eskaera
	ser.write (chr(sensor))
	# Irakurri emaitza...	
	svalue = ser.readline()
	while svalue == "\n":
		# Balioa irakurri arte behin eta berriz saiatu
		svalue = ser.readLine()
	ser.close()
	# Badirudi zuriuneekin itzultzen duela, goazen garbitzera!
	svalue = svalue.rstrip()
	return svalue

def getTemperature():
	svalue = getSensorValue(SENSOR_TEMP)
	temp = float(svalue)-5.00 # Kalibrazioa, zuzenketa faktorea :P
	print "Zerbitzari gelako tenperatura: %.2f C" % temp

def getACPowerStatus():
	svalue = getSensorValue(SENSOR_ACPOWER)
	if svalue.isdigit():
		status = int(svalue)
		if status == 1:
			print "Aire Girotuaren egoera: OFF"
		elif status == 0:
			print "Aire Girotuaren egoera: ON"
		else:
			print "Aire Girotuaren egoera: ezezaguna"
	else:
		print "Aire Girotuaren egoera: ezezaguna"

def getACFilterStatus():
	svalue = getSensorValue(SENSOR_ACFILTER)
	if svalue.isdigit():
		status = int(svalue)
		if status == 1:
			print "Aire Girotuaren filtroen egoera: MATXURA"
		elif status == 0:
			print "Aire Girotuaren filtroen egoera: ONDO"
		else:
			print "Aire Girotuaren filtroen egoera: ezezaguna"
	else:
		print "Aire Girotuaren filtroen egoera: ezezaguna"


if __name__ == '__main__':
	getTemperature()
	getACPowerStatus()
	getACFilterStatus()


