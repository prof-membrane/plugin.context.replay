# -*- coding: utf-8 -*-
import libArd
import resources.lib.helper as helper

name = 'ARD Mediathek'
addonName = 'ARD Mediathek'
supportsPlay = True
supportsMore = True
supportsShow = True
supportsSearch = True
supportsAddon = True
channels = {"daserste":"daserste",
			   "einsfestival":"einsfestival",
			   "wdr":"wdr",
			   "wdrköln":"wdr",
			   "br":"br",
			   "brfernsehen":"br",
			   "brnord":"br",
			   "brfernsehennord":"br",
			   "mdr":"mdr",
			   "mdrsachsen":"mdr",
			   "mdrthüringen":"mdr",
			   "mdrsachsenanhalt":"mdr",
			   "rbb":"rbb",
			   "rbbberlin":"rbb",
			   "rbbbrandenburg":"rbb",
			   "sr":"sr",#todo make more
			   "hr":"hr",#todo make more
			   "ndr":"ndr",
			   "tagesschau24":"tagesschau24",
			   "ardalpha":"ardalpha",
			   "einsplus":"einsplus",
			   "swr":"swr",
			   "swrrheinlandpfalz":"swr",
			   "swrbadenwürttemberg":"swr",
			  }

def fetchShows(dict):
	return libArd.libArdPvrDate(str(dict['day']),dict['channel'])
def more(dict):
	return False
def getShows():
	import ardShows
	return ardShows.shows
def show(url):
	import xbmc
	import urllib
	xbmc.executeJSONRPC('{"jsonrpc": "2.0","id": 2,"method": "GUI.ActivateWindow","params": {"window": "videos","parameters": ["plugin://plugin.video.ardmediathek_de?mode=libArdListVideos&url='+urllib.quote_plus(url)+'"]}}')
def play(dict):
	return libArd.libArdPvrPlay(dict)
def addon():
	import xbmc
	#xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"plugin.video.ardmediathek_de","wait":false},"id":4}')
	
	xbmc.executeJSONRPC('{"jsonrpc": "2.0","id": 2,"method": "GUI.ActivateWindow","params": {"window": "videos","parameters": ["plugin://plugin.video.ardmediathek_de"]}}')
def search(searchString):
	import xbmc
	import urllib
	xbmc.executeJSONRPC('{"jsonrpc": "2.0","id": 2,"method": "GUI.ActivateWindow","params": {"window": "videos","parameters": ["plugin://plugin.video.ardmediathek_de?mode=libArdListSearch&searchString='+urllib.quote_plus(searchString)+'"]}}')
"""
def play():
	dict = helper.getInfos()
	dict["channel"] = dict["channel"].replace(" HD","")
	if dict["channel"] == 'mdrsachsen' or dict["channel"] == 'mdrsachsenanhalt' or dict["channel"] == 'mdrthüringen':
		if dict["time"] == 1140:
			#libArd.libArdPvrPlay(dict["time"],dict["day"],dict["name"],dict["channel"])
			libArd.libArdPvrPlay(dict)
		else:
			#libArd.libArdPvrPlay(dict["time"],dict["day"],dict["name"],channels[dict["channel"]])
			dict["channel"] = channels[dict["channel"]]
			libArd.libArdPvrPlay(dict)
			
	else:
		#libArd.libArdPvrPlay(dict["time"],dict["day"],dict["name"],channels[dict["channel"]])
		dict["channel"] = channels[dict["channel"]]
		libArd.libArdPvrPlay(dict)
"""