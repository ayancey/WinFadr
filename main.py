import pythoncom, pyHook

FadeFocusKey = "Win+Oem_2"
WinDown = False


# http://sourceforge.net/p/pyhook/wiki/PyHook_Tutorial/
def OnKeyboardEvent(event):
	global WinDown
	global FadeFocusKey
	HotKey = FadeFocusKey
	# print 'MessageName:',event.MessageName
	# print 'Message:',event.Message
	# print 'Time:',event.Time
	# print 'Window:',event.Window
	# print 'WindowName:',event.WindowName
	# print 'Ascii:', event.Ascii, chr(event.Ascii)
	# print 'Key:', event.Key
	# print 'KeyID:', event.KeyID
	# print 'ScanCode:', event.ScanCode
	# print 'Extended:', event                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      .Extended
	# print 'Injected:', event.Injected
	# print 'Alt', event.Alt 
	# print 'Transition', event.Transition
	# print '---'

	if event.Key == 'Lwin' or event.Key == 'Rwin':
		if event.MessageName == 'key down':
			WinDown = True
		else:
			WinDown = False

	print WinDown
	if WinDown:
		HotKey = FadeFocusKey.replace("Win+","")

	if HotKey == event.Key:
		print 'KEY PRESSED'
	return True


hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.KeyUp = OnKeyboardEvent
hm.HookKeyboard()

# Get hooked kid
pythoncom.PumpMessages()