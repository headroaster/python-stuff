#!/usr/bin/python

# simple.py

import wx

app = wx.App()

frame = wx.Frame(None, -1, 'Example Window', size=(1280, 960), style =
                 wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER |
                 wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
frame = wx.Frame(frame, -1, 'First Interior', size = (480, 240))
frame.Centre()
frame.Show()

app.MainLoop()
