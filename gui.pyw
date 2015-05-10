import wx
import pythoncom
import pyHook

# http://sourceforge.net/p/pyhook/wiki/PyHook_Tutorial/
def OnKeyboardEvent(event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'
    return True

class FadrFrame(wx.Frame):

	def __init__(self, parent, title):
		global hotkey
		global thebutton
		wx.Frame.__init__(self, parent, wx.ID_ANY, title,None,None,wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
		self.panel = wx.Panel(self, wx.ID_ANY)

		text = wx.StaticText(self.panel, label="Fade Hotkey:", pos=(50,51))
		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
		text.SetFont(font)

		text = wx.StaticText(self.panel, label="CTRL+, ALT+, WIN+, SHIFT+", pos=(124,75))
		font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
		text.SetFont(font)

		hotkey = wx.TextCtrl(self.panel, value="WIN+/", pos=(150,50))

		thebutton = wx.Button(self.panel,label="Set", pos=(260,49))
		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
		thebutton.SetFont(font)
		thebutton.Bind(wx.EVT_BUTTON, self.OnSet)

		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Show()

	def OnExit(self, event):
		exit()

	def OnSet(self, event):
		global hotkey
		global thebutton

		if thebutton.GetLabel() == "Set":
			oldvalue = hotkey.GetValue()
			hotkey.Destroy()
			hotkey = wx.TextCtrl(self.panel, value=oldvalue, pos=(150,50), style= wx.TE_READONLY)
			thebutton.SetLabel("Unset")
		else:
			oldvalue = hotkey.GetValue()
			hotkey.Destroy()
			hotkey = wx.TextCtrl(self.panel, value=oldvalue, pos=(150,50))
			thebutton.SetLabel("Set")


app = wx.App(False)
frame = FadrFrame(None, "WinFadr")

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.KeyUp = OnKeyboardEvent
hm.HookKeyboard()

# Get hooked kid
pythoncom.PumpMessages()

app.MainLoop()