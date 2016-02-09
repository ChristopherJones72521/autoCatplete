#!/usr/bin/python
import os
import random
import requests
import functions
import json
from urllib2 import Request, urlopen, URLError

functions.generateName()

#############################################################
# This file will generate 3-million records for Elasticsearch
# Using bulk indexing API
#############################################################

# Use The Cat API to retrieve cat images
catPic = ('http://thecatapi.com/api/images/get?format=src&type=jpg,gif&size=full')

# Begin entering records # run the record entry query 3,000,000 times. 
i = 0
for each in range(10):
	description = functions.catIpsum()
	catName = functions.generateName()
	payload = json.dumps({'name':catName,'description':description,'image':catPic})
	#payload = json.dumps({'name':'%s','description':'%s','image':'%s'}) % (catName, description, catPic)
	url = "http://localhost:9200/shelter/cats/"+str(i)
	var = requests.put(url, data = payload)
	i += 1
	
# Process complete message
request = Request('http://placekitten.com/')

try:
	print "Process complete"
	response = urlopen(request)
	kittens = response.read()
	print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e