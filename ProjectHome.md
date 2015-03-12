[Castellano](Castellano.md) | [English](English.md)

# 1 Arduino: Eskema elektrikoa #
Gure kasuan Arduinoa honetarako erabiliko dugu:
  * Tenperatura neurtu
  * Aire girotua piztua edo itzalia dagon aztertu
  * Aire girotuko filtroak ondo dauden ikusi

Hona hemen diagrama elektronikoaren irudia:

# 2 Arduino: Firmwarearen programazioa #
Arduinoren lengoaian programatu dugu zenbait liburutegi erabiliz:

# 3 PCtik datuak kontsultatzen #
Pythonen egindako script batzuen bidez egin dugu datuen jasotzea

Momentuz bi tresna ditugu garatuak datuak kontsultatzeko:

### tknSensors.py: kontsulta tresna ###

#python tknSensors.py

Itzulitako emaitza:

.f..fd.a.fa

### check\_tknSensors.py: Nagios-eko plugina ###

#python check\_tknSensors.py temp|acpower|acfilter

Itzulitako emaitza: