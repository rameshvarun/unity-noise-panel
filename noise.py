#!/usr/bin/env python 

import gobject
import gtk
import appindicator
import pygame
import sys
import os

pygame.mixer.init()
pygame.mixer.music.load( os.path.join( os.path.dirname( os.path.realpath(__file__)) , "noise.mp3" ) )
pygame.mixer.music.play(-1)

playing = True
def toggle_play(widget):
	global playing
	playing = not playing

	if playing:
		pygame.mixer.music.unpause()
	else:
		pygame.mixer.music.pause()
	widget.set_label("Pause" if playing else "Play")

ICON_PATH = os.path.join( os.path.dirname( os.path.realpath(__file__)) , "icon.png" )
print ICON_PATH

if __name__ == "__main__":
	ind = appindicator.Indicator ("noise-client", ICON_PATH , appindicator.CATEGORY_APPLICATION_STATUS)
	ind.set_status (appindicator.STATUS_ACTIVE)

	# create a menu
	menu = gtk.Menu()

	# create some 
	toggle_item = gtk.MenuItem("Pause")



	toggle_item.connect("activate", toggle_play)
	menu.append(toggle_item)

	toggle_item.show()

	ind.set_menu(menu)

	gtk.main()
