import wx

class FadrFrame(wx.Frame):

	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, wx.ID_ANY, title,None,None,wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
		self.panel = wx.Panel(self, wx.ID_ANY)

		text = wx.StaticText(self.panel, label="Fade Hotkey:", pos=(50,51))
		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
		text.SetFont(font)

		wx.TextCtrl(self.panel, value="Win+/", pos=(150,50))
		self.Show()

	def OnExit(self, event):
		exit()


app = wx.App(False)

frame = FadrFrame(None, "WinFadr")

app.MainLoop()