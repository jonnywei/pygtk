#!/usr/bin/python
# -*- coding: utf-8 -*-

#

from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.Box(spacing = 6)
        self.add(self.box)
        
        self.label = Gtk.Label(label="label", angle= 25)
        #self.add(self.label)
        self.box.pack_start(self.label, True, False, 0)
        
        self.button = Gtk.Button(label="Click Me")
        self.button.connect("clicked", self.on_button_clicked)

        self.box.pack_start(self.button, True, False, 0)

        #self.add(self.button)

        

    def on_button_clicked(self, widget):
        print "Hello World"

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
