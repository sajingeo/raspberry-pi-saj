##########################################
# Author: Sajin George
# email:sajin.geo@gmail.com
# open source, thanks to adafruit you can also use smbus :-)
# using RGB led from MBLINK
# thanks to adafruit
##########################################
#
# refer instructable for required libs.
#
#########################################
import feedparser,time
from smbus import SMBus
from Adafruit_I2C import Adafruit_I2C
import os

## username and password
USERNAME="tom.tom"
PASSWORD="password"

## email now in inbox
MAILSNOW=6579

# frequency of checking
MAILCHECK=60

## codes for blink M
RED=[0x63,0xff,0x00,0x00]
GREEN=[0x63,0x00,0xff,0x00]

## address of blinkM
data=Adafruit_I2C(0x09)

while(True):
	data.write8(0x00,0x6f)
	newmails=int(feedparser.parse("http://"+USERNAME+":"+PASSWORD+"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
	print newmails
	
	if(newmails>MAILSNOW):
		data.writeList(0x00,RED)
	else:
		data.writeList(0x00,GREEN)
	time.sleep(MAILCHECK)
