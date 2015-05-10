import wx
import pythoncom, pyHook
import time

FadeFocusKey = "Win+Oem_2"
WinDown = False

hotkey = None

# http://sourceforge.net/p/pyhook/wiki/PyHook_Tutorial/
def OnKeyboardEvent(event):

    print "TextCtrl" in str(wx.Window.FindFocus())
    hotkey.SetValue(event.Key)

# return True to pass the event to other handlers
    return True


class FadrFrame(wx.Frame):

	def __init__(self, parent, title):
		global hotkey
		wx.Frame.__init__(self, parent, wx.ID_ANY, title,None,None,wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
		self.panel = wx.Panel(self, wx.ID_ANY)

		text = wx.StaticText(self.panel, label="Fade Hotkey:", pos=(50,51))
		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
		text.SetFont(font)

		hotkey = wx.TextCtrl(self.panel, value="Win+/", pos=(150,50))

		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Show()

	def OnExit(self, event):
		exit()


app = wx.App(False)

frame = FadrFrame(None, "WinFadr")

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.KeyUp = OnKeyboardEvent
hm.HookKeyboard()

# Get hooked kid
pythoncom.PumpMessages()

app.MainLoop()