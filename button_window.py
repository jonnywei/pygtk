#!/usr/bin/python
# -*- coding: utf-8 -*-

#

from gi.repository import Gtk,GObject

class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ButtonWindow Demo")

        #self.set_size_request(200, 100)
       
         
        hbox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing= 6)
        self.add(hbox)

        button = Gtk.Button("click me")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        
        
        self.pulse = Gtk.Button (stock = Gtk.STOCK_OPEN)
        self.pulse.connect("clicked", self.on_open_clicked)
       
        hbox.pack_start(self.pulse, True, True, 0)

        self.icon = Gtk.Button("Icon", use_underline = True)
        self.icon.connect("clicked", self.on_icon_clicked)
        hbox.pack_start(self.icon, True, True, 0)

        

    def on_click_me_clicked(self, button):
        pass

    def on_open_clicked(self, button):
        pass

    def on_icon_clicked(self, button):
        pass 
                
win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
