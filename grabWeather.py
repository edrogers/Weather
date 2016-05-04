#!/usr/bin/python

import os
import urllib2
import json
import time
import config


unixTime=int(time.time())
dirName=os.path.dirname(os.path.realpath(__file__))
dataSourceDir="{}/output".format(dirName)
conditionsFileName="{}/{}-conditions.json".format(dataSourceDir,unixTime)
forecastFileName="{}/{}-forecast.json".format(dataSourceDir,unixTime)

with open(conditionsFileName,'w') as outfile :
  f = urllib2.urlopen('http://api.wunderground.com/api/{}/geolookup/conditions/q/WI/Madison.json'.format(config.apikey))
  json_string = f.read()
  outfile.write(json_string)
  f.close()

with open(forecastFileName,'w') as outfile :
  f = urllib2.urlopen('http://api.wunderground.com/api/891a8289f71019c6/forecast/q/WI/Madison.json'.format(config.apikey))
  json_string = f.read()
  outfile.write(json_string)
  f.close()
  
# parsed_json = json.loads(json_string)
# location = parsed_json['location']['city']
# temp_f = parsed_json['current_observation']['temp_f']
# print "Current temperature in %s is: %s" % (location, temp_f)
