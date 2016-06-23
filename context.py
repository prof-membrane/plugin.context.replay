# -*- coding: utf-8 -*-
import xbmc
import sys
import resources.lib.helper as helper
import resources.lib.ard as ard
import resources.lib.br as br
import resources.lib.zdf as zdf

channel = helper.getChannelName()

dict = helper.getInfos()

if channel in br.channels:
	channelModule = br
elif channel in ard.channels:
	channelModule = ard
elif channel in zdf.channels:
	channelModule = zdf
#elif channel in arte.channels:
#	arte.play()
#elif channel in servustv.channels:
#	servustv.play()
else:
	xbmc.log("channel not supported")
	xbmc.executebuiltin("Notification(Kein Video gefunden,Sender wird nicht unterstützt, 7000)")
	sys.exit()

import xbmcgui	
pDialog = xbmcgui.DialogProgressBG()
pDialog.create(channelModule.name, 'Suche Beitrag')
shows = channelModule.fetchShows(dict)
foundVideo = helper.findVideo(dict,shows)

pDialog.close()

menuList = []
actionList = []
if foundVideo:
	if channelModule.supportsPlay:
		menuList.append("Aus Mediathek abspielen")
		actionList.append('play')
	if channelModule.supportsMore:
		menuList.append("Sendungsseite")
		actionList.append('more')
else:
	if channelModule.supportsShow:
		foundShow = helper.findShow(dict,channelModule.getShows())
		if foundShow:
			menuList.append("Sendungsseite")
			actionList.append('show')
		
if channelModule.supportsSearch:
	menuList.append("In Mediathek suchen")
	actionList.append('search')
if channelModule.supportsAddon:
	menuList.append(channelModule.addonName + ' aufrufen')
	actionList.append('addon')
	
if len(menuList) == 0:
	sys.exit()

selected = xbmcgui.Dialog().contextmenu(list=menuList)
xbmc.log(str(selected))
if selected == -1:
	sys.exit()
action = actionList[selected]

if action == 'play':
	channelModule.play(foundVideo)
elif action == 'more':
	channelModule.more(foundVideo)
elif action == 'show':
	channelModule.show(foundShow)
elif action == 'search':
	channelModule.search(dict['name'])
elif action == 'addon':
	channelModule.addon()
	
"""
if foundShow:
	selected = xbmcgui.Dialog().contextmenu(list=["Aus Mediathek abspielen", "Weitere Beiträge zeigen", "In Mediathek suchen"])
	if selected == 0:
		channelModule.play(foundShow)
else:
	selected = xbmcgui.Dialog().contextmenu(list=["In Mediathek suchen"])"""