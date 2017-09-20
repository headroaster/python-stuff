#c:\python
# Copyright (c) 2017 Dayan Cretan
# @file: Claimer.py
# @desc: finds triage tickets and claims as many as user specifies, creates notes on which to base phone calls.

import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("window-size=1280,1024")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(0)
base_url = "http://test.pendum.com/ServiceCenter/ServiceCallDetail.aspx?type=serviceC"

#this prompts for user name, password, and last name of agent
username = 'dcretan' #input("What's your username, please? ")
userpass = 'BURR2015' #input("What's your password, please? ")
userLName = 'Cretan' #input("What's your last name, please? ")

def click (button):
    driver.find_element_by_id(button).click()
    return

def login (website, username, userpass):
    driver.get(website)
    driver.find_element_by_id("txtName").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(userpass)
    click('btnSubmit')
    return

#Searches for tickets ready to triage
def triSearch ():
    driver.find_element_by_id("MainContent_ChildContent1_dpOpenStartDate_txtDate").clear()
    driver.find_element_by_id("MainContent_ChildContent1_dpOpenStartDate_txtDate").send_keys("")
    driver.find_element_by_id("MainContent_ChildContent1_txtTech").clear()
    driver.find_element_by_id("MainContent_ChildContent1_txtTech").send_keys("tsr, triage")
    click("btnSubmit")
    driver.find_element_by_link_text('Call ID').click()
    click("MainContent_ChildContent1_gvResults_lbtnServiceCall_0")
    return

#Places a desired number of tickets in my name for processing
def inMyName ():
    print("Working on " + str(i) + ",")
    click("MainContent_ChildContent1_ModifyCall")
    driver.switch_to_frame("Iframe")
    driver.find_element_by_id("ddlProbTask").send_keys("SVC / SVC100 Maintenance Needed")
    driver.find_element_by_id("ddlApptStatus").send_keys("TRI-START")
    click("btnApptNow")
    driver.find_element_by_id("ddlTechnician").send_keys(userLName)
    click("btnSave")
    driver.switch_to.default_content()
    click("MainContent_ChildContent1_ModifyCall")
    driver.switch_to_frame("Iframe")
    driver.find_element_by_id("ddlApptStatus").send_keys("TRI-ATTMPT")
    click("btnApptNow")
    click("btnSave")
    driver.switch_to.default_content()
    noteTidel()
    click("MainContent_ChildContent1_btnNext")
    return

#Stores created notes in a local document
def saveDocument ():
    with open("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "r") as notes:
            lines = notes.readlines()
            with open ("tidelNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "a") as finalNotes:
                finalNotes.writelines(lines)
                notes.close()
                finalNotes.close()
            return

#Checks for weekends, adds part order notes
def weekendCheck ():
    def border():
        notes.write("\n*********************************************************\n")
        return
    with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "a") as notes:
        dayOfWeek = datetime.datetime.today().weekday()
        weekends = [5,6]
        if dayOfWeek in weekends:
            notes.write("     *************ATTN TECH************\n\
        No parts ordered on weekends \n\
       pull parts from truck stock or \n\
        call in to order from Choice \n\
     **********************************\n\n")
            border()
        else: border()
        notes.close()
        return

#Gathers the information needed for notes to work from
def noteTidel ():
    noteData = {
    'bT' : ('Burroughs Ticket: '  , driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblServiceCall_0").text + " \n"),
    'tT' : ('Tidel Ticket: '  , driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblPendumRef_0").text + " \n"),
    'sS' : ('Safe Serial: '  , driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lbtnEquipID_0").text + " \n"),
    'sPN' : ('Safe Part Number: '  , "" + "\n"),
    'sN' : ('Site Name: '  , driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblSiteLoc_0").text + " \n"),
    'sSA' : ('Site Address: \n'  , "    " + driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblAddress1_0").text + " \n"),
    'sC' : ('', "    " +  driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblCity_0").text + ", "),
    'sSt' : ('', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblState_0").text + "  "),
    'sZ' : ('', driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblZip_0").text + " \n"),
    'sPhN' : (''  , "Site Phone Number: " + "\n"),
    'rI' : ('Reported Issue: '  , driver.find_element_by_id("MainContent_ChildContent1_txtDescNotes").text + " \n"),
    'cN' : ('Call Notes: '  , "   " + "\n")
    }
    with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "w") as notes:
        def border():
            notes.write("\n*********************************************************\n")
            return
        border()
        for item in noteData:
                notes.write(noteData[item][0] + noteData[item][1])
        notes.close()
        weekendCheck()
    saveDocument()
    return

#This opens and signs in to the website for work
login(base_url, username, userpass)
click("MainContent_Sub3b")
#This searches for triage tickets
triSearch()
#This determines how many I want from the pool
tickets = input("How many do you want to grab?")
i=0
while i < int(tickets) :
    i+=1
#This puts the requested number in my name and provides working notes.
    inMyName()
print("Done.")
driver.close()
