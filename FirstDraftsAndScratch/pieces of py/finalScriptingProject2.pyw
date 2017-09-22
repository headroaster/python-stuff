#!/usr/bin/python
import wx, os, time, shutil

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        ssbtn = wx.Button(pnl, label='Choose Source', pos=(10, 15))
        dsbtn = wx.Button(pnl, label='Choose Destination', pos=(10, 45))
        gobtn = wx.Button(pnl, label='Perform Check', pos=(10, 75))
        cbtn = wx.Button(pnl, label='Close', pos=(10, 105))

        ssbtn.Bind(wx.EVT_BUTTON, self.SrcSel)
        dsbtn.Bind(wx.EVT_BUTTON, self.DestSel)
        gobtn.Bind(wx.EVT_BUTTON, self.GoBtn)
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((350, 200))
        self.SetTitle('wx.Button')
        self.Centre()
        self.Show(True)

    def SrcSel (self, e):
        SrcSel = wx.DirDialog(None, "Select directory to search")
        SrcSelM=SrcSel.ShowModal()
        if SrcSelM == wx.ID_OK:
              print('You selected: %s\n' % SrcSel.GetPath())
              global source
              source=SrcSel.GetPath()

        else:
               print('You clicked cancel')

        return True


    def DestSel (self, e):
        DestSel = wx.DirDialog(None, "Select directory to copy to")
        DestSelM=DestSel.ShowModal()
        if DestSelM == wx.ID_OK:
              print('You selected: %s\n' % DestSel.GetPath())
              global dest
              dest=DestSel.GetPath()

        else:
               print('You clicked cancel')


        return True

    def GoBtn (self, e):

        #source=(SrcSel.GetPath())
        #dest=(DestSel.GetPath())
        os.chdir(source)
        for filename in os.listdir(os.getcwd()):
            head, tail = os.path.split(filename)
            chdate = os.path.getmtime(filename)
            #source = head
            if (int(time.time()-chdate)/3600 < 24):
                shutil.copy2(head+tail, dest)
                print ('Copied '+tail+' to '+dest+'.\n')
            else:
                print ('nothin')
                pass

    def OnClose(self, e):
        
        self.Close(True)


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
