#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
import json
import requests
reload(sys)
sys.setdefaultencoding("utf-8")
from BeautifulSoup import BeautifulSoup
import urllib, urllib2

url = "http://websys.secr.ncku.edu.tw/act/index.php?c=auth"
data = urllib2.urlopen(url)
soup = BeautifulSoup(data)

activities = 0
info = 0
target = 0	#資訊教育
find = 0	#bool
result = []
event = {}
table = soup.find("table", {"class" : "grid_data"})
for row in table.findAll("tr"):
	cells = row.findAll("td")
	#print cells
	for elements in cells:
		#print cells[1]
		info += 1
		if info == 2:	#info 2 = catagory
			
			if "通識認證講座" in elements.contents[0]:
				target += 1
				#print elements.contents[0].strip()
				find =1
				
				event['catagory'] = elements.contents[0].strip()
		if info == 3 and find == 1:	#get the name of the activity

			#print elements.contents[0].strip()
			event['name'] = elements.contents[0].strip()
		if info == 4 and find == 1:	#get the time of activity
			#print elements.contents[0].strip()
			event['time'] = elements.contents[0].strip()
			print json.dumps(event, encoding='UTF-8', ensure_ascii=False)


			url = 'http://52.192.20.250/chat/create/robot/'
			payload = {'robot_id':108143422899450,'content':event['name'],'lng':0,'lat':0}
			#payload = json.dumps(event, encoding='UTF-8', ensure_ascii=False)
			r = requests.post(url, data=payload)
			print r.text
			print r.status_code
			#print event


	#print event

	info = 0
	activities += 1
	find = 0



#print "There are %d activities~~" %(activities-1)	#because the first row in just information

print "There are %d 通識認證講座" %target


