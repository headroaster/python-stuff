import wx
import datetime






prompts = ["What line did this\n come in on?", "Is the TID available?",
"Why is this person\n calling you?", "Callers name?",
"Callback Number?", "Is the safe serial\n available?",
"Street Address?", "Zip Code?",
"What did you do,\n or what needs\n to be done?"]


def fieldMaker(prompts, event=None):
      fieldBox = wx.BoxSizer(wx.VERTICAL)
      for item in prompts:
          n = str(prompts.index(item)+1)
          label = 'l'+n
          textBox = 't'+n
          hbox = 'hbox' + n

          hbox = wx.BoxSizer(wx.HORIZONTAL)
          label = wx.StaticText(window, 1, item)
          label.SetForegroundColour((wx.WHITE))
          hbox.Add(label, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
          window.textBox = wx.TextCtrl(window)
          hbox.Add(window.textBox, 1, wx.EXPAND|wx.ALIGN_RIGHT|wx.ALL,5)
          window.textBox.Bind(wx.EVT_TEXT, OnKeyTyped)
          fieldBox.Add(hbox, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)
          return fieldBox
          panel.Add(fieldBox)

def buttonMaker(event=None):
      buttonBox = wx.BoxSizer(wx.VERTICAL)
      hbox = wx.BoxSizer(wx.HORIZONTAL)
      window.btn2 = wx.Button(window, 1, "Clear")
      hbox.Add(window.btn2, 1, wx.ALIGN_LEFT, wx.ALL, 5)
      window.btn2.Bind(wx.EVT_BUTTON, clear)
      window.btn = wx.Button(window, 1, "Add This to Notes")
      hbox.Add(window.btn, 1, wx.ALIGN_RIGHT, wx.ALL, 5)
      window.btn.Bind(wx.EVT_BUTTON, takeNote)
      buttonBox.Add(hbox, wx.ALL, 5)
      return buttonBox
      window.SetSizer(fieldBox, buttonBox)
      panel.Add(buttonBox)


def OnKeyTyped(window, event=None):
   print (event.GetString())


def saveDocument (window, event=None):
     with open(os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
              lines = notes.readlines()
              with open (os.path.expanduser("~/Documents/notes/ticketNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "a") as finalNotes:
                  finalNotes.writelines(lines)
                  notes.close()
                  finalNotes.close()
              return


def takeNote (window, event=None):
  responses = ({window.t1 : "Customer Name: ", window.t2 : "TID:  ",
      window.t3 : "Call Driver: ", window.t5 : "Caller's Name: ",
      window.t6 : "Phone Number: ", window.t4 : "Serial Number: ",
      window.t7 : "Street Address: ", window.t8 : "ZIP or Postal Code: ",
      window.t9 : "Notes: "})
  with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "w") as notes:
      def border():
          notes.write("\n*********************************************************\n")
          return
      border()
      for item in responses:
          notes.write(responses[item] + item.GetValue() + "\n")
      border()
  window.saveDocument()
  return


def clear(window, event=None):
   fields = [window.t1, window.t2, window.t3, window.t4, window.t5, window.t6, window.t7, window.t8 , window.t9]
   for item in fields:
       item.SetValue("")


app = wx.App()
panel = wx.Panel()
panel.SetBackgroundColour(wx.BLACK)
font = wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.SLANT, wx.NORMAL)
panel.SetFont(font)
fieldMaker(prompts)
panel.SetSizer(fieldBox)
buttonMaker()
panel.SetSizer(buttonBox)
app.MainLoop()
