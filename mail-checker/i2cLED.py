##########################################
# Author: Sajin George
# email:sajin.geo@gmail.com
# open source, thanks to adafruit you can also use smbus :-)
# using RGB led from MBLINK
# thanks to adafruit
##########################################
import feedparser,time
from smbus import SMBus
from Adafruit_I2C import Adafruit_I2C
import os

USERNAME="tom.tom"
PASSWORD="password"

MAILSNOW=6579
MAILCHECK=60
RED=[0x63,0xff,0x00,0x00]
GREEN=[0x63,0x00,0xff,0x00]
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
