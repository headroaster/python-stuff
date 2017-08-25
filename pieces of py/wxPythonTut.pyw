#!/usr/bin/python

# simple.py

import wx

app = wx.App()

frame = wx.Frame(None, -1, 'Example Window', size=(1280, 960))
frame.CreateStatusBar()
frameB = wx.Frame(frame, -1, 'First Interior', size = (480, 360))
frameB.CreateStatusBar()
frameB.SetStatusText('what, this?', 0)
frame.SetStatusText('and now this?', 0)
frame.Centre()
frameB.Centre()
frame.Show()
frameB.Show()
app.MainLoop()
