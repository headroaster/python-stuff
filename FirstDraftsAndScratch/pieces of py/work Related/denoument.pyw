import os
import wx
import datetime
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("window-size=1360,1024")
driver = webdriver.Chrome(chrome_options=chrome_options)


def click (button, event = None):
 driver.find_element_by_id(button).click()
 return


def saveDocument ():
  with open(os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
      lines = notes.readlines()
      with open (os.path.expanduser("~/Documents/notes/ticketNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "a") as finalNotes:
          finalNotes.writelines(lines)
          return


def login (website, username, password):
 driver.get(website)
 driver.find_element_by_id("txtName").send_keys(username)
 driver.find_element_by_id("txtPassword").send_keys(password)
 click('btnSubmit')
 return


def gatherNotes (event = None):
    inputs = []
    with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
        for line in notes:
            inputs.append(line.rstrip('\n'))
        gathered = {}
        for item in inputs:
            gathered[inputs.index(item)+1] = [item]
        return gathered


def dismissAlert ():
 try:
     print (driver.switch_to.alert.text)
     driver.switch_to.alert.accept()
 except:
     pass
     return


def getTarget ():
 driver.find_element_by_id("MainContent_Sub3a").click()
 linesOfBiz = {"Cardtronics" : "2000300",  "ASAI" : "2000800", "ATM USA" : "2001200",
     "National" : "2001300", "OptConnect" : "2001600", "EGlobal ATM" : "2001700",
     "Cord Financial" : "2002000", "Cardtronics Canada" : "2002300", "CAI" : "2002400",
     "First" : "2002600", "ISA" : "2003200", "Kahuna" : "2003600",  "Jarrett" : "2003800",
      "Paramount" : "2004400",  "Access One" : "2004700", "IntelliCall" : "2005900",
      "tidel" : "2000600", "tidel - Loomis" : "2000601"}
 tidels = ['2000600', '2000601']
 _TID = ""
 _customer = ""
 _customerName = ""
 _Serial = ""
 _Address = ""
 _Zip = ""

 if str.split(inputNotes[1][0], ': ')[1] in linesOfBiz:
     _customer = linesOfBiz[str.split(inputNotes[1][0], ': ')[1]]
     _customerName = str.split(inputNotes[1][0], ': ')[1]
 else:
     pass

 if str.split(inputNotes[2][0], ': ')[1] == " ":
     _TID = ("phone support")
 else:
     _TID = str.split(inputNotes[2][0], ': ')[1]

 if _customer != ("") or _customer not in tidels:
     pass
 else:
     _Serial = str.split(inputNotes[6][0], ': ')[1]
     _customer = ("")

 #This selects for either a specific or generic ticket using any combination of the 6 available fields.
 fields = {'Equipment' : _TID, 'Customer' : _customer, 'CustomerName' : _customerName,
            'SerialNum' : _Serial, 'Address' : _Address, 'Zip' : _Zip}
 for item in fields:
     driver.find_element_by_id("MainContent_ChildContent1_txt"  + item).send_keys(fields[item])
 click("MainContent_ChildContent1_btnSubmit")
 #This confirms the location, equipment, or customer
 driver.switch_to_frame("fancybox-frame")
 click("gvResults_LinkButton1_0")
 driver.switch_to.default_content()
 return


def makeTicket ():
   #This opens the specific ticket
  click("MainContent_ChildContent1_OpenCall")
 #Captures the text of any alert and dismisses said alert
  dismissAlert()
 #Submits note information to the ticket
  driver.switch_to_frame("Iframe")
  driver.find_element_by_id("ddlTask").send_keys("ITS - Internal Tech Support")
  click("btnSubmitTask")
  dismissAlert()
  notes = {'txtProbDesc' : str.split(inputNotes[3][0], ': ')[1], 'txtCallerName' : str.split(inputNotes[4][0], ': ')[1],
            'txtCustPhone' : str.split(inputNotes[5][0], ': ')[1], 'txtResolutionNotes' : str.split(inputNotes[9][0], ': ')[1],
            'ddlCategory' : 'EFT', 'ddlProblemCode' : 'other', 'ddlRepairAction' : 'fixed'}
  for item in notes:
      driver.find_element_by_id(item).send_keys(notes[item])
      dismissAlert()
  click("btnComplete")
  dismissAlert()
  driver.switch_to.default_content()
  return


def documentThis ():
 prompts = {1 : "Customer Name: ", 2 : "TID:  ",
     3 : "Call Driver: ", 4 : "Caller's Name: ",
     5 : "Phone Number: ", 6 : "Serial Number: ",
     7 : "Street Address: ", 8 : "ZIP or Postal Code: ",
     9 : "Notes: "}
 with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "w") as notes:
     for item in prompts:
         notes.write(prompts[item]+" "+str.split(inputNotes[item][0], ': ')[1]+ "\n")
 return


def documentThat ():
 spacer = "  "
 headers = {'scn' : ('Service Call Number: ', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblServiceCall_0").text + "\n"),
    'cf' : ('Created for: ' , str.split(inputNotes[1][0], ': ')[1]+ "\n"),
    'cn' : ('Caller Name: ', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_Label1_0").text + "\n"),
    'sna' : ('Store Name and Address: ', "\n" + driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblSiteLoc_0").text + "\n"),
    'add' : (spacer, driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblAddress1_0").text + "\n"),
    'city' : (spacer, driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblCity_0").text + " "),
    'state' : ("", driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblState_0").text + " "),
    'zip' : ('', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblZip_0").text + "\n"),
    'cbn' : ('Call Back Number: ', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_Label4_0").text + "\n"),
    'rfc' : ('Reason for Call: ', driver.find_element_by_id("MainContent_ChildContent1_txtDescNotes").text + "\n"),
    'rn' : ('Resolution Notes: ', driver.find_element_by_id("MainContent_ChildContent1_txtResNotes").text + "\n")}

 with open (os.path.expanduser("~/Documents/notes/ticketNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "w") as notes:

     def border():
         notes.write("\n*********************************************************\n")
         return
     border()
     for item in headers:

         notes.write(headers[item][0] + headers[item][1])
     border()
     print("Created: " + driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblServiceCall_0").text)
     return


class Mywin(wx.Frame):
   def __init__(self, parent, title):
      super(Mywin, self).__init__(parent, title = title,size = (320,475), style= wx.CAPTION | wx.CLOSE_BOX)


      panel = wx.Panel(self)
      self.SetBackgroundColour(wx.BLACK)
      font = wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.SLANT, wx.NORMAL)
      self.SetFont(font)

      vbox = wx.BoxSizer(wx.VERTICAL)

      hbox1 = wx.BoxSizer(wx.HORIZONTAL)
      l1 = wx.StaticText(panel, -1, "What line did this\n come in on?")
      l1.SetForegroundColour((wx.WHITE))
      hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t1 = wx.TextCtrl(panel)
      hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox1, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)

      hbox2 = wx.BoxSizer(wx.HORIZONTAL)
      l2 = wx.StaticText(panel, -1, "Is the TID available?")
      l2.SetForegroundColour((wx.WHITE))
      hbox2.Add(l2, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t2 = wx.TextCtrl(panel)
      hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t2.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox2, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)

      hbox4 = wx.BoxSizer(wx.HORIZONTAL)
      l4 = wx.StaticText(panel, -1, "Is the safe serial\n available?")
      l4.SetForegroundColour((wx.WHITE))
      hbox4.Add(l4, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t4 = wx.TextCtrl(panel)
      hbox4.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t4.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox4, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)

      hbox7 = wx.BoxSizer(wx.HORIZONTAL)
      l7 = wx.StaticText(panel, -1, "Street Address?")
      l7.SetForegroundColour((wx.WHITE))
      hbox7.Add(l7, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t7 = wx.TextCtrl(panel)
      hbox7.Add(self.t7,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t7.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox7, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)

      hbox8 = wx.BoxSizer(wx.HORIZONTAL)
      l8 = wx.StaticText(panel, -1, "Zip Code?")
      l8.SetForegroundColour((wx.WHITE))
      hbox8.Add(l8, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t8 = wx.TextCtrl(panel)
      hbox8.Add(self.t8,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t8.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox8, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)

      hbox5 = wx.BoxSizer(wx.HORIZONTAL)
      l5 = wx.StaticText(panel, -1, "Callers name?")
      l5.SetForegroundColour((wx.WHITE))
      hbox5.Add(l5, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t5 = wx.TextCtrl(panel)
      hbox5.Add(self.t5,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t5.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox5, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)

      hbox6 = wx.BoxSizer(wx.HORIZONTAL)
      l6 = wx.StaticText(panel, -1, "Callback Number?")
      l6.SetForegroundColour((wx.WHITE))
      hbox6.Add(l6, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t6 = wx.TextCtrl(panel)
      hbox6.Add(self.t6,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t6.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox6, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)

      hbox3 = wx.BoxSizer(wx.HORIZONTAL)
      l3 = wx.StaticText(panel, -1, "Why is this person\n calling you?")
      l3.SetForegroundColour((wx.WHITE))
      hbox3.Add(l3, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t3 = wx.TextCtrl(panel)
      hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t3.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox3, 1, wx.EXPAND|wx.ALIGN_LEFT, 5)

      hbox9 = wx.BoxSizer(wx.HORIZONTAL)
      l9 = wx.StaticText(panel, -1, "What did you do,\n or what needs\n to be done?")
      l9.SetForegroundColour((wx.WHITE))
      hbox9.Add(l9,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t9 = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE)
      hbox9.Add(self.t9,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      vbox.Add(hbox9)
      self.t9.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)

      hbox10 = wx.BoxSizer(wx.HORIZONTAL)

      hbox10.AddSpacer(5)

      self.btn2 = wx.Button(panel, -1, "Clear")
      hbox10.Add(self.btn2, 1, wx.ALIGN_LEFT)
      self.btn2.Bind(wx.EVT_BUTTON, self.clear)

      hbox10.AddSpacer(5)

      self.btn2 = wx.Button(panel, -1, "Ticket")
      hbox10.Add(self.btn2, 1, wx.ALIGN_LEFT)
      self.btn2.Bind(wx.EVT_BUTTON, self.ticket)

      hbox10.AddSpacer(5)

      self.btn = wx.Button(panel, -1, "Add to Notes")
      hbox10.Add(self.btn, 1, wx.ALIGN_RIGHT)
      self.btn.Bind(wx.EVT_BUTTON, self.takeNote)

      hbox10.AddSpacer(5)

      vbox.Add(hbox10, wx.ALL)

      panel.SetSizer(vbox)

      self.Centre()
      self.Show()
      self.Fit()

   def OnKeyTyped(self, event):
      #print (event.GetString())
      pass


   def OnEnterPressed(self, event):
      print ("Enter pressed")


   def takeNote (self, event=None):
      prompts = {self.t1 : "Customer Name: ", self.t2 : "TID:  ",
          self.t3 : "Call Driver: ", self.t5 : "Caller's Name: ",
          self.t6 : "Phone Number: ", self.t4 : "Serial Number: ",
          self.t7 : "Street Address: ", self.t8 : "ZIP or Postal Code: ",
          self.t9 : "Notes: "}
      with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "w") as notes:
          for item in prompts:
              notes.write(prompts[item] + item.GetValue() + "\n")

      return


   def clear(self, event=None):
       prompts = [self.t1 , self.t2, self.t3, self.t4, self.t5, self.t6, self.t7, self.t8 , self.t9]
       for item in prompts:
           item.SetValue("")


   def ticket(self, event=None):

       website = "http://test.pendum.com/ServiceCenter/ServiceCallDetail.aspx?type=serviceC"

     #This gathers your username, and password.
       userUName = "dcretan"
       userPWord = "BURR2015"
     #This gathers the necessary information to fill out the ticket.

     #This opens and signs in to the website for work
       login(website, userUName, userPWord)
       global inputNotes
       inputNotes = gatherNotes()
     #This opens a phone support ticket making sure we're opening a ticket for a valid customer
       getTarget()
       makeTicket()
     #Creates .txt documents capturing call number created and  notes gathered for and submitted to this call
       saveDocument()
       documentThat()
       return


app = wx.App()
Mywin(None,  'Note Maker')
app.MainLoop()
