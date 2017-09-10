#c:\python
# Copyright (c) 2017 Dayan Cretan
# @file: ticketMaker.py
# @desc: creates tickets in Service Center as well as creating a locally stored document noting the tickets created

import datetime
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument("window-size=1280,1280")
driver = webdriver.Chrome(chrome_options=chrome_options)

def click (button):
    driver.find_element_by_id(button).click()
    return

def login (website, username, password):
    driver.get(website)
    driver.find_element_by_id("txtName").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    click('btnSubmit')
    return

#Detects and dismisses any pop_up alerts while collecting their messages
def dismissAlert ():
    try:
        print (driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
    except:
        pass
        return

#Gathers the notes necessary for creating a phone ticket
def gatherNotes ():
    prompts = {"customerName" : "What line is this coming in on? ", "tid" : "What's the TID? ",
        "callDriver" : "Why is this person calling you? ", "caller" : "What's their name? ",
        "callBack" : "What's their phone number? ", "serial" : "What's the serial number? ",
        "address" : "What's the street address? ", "zip" : "What's the ZIP or Postal Code? ",
        "notes" : "What did you do, or what needs to be done? "}
    gathered = ({})
    for item in prompts:
        gathered[item] = input(prompts[item])
    return gathered

#Submits a selection of the information collected in order to create the most appropriate ticket.
def getTarget ():
    driver.find_element_by_id("MainContent_Sub3a").click()
    linesOfBiz = {"Cardtronics" : "2000300",  "ASAI" : "2000800", "ATM USA" : "2001200",
        "National" : "2001300", "OptConnect" : "2001600", "EGlobal ATM" : "2001700",
        "Cord Financial" : "2002000", "CT Can" : "2002300", "CAI" : "2002400",
        "First" : "2002600", "ISA" : "2003200", "Kahuna" : "2003600",  "Jarrett" : "2003800",
         "Paramount" : "2004400",  "Access One" : "2004700", "IntelliCall" : "2005900",
         "tidel" : "2000600", "tidel - Loomis" : "2000601"}
    if inputNotes['tid'] != (""):
        TID = inputNotes['tid']
        Serial = ""
    else:
        TID = ("phone support")
    if inputNotes['customerName'] in linesOfBiz:
        customer = linesOfBiz[inputNotes['customerName']]
    else:
        customer = ("")
    if customer != (""):
        Serial = ""
    else:
        Serial = inputNotes['serial']
        TID = ""
    #This selects for either a specific or generic ticket using any combination of the 6 available fields.
    fields = {'Equipment' : TID, 'Customer' : customer, 'CustomerName' : inputNotes['customerName'],
               'SerialNum' : Serial, 'Address' : inputNotes['address'], 'Zip' : inputNotes['zip']}
    for item in fields:
        driver.find_element_by_id("MainContent_ChildContent1_txt"  + item).send_keys(fields[item])
    click("MainContent_ChildContent1_btnSubmit")
    #This confirms the location, equipment, or customer
    driver.switch_to_frame("fancybox-frame")
    click("gvResults_LinkButton1_0")
    driver.switch_to.default_content()
    return

#Submits collected information to Service Center
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
    notes = {'txtProbDesc' : inputNotes['callDriver'], 'txtCallerName' : inputNotes['caller'],
              'txtCustPhone' : inputNotes['callBack'], 'txtResolutionNotes' : inputNotes['notes'],
              'ddlCategory' : 'DISPENSER', 'ddlProblemCode' : 'Other', 'ddlRepairAction' : 'FIXED VIA PHONE'}
    for item in notes:
        driver.find_element_by_id(item).send_keys(notes[item])
        dismissAlert()
    click("btnComplete")
    dismissAlert()
    driver.switch_to.default_content()
    return

#Creates a permanent record of a temporarily saved note file.
def saveDocument ():
    with open("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "r") as notes:
            lines = notes.readlines()
            with open ("ticketNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "a") as finalNotes:
                finalNotes.writelines(lines)
                notes.close()
                finalNotes.close()
            return

#Creates a temporary record of the information collected during the call, saves that to another document
def documentThis ():
    prompts = ({"customerName" : "Customer Name: ", "tid" : "TID:  ",
        "callDriver" : "Call Driver: ", "caller" : "Caller's Name: ",
        "callBack" : "Phone Number: ", "serial" : "Serial Number: ",
        "address" : "Street Address: ", "zip" : "ZIP or Postal Code: ",
        "notes" : "Notes: "})
    with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "w") as notes:
        def border():
            notes.write("\n*********************************************************\n")
            return
        border()
        for item in prompts:
            notes.write(prompts[item]+inputNotes[item]+ "\n")
        border()
    saveDocument()
    return

#Copies the infomation submitted to Service Center noting the ticket number created and infomration presented.
def documentThat ():
    spacer = "  "
    headers = {'scn' : ('Service Call Number: ', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblServiceCall_0").text + "\n"),
       'cf' : ('Created for: ' , inputNotes['customerName']),
       'cn' : ('Caller Name: ', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_Label1_0").text + "\n"),
       'sna' : ('Store Name and Address: ', "\n" + driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblSiteLoc_0").text + "\n"),
       'add' : (spacer, driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblAddress1_0").text + "\n"),
       'city' : (spacer, driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblCity_0").text + " "),
       'state' : ("", driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblState_0").text + " "),
       'zip' : ('', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblZip_0").text + "\n"),
       'cbn' : ('Call Back Number: ', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_Label4_0").text + "\n"),
       'rfc' : ('Reason for Call: ', driver.find_element_by_id("MainContent_ChildContent1_txtDescNotes").text + "\n"),
       'rn' : ('Resolution Notes: ', driver.find_element_by_id("MainContent_ChildContent1_txtResNotes").text + "\n")}

    with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "w") as notes:
        def border():
            notes.write("\n*********************************************************\n")
            return
        border()
        for item in headers:
                notes.write(headers[item][0] + headers[item][1])
        border()
        print("Created: " + driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblServiceCall_0").text)
        notes.close()
    saveDocument()
    return

#This is the website we'll work in
base_url = "http://test.pendum.com/ServiceCenter/ServiceCallDetail.aspx?type=serviceC"
#This gathers your username, password, and last name for later use.  Hardcoded and unnecessary for now.
userUName = "dcretan"   #input("What's your username, please? ")
userPWord = "BURR2015"  #input("What's your password, please? ")
#This gathers the necessary information to fill out the ticket.
inputNotes = gatherNotes()
#This opens and signs in to the website for work
login(base_url, userUName, userPWord)
#This opens a phone support ticket making sure we're opening a ticket for a valid customer.
getTarget()
makeTicket()
#Creates .txt documents capturing call number created and  notes gathered for and submitted to this call
documentThis()
documentThat()
#Closes the browser
driver.close()
