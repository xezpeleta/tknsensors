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
	if temp > 30:
		print "CRITICAL - Temp: %.2f C" % temp
		sys.exit(2)
	elif temp > 27:
		print "WARNING - Temp: %.2f C" % temp
		sys.exit(1)
	else:
		print "OK - Temp: %.2f C" % temp
		sys.exit(0)

def getACPowerStatus():
	svalue = getSensorValue(SENSOR_ACPOWER)
	if svalue.isdigit():
		status = int(svalue)
		if status == 1:
			print "CRITICAL - ACPowerStatus: OFF"
			sys.exit(2)
		elif status == 0:
			print "OK - ACPowerStatus: ON"
			sys.exit(0)
		else:
			print "WARNING - ACPowerStatus: UNKNOWN"
			sys.exit(1)
	else:
		print "WARNING - ACPowerStatus: UNKNOWN"
		sys.exit(1)

def getACFilterStatus():
	svalue = getSensorValue(SENSOR_ACFILTER)
	if svalue.isdigit():
		status = int(svalue)
		if status == 1:
			print "CRITICAL - ACFilterStatus: OFF"
			sys.exit(2)
		elif status == 0:
			print "OK - ACFilterStatus: ON"
			sys.exit(0)
		else:
			print "WARNING - ACFilterStatus: UNKNOWN"
			sys.exit(1)
	else:
		print "WARNING - ACFilterStatus: UNKNOWN"
		sys.exit(1)


if __name__ == '__main__':
	sensor = sys.argv[1]
	if sensor == "temp":
		getTemperature()
	elif sensor == "acpower":
		getACPowerStatus()
	elif sensor == "acfilter":
		getACFilterStatus()
	else:
		print "Erabilera modua: python tknSensors.py [temp|acpower|acfilter]"

