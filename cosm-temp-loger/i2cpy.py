##########################################
# Author: Sajin George
# email:sajin.geo@gmail.com
# open source, thanks to adafruit you can also use smbus :-)
# using PMOD TEMP from digilent
##########################################
#
#  refer instrucatables
#
###########################################
from smbus import SMBus
from Adafruit_I2C import Adafruit_I2C
import os
import time
import psutil
import eeml
## your key
API_KEY = '**********************************'
## ur feed ID
FEED   = 74897
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum =FEED)


#set the device addresss
data=Adafruit_I2C(0x4b)

while(True):
	#set the address
	datalist=data.readList(0x00,2)

	# get the MSB and LSB and calculate the temp 
	temp = (datalist[0]<<8)|datalist[1]
	tempraw =(temp>>3)*0.0625
	#print "the temperature at lab:"
	#print tempraw
	cosm=eeml.Pachube(API_URL,API_KEY)
	cosm.update([eeml.Data(1,tempraw,unit=eeml.Celsius())])
	cosm.put()
	time.sleep(60)