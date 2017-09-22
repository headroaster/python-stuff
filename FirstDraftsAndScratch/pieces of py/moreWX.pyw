def __init__(self, parent):
    """docstring for __"""
    wx.Panel.__init__(self, parent)
    self.frame = parent

    self.main_sizer = wx.BoxSizer(wx.VERTICAL)
    self.widget_sizer = wx.BoxSizer(wx.VERTICAL)

    self.text_object = wx.StaticText(self, -1, 'Example')
    self.button_object = wx.Button(self, -1, 'QUIT')
    self.button_object.Bind(wx.EVT_BUTTON, self.on_quit)

    self.widget_sizer.Add(self.text_object, 0)
    self.widget_sizer.Add(self.button_object, 0)

    self.main_sizer.Add(self.widget_sizer, 0)


def on_quit(self, event):
    """docstring for on"""
    
