# -*- coding: utf-8 -*-
import xbmc
import libZdf
import resources.lib.helper as helper

name = 'ZDF Mediathek'
addonName = 'ZDF Mediathek'
supportsPlay = True
supportsMore = False
supportsShow = False
supportsSearch = False
supportsAddon = False

channels = {"zdf":"zdf",
			   "zdfinfo":"zdfinfo",
			   "3sat":"3sat",
			   "zdfkultur":"zdfkultur",
			   "zdfneo":"zdfneo",
			   "neo":"zdfneo",
			   "neokika":"zdfneo",
			   "phoenix":"phoenix"
			  }

def fetchShows(dict):
	if dict['time'] < 330:
		dict['day'] = dict['day'] + 1
	return libZdf.libZdfPvrDate(str(dict['day']),dict['channel'])
		
	#return libArd.libArdPvrDate(str(dict['day']),dict['channel'])
	
def play(dict):
	libZdf.libZdfPvrPlay(dict)
"""
	dict = helper.getInfos()
	if dict["channel"] != "neokika":
		libZdf.libZdfPvrPlay(dict["time"],dict["day"],dict["name"],channels[dict["channel"]])
	elif dict["time"] >= 1260 or dict["time"] < 360:# on dvb-t, neo and kika share a channel. neo broadcasts between 21:00 and 6:00
		libZdf.libZdfPvrPlay(dict["time"],dict["day"],dict["name"],channels[dict["channel"]])
	else:
		xbmc.executebuiltin("Notification(Kein Video gefunden,Sender wird nicht unterstützt, 7000)")
"""	
def listSimmilar():
	return
def listMore():
	return