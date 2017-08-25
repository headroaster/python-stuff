import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(920, 480))
        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1, "What did you do or what needs to be done?")
        multiText = wx.TextCtrl(panel, -1,"",size=(640, 320), style=wx.TE_MULTILINE)
        multiText.SetInsertionPoint(0)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, multiText])
        panel.SetSizer(sizer)

app = wx.PySimpleApp()
frame = TextFrame()
frame.Centre()
frame.Show()
app.MainLoop()
