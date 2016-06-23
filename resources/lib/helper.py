# -*- coding: utf-8 -*-
from datetime import date
import xbmc,sys
import time

dateformat = 'weekday, DD. Month YYYY'  

months = {
			"Januar":1,
			"Februar":2,
			"März":3,
			"April":4,
			"Mai":5
		}#todo

def log(m):
	xbmc.log(m)
def getMinutes():
	videodate = xbmc.getInfoLabel("ListItem.FileName").replace('.epg','')
	t = videodate.split(" ")[-1]
	HH,MM,SS = t.split(":")
	return int(HH) * 60 + int(MM) + 120
	
def timeToMM(t):
	HH,MM = t.split(":")
	return int(HH) * 60 + int(MM)
	
def getDuration():
	d = xbmc.getInfoLabel("ListItem.Duration").split(":")
	for i, val in enumerate(d[::-1]):
		if i == 0:
			duration = int(val)
		elif i == 1:
			duration += int(val) * 60
		elif i == 2:
			duration += int(val) * 3600
	return duration
def getChannelName():
	channel = xbmc.getInfoLabel("ListItem.ChannelName")
	channel = channel.replace("HD","").replace(" ","").replace(".","").replace("-","").replace("/","").lower()
	return channel
	
def getDate():
	videodate = xbmc.getInfoLabel("ListItem.FileName")
	d = videodate.split(" ")[0]
	YYYY,MM,DD = d.split("-")
	delta = date.today() - date(int(YYYY), int(MM), int(DD))
	return delta.days
	
def getInfos():
	
	xbmc.log(xbmc.getInfoLabel("ListItem.Label"))
	xbmc.log(xbmc.getInfoLabel("ListItem.Label2"))
	xbmc.log(xbmc.getInfoLabel("ListItem.OriginalTitle"))
	xbmc.log(xbmc.getInfoLabel("ListItem.Episode"))
	xbmc.log(xbmc.getInfoLabel("ListItem.Season"))
	xbmc.log(xbmc.getInfoLabel("ListItem.FileName"))
	xbmc.log(xbmc.getInfoLabel("ListItem.Date"))
	xbmc.log(xbmc.getInfoLabel("ListItem.Tagline"))
	xbmc.log('episode')
	xbmc.log(xbmc.getInfoLabel("ListItem.EpisodeName"))
	xbmc.log(xbmc.getInfoLabel("ListItem.Duration"))
	xbmc.log("#############")
	xbmc.log(xbmc.getInfoLabel("ListItem.Path"))
	xbmc.log("#############")
	xbmc.log(xbmc.getInfoLabel("ListItem.FileNameAndPath"))
	xbmc.log("#############")
	xbmc.log(sys.listitem.getLabel("Path"))
	dict = {}
	#videodate = xbmc.getInfoLabel("ListItem.Date")
	#xbmc.log(videodate)#25.04.2016 19:50
	dict["epoch"] = int(time.mktime(time.strptime(xbmc.getInfoLabel("ListItem.FileName").replace('.epg',''), '%Y-%m-%d %H:%M:%S')))
	dict["date"] = xbmc.getInfoLabel("ListItem.FileName").split(" ")[0]
	dict["time"] = getMinutes()
	dict["day"] = getDate()
	if dict["time"] == 1440:
		dict["time"] = 0
		dict["day"] = dict["day"] - 1
	dict["duration"] = getDuration()
	dict["name"] = xbmc.getInfoLabel("ListItem.Title")
	if dict["name"].endswith(')'):
		dict["episode"] = dict["name"].split('(')[-1].replace(')','')#extracts episode number: "someseries (5)" -> 5
		l = len(dict["episode"]) + 3
		dict["name"] = dict["name"][:-l]#removes " (5)"
	dict["subtitle"] = xbmc.getInfoLabel("ListItem.EpisodeName")

	
	dict["channel"] = getChannelName()
	return dict
	
def findVideo(dict,list):
	log(str(dict['time']))
	for d in list:
		if d['time'] == dict['time']:
			return d
	#log(str(dict))
	#log(str(list))
	return False
	
def findShow(dict,list):
	for entry in list:
		if entry['name'] == dict['name']:
			return entry['url']
	return False
	