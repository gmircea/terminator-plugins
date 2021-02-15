import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import re
import terminatorlib.plugin as plugin
from datetime import datetime

# AVAILABLE must contain a list of all the classes that you want exposed
AVAILABLE = ['TimestampConvertPlugin']

class TimestampConvertPlugin(plugin.Plugin):
    capabilities = ['terminal_menu']

    def callback(self, menuitems, menu, terminal):
        """Add our menu item to the menu"""
        self.terminal = terminal
        item = Gtk.ImageMenuItem(Gtk.STOCK_FIND)
        if terminal.vte.get_has_selection():
            clipboard = Gtk.Clipboard.get(Gdk.SELECTION_PRIMARY)
            self.selectedtext = clipboard.wait_for_text().strip()
        else:
            self.selectedtext = None

        if self.selectedtext:
            try:
                reg = re.findall(r"([0-9]+\.*[0-9]*)\:", self.selectedtext)
                if len(reg) > 0:
                    d = datetime.fromtimestamp(float(reg[0]))
                else:
                    d = datetime.fromtimestamp(float(self.selectedtext))
                displaystring = d.strftime('%Y-%m-%d %H:%M:%S')
                item.set_label("Timestamp: %s" % displaystring)
                item.set_sensitive(True)
            except ValueError:
                item.set_label("Timestamp n/a")
                item.set_sensitive(False)
        else:
            item.set_label("Timestamp...")
            item.set_sensitive(False)
        menuitems.append(item)
