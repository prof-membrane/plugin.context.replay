# -*- coding: utf-8 -*-
import xbmc
import urllib
listArd = ["daserste",
		   "einsfestival",
		   "mdrsachsen",
		   "wdrköln",
		   "brfernsehennord",
		   "rbbbrandenburg"
		  ]

channel = xbmc.getInfoLabel("ListItem.ChannelName")
channel = channel.lower().replace(" ","").replace(".","").replace("-","").replace("/","")

name = xbmc.getInfoLabel("ListItem.Title")

if channel in listArd:
	#xbmc.executebuiltin("XBMC.Container.Update(plugin://script.module.libArd/?mode=libArdListSearch&searchString="+urllib.quote_plus(name)+")")
	#xbmc.executebuiltin("Container.Update(plugin://script.module.libArd/?mode=libArdListSearch&searchString="+urllib.quote_plus(name)+")")
	#xbmc.executebuiltin("RunPlugin(plugin://script.module.libArd/?mode=libArdListSearch&searchString="+urllib.quote_plus(name)+")")
	xbmc.executeJSONRPC('{"jsonrpc": "2.0","method": "Addons.ExecuteAddon","params": {"wait": false,"addonid": "script.module.libArd","params": ["?mode=libArdListSearch&searchString='+urllib.quote_plus(name)+'"]},"id": 2} }')
else:
	xbmc.executebuiltin("Notification(Kein Video gefunden,Sender wird nicht unterstützt, 7000)")