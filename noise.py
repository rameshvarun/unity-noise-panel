#!/usr/bin/env python 

import gobject
import gtk
import appindicator
import pygame
import sys
import os

pygame.mixer.init()


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

SOUNDS = {
	"Morning Murmur" : "morningMurmur_mp3.mp3",
	"Lunchtime Lounge" : "lunchtimeLounge_mp3.mp3",
	"University Undertones" : "universityUndertones_mp3.mp3"
}

def startSound(widget, sound):
	pygame.mixer.music.load( os.path.join( os.path.dirname( os.path.realpath(__file__)) , SOUNDS[sound] ) )
	pygame.mixer.music.play(-1)
startSound(None, SOUNDS.keys()[0])

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

	quit_item = gtk.MenuItem("Quit")
	quit_item.connect("activate", lambda x: gtk.main_quit())
	menu.append(quit_item)
	quit_item.show()

	sep = gtk.SeparatorMenuItem()
	menu.append(sep)
	sep.show()

	for sound in SOUNDS:
		sound_item = gtk.MenuItem(sound)
		sound_item.connect("activate", startSound, sound)
		menu.append(sound_item)
		sound_item.show()

	sep = gtk.SeparatorMenuItem()
	menu.append(sep)
	sep.show()

	volumem = gtk.MenuItem("Volume")
	volumemenu = gtk.Menu()
	volumem.set_submenu(volumemenu)

	menu.append(volumem)
	volumem.show()

	VOLUMES = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	for volume in VOLUMES:
		item = gtk.MenuItem(str(volume * 100) + "%")
		volumemenu.append(item)
		item.connect("activate", lambda x, v: pygame.mixer.music.set_volume(v), volume )
		item.show()

	ind.set_menu(menu)

	gtk.main()
