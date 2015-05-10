import wx

class FadrFrame(wx.Frame):

	def __init__(self, parent, title):
		global hotkey
		wx.Frame.__init__(self, parent, wx.ID_ANY, title,None,None,wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
		self.panel = wx.Panel(self, wx.ID_ANY)

		text = wx.StaticText(self.panel, label="Fade Hotkey:", pos=(50,51))
		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
		text.SetFont(font)

		text = wx.StaticText(self.panel, label="CTRL+, ALT+, WIN+, SHIFT+", pos=(126,75))
		font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
		text.SetFont(font)

		hotkey = wx.TextCtrl(self.panel, value="Win+/", pos=(150,50))

		thebutton = wx.Button(self.panel,label="Set", pos=(260,49))
		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
		thebutton.SetFont(font)
		thebutton.Bind(wx.EVT_BUTTON, self.OnSet)

		self.Bind(wx.EVT_CLOSE, self.OnExit)
		self.Show()

	def OnExit(self, event):
		exit()

	def OnSet(self, event):
		# Grabs the old dumb value of the textbox, destroys the textbox, and makes a new read-only textbox
		global hotkey
		oldvalue = hotkey.GetValue()
		hotkey.Destroy()
		hotkey = wx.TextCtrl(self.panel, value=oldvalue, pos=(150,50), style= wx.TE_READONLY)


app = wx.App(False)

frame = FadrFrame(None, "WinFadr")

app.MainLoop()