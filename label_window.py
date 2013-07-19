#!/usr/bin/python
# -*- coding: utf-8 -*-

#

from gi.repository import Gtk

class LabelWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")

        hbox = Gtk.Box(spacing= 10)
        hbox.set_homogeneous(False)
        self.add(hbox)
        
        vbox_left = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing= 10)
        vbox_left.set_homogeneous(False)

        vbox_right = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing= 10)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        label = Gtk.Label()
        label.set_markup("Text can be <small>small</small>, <big>big</big>, "
                         "<b>bold</b>, <i>italic</i> and even point to "
                         "somewhere in the <a href=\"http://www.gtk.org\" "
                         "title=\"Click to find out more\">internets</a>.")
        label.set_line_wrap(True)
        vbox_left.pack_start(label, True, True, 0)
        
        label = Gtk.Label.new_with_mnemonic(
            "_Press Alt + P to select button to the right")
        vbox_left.pack_start(label, True, True, 0)
        label.set_selectable(True)

        button = Gtk.Button(label="Click at your own risk")
        label.set_mnemonic_widget(button)
        vbox_right.pack_start(button, True, True, 0)
        
        
win = LabelWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
