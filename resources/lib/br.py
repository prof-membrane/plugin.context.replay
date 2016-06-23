# -*- coding: utf-8 -*-
import libBr
import resources.lib.helper as helper

name = 'BR Mediathek'
addonName = 'ARD Mediathek'
supportsPlay = True
supportsMore = False
supportsShow = False
supportsSearch = False
supportsAddon = False
channels = {"br":"br",
			   "brfernsehen":"br",
			   "brnord":"br",
			   "brfernsehennord":"br",
			   "ardalpha":"ardalpha",
			  }
			  
def fetchShows(dict):
	return libBr.getDate(dict['date'])
def play(dict):
	libBr.play(dict)