#!/usr/bin/python
# -*- coding: utf-8 -*-

#

from gi.repository import Gtk,GObject

class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="EntryWindow Example")

        self.set_size_request(200, 100)
        self.timeout_id = None
        
         
        vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing= 10)
        self.add(vbox)

        self.entry = Gtk.Entry()

        self.entry.set_text("Hello, World")
        vbox.pack_start(self.entry,True, True, 0)

        hbox = Gtk.Box(spacing = 6)
        vbox.pack_start(hbox,True, True, 0)

        self.check_editable = Gtk.CheckButton("Editable")
        self.check_editable.connect("toggled", self.on_editable_toggled)
        self.check_editable.set_active(True)
        
        hbox.pack_start(self.check_editable, True, True, 0)

        self.pulse = Gtk.CheckButton("Pulse")
        self.pulse.connect("toggled", self.on_pulse_toggled)
        self.pulse.set_active(False)
        hbox.pack_start(self.pulse, True, True, 0)

        self.icon = Gtk.CheckButton("Icon")
        self.icon.connect("toggled", self.on_icon_toggled)
        self.icon.set_active(False)
        hbox.pack_start(self.icon, True, True, 0)

        

    def on_editable_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)

    def on_pulse_toggled(self, button):
        if button.get_active():
            self.entry.set_progress_pulse_step(0.2)
            self.timeout_id = GObject.timeout_add(1000,self.do_pulse,None)
        else:
            GObject.source_remove(self.timeout_id)
            self.timeout_id = None
            self.entry.set_progress_pulse_step(0)

    def do_pulse(self, user_data):
        self.entry.progress_pulse()
        return True

    def on_icon_toggled(self, button):
        if button.get_active():
            stock_id = Gtk.STOCK_FIND
        else:
            stock_id = None
        self.entry.set_icon_from_stock(Gtk.EntryIconPosition.PRIMARY, stock_id)
        
                
win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
