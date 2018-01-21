#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scan.py
#  
#  Copyright 2017  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time
from beacontools import BeaconScanner, IBeaconFilter
import schedule
from threading import Lock
from time import gmtime,strftime

uuid="b9407f30-f5f8-466e-aff9-25556b57fe6d"
def get_response(uuid):
	def callback(bt_addr, rssi, packet, additional_info):
		lock.acquire()
		major.add(packet.major)
		addr.add(bt_addr)
		#rss.add(str(rssi))
		#mionr.add(packet.minor)
		#addinfo.add(addtional_info)
		
		lock.release()
	
	lock = Lock()
	major = set()
	addr = set()
	#rss = set()
	#minor = set()	
	#addinfo = set()
	
	status = ('tag',addr,'major',major)
			
	scanner = BeaconScanner(callback,
		device_filter=IBeaconFilter(uuid=uuid)
	)
		
	scanner.start()
	time.sleep(0.5)
	
	#numebr of ibeacons under uuid
	ibno = 3
	majors = ([21248,805,4863])
	if (len(major) <= ibno):
		print((ibno - len(major)), 'ibeacons not found')
		for i in range(ibno):
			if not majors[i] in major:
				print(majors[i],'is out')
				
                	#tracking algorithm
			

	
				
		
	scanner.stop()
	return status
	
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial 

while True:
	
	time.sleep(0.5)
	
	print('scanning time')
	print(strftime('%Y-%m-%d %H:%M:%S', gmtime()))
	print(get_response(uuid))
	raspi1 = getserial()
        print(raspi1)
	#print('the', uuid, 'has pass the', raspi1)
	
	
