#!/usr/bin/python
import os
import random
import json
import functions
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
	var = '''
		curl -XPOST "localhost:9200/shelter/cats/_bulk -d
		{'index':{'_id':'%d'}}
		{'name':'%s','description':'%s','image':'%s'}
		"''' % (i, catName, description, catPic)
	i += 1
	os.system(var)
	

# Process complete message
request = Request('http://placekitten.com/')

try:
	response = urlopen(request)
	kittens = response.read()
	print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e
