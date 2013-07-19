#!/usr/bin/python
# -*- coding: utf-8 -*-

#

from gi.repository import Gtk

class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        self.grid = Gtk.Grid()
        self.add(self.grid)

        button1 = Gtk.Button(label = "Button 1")
        button2 = Gtk.Button(label = "Button 2")
        button3 = Gtk.Button(label = "Button 3")
        button4 = Gtk.Button(label = "Button 4")
        button5 = Gtk.Button(label = "Button 5")
        button6 = Gtk.Button(label = "Button 6")

        self.grid.add(button1)
        self.grid.attach(button2, 1,0, 2,1)
        self.grid.attach_next_to(button3, button1,Gtk.PositionType.BOTTOM, 1, 2)
        
        
win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
