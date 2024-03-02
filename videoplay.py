import keyboard
import vlc

import vlc
from tkinter import *
root=Tk()
instance=vlc.Instance()
p=instance.media_player_new()
p.set_hwnd(root.winfo_id())
try:
        libtk = 'libtk%s.dylib' % (tk.TkVersion,)
        prefix = getattr(sys, 'base_prefix', sys.prefix)
        libtk = joined(prefix, 'lib', libtk)
        dylib = cdll.LoadLibrary(libtk)
        # getNSView = dylib.TkMacOSXDrawableView is the
        # proper function to call, but that is non-public
        # (in Tk source file macosx/TkMacOSXSubwindows.c)
        # and dylib.TkMacOSXGetRootControl happens to call
        # dylib.TkMacOSXDrawableView and return the NSView
        _GetNSView = dylib.TkMacOSXGetRootControl
        # C signature: void *_GetNSView(void *drawable) to get
        # the Cocoa/Obj-C NSWindow.contentView attribute, the
        # drawable NSView object of the (drawable) NSWindow
        _GetNSView.restype = c_void_p
        _GetNSView.argtypes = c_void_p,
        del dylib

except (NameError, OSError):  # image or symbol not found

    def _GetNSView(unused):
        return None
    libtk = "N/A"

h = root.winfo_id()  # .winfo_visualid()?
                # XXX 1) using the videopanel.winfo_id() handle
                # causes the video to play in the entire panel on
                # macOS, covering the buttons, sliders, etc.
                # XXX 2) .winfo_id() to return NSView on macOS?
v= _GetNSView(h)
if v:
    p.set_nsobject(v)
else:
    p.set_xwindow(h)# plays audio, no video


p.set_media(instance.media_new("video1.mp4"))
p.play()
root.mainloop()
