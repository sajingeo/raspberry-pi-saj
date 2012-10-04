##############################################################
#
#    CPU logger 1.0
#    Author:Sajin George
#    Website:www.mycrobonics.com
#    licence:GNU
###############################################################
import os
import time
import psutil
import eeml 

API_KEY = 'mKii5nsNrnsE9RshWqwCiPDT-1-SAKx1L3M5amlpNWt1UT0g'
FEED   = 70623
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum =FEED)
# you can put it in an loop and run it as sudo python cpuloger.py &
# while (True):
cpuper=psutil.cpu_percent()
memVir=psutil.virtmem_usage()
memPhy=psutil.phymem_usage()
diskUsageRoot=psutil.disk_usage('/')
#	for debug only
#	print ("CPU USAGE:%s" % cpuper)
#	print ("Virtual Mem:%s" % memVir.percent)
#	print ("Physical Mem:%s" % memPhy.percent)
#	print ("Disk Usage:%s" % diskUsageRoot.percent)
cosm=eeml.Pachube(API_URL,API_KEY)
cosm.update([eeml.Data(0,cpuper,unit=eeml.RH())])
cosm.update([eeml.Data(1,memVir.percent,unit=eeml.RH())])
cosm.update([eeml.Data(2,memPhy.percent,unit=eeml.RH())])
cosm.update([eeml.Data(3,diskUsageRoot.percent,unit=eeml.RH())])
cosm.put()

