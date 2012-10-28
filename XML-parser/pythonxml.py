##########################################
# Author: Sajin George
# email:sajin.geo@gmail.com
# open source, thanks to adafruit you can also use smbus :-)
# thanks to my friend Aniket Mathare for the web code and Adafruit for a nice tutorial on EEML
# this is a cpu usage loger using Jquery
# this updates an XML files that is used in the html file.
##########################################
import xml.etree.ElementTree as ET
import os
import time
import psutil
import eeml 

while (True):
	cpuper=psutil.cpu_percent()
	memVir=psutil.virtmem_usage()
	memPhy=psutil.phymem_usage()
	diskUsageRoot=psutil.disk_usage('/')


	root = ET.Element("sys_info")

	cpu = ET.SubElement(root,"cpu")
	value1 = ET.SubElement(cpu,"value")
	value1.text=str(cpuper)

	memory = ET.SubElement(root,"memory")
	value2 = ET.SubElement(memory,"value")
	value2.text=str(memPhy.percent)

	network = ET.SubElement(root,"network")
	value3 = ET.SubElement(network,"value")
	value3.text=str(diskUsageRoot.percent)

	tree = ET.ElementTree(root)
	tree.write("sys_stats.xml")
	time.sleep(20)

