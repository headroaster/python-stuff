#!/usr/bin/python

# nominimizebox.py

import wx

app = wx.App()
window = wx.Frame(None, style= wx.CAPTION | wx.CLOSE_BOX)
window.Show(True)

app.MainLoop()
