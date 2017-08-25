#c:\python
# Copyright (c) 2017 Dayan Cretan
# @file: claimer.py
# @desc: finds triage tickets and claims as many as user specifies, creates notes on which to base phone calls.

import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("window-size=1280,1024")
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()
driver.implicitly_wait(0)

#this prompts for user name, password, and last name of agent
userUName = input("What's your username, please? ")
userPWord = input("What's your password, please? ")
userLName = input("What's your last name, please? ")

#This opens and signs in to the website for work
base_url = "http://test.pendum.com"
driver.get(base_url + "/ServiceCenter/ServiceCallDetail.aspx?type=serviceC")
driver.find_element_by_id("txtPassword").clear()
driver.find_element_by_id("txtPassword").send_keys(userPWord)
driver.find_element_by_id("txtName").clear()
driver.find_element_by_id("txtName").send_keys(userUName)
driver.find_element_by_id("btnSubmit").click()
driver.find_element_by_id("MainContent_Sub3b").click()

#This scrubs for triage tickets
driver.find_element_by_id("MainContent_ChildContent1_dpOpenStartDate_txtDate").clear()
driver.find_element_by_id("MainContent_ChildContent1_dpOpenStartDate_txtDate").send_keys("")
driver.find_element_by_id("MainContent_ChildContent1_txtTech").clear()
driver.find_element_by_id("MainContent_ChildContent1_txtTech").send_keys("tsr, triage")
driver.find_element_by_id("btnSubmit").click()
driver.find_element_by_link_text("Call ID").click()
driver.find_element_by_id("MainContent_ChildContent1_gvResults_lbtnServiceCall_0").click()

tickets = input("How many do you want to grab?")

i=0
while i < int(tickets) :
    i+=1

    #This claims the ticket
    driver.find_element_by_id("MainContent_ChildContent1_ModifyCall").click()
    driver.switch_to_frame("Iframe")
    driver.find_element_by_id("ddlProbTask").send_keys("SVC / SVC100 Maintenance Needed")
    driver.find_element_by_id("ddlApptStatus").send_keys("TRI-START")
    driver.find_element_by_id("btnApptNow").click()
    driver.find_element_by_id("ddlTechnician").send_keys(userLName)
    driver.find_element_by_id("btnSave").click()
    driver.switch_to.default_content()

    #And this will place the ticket in Attempt while I work through a pile.
    driver.find_element_by_id("MainContent_ChildContent1_ModifyCall").click()
    driver.switch_to_frame("Iframe")
    driver.find_element_by_id("ddlApptStatus").send_keys("TRI-ATTMPT")
    driver.find_element_by_id("btnApptNow").click()
    driver.find_element_by_id("btnSave").click()
    driver.switch_to.default_content()

    dayOfWeek = datetime.datetime.today().weekday()

    #This takes the necessary information from the ticket to generate preliminary notes.
    with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "w") as notes:

        notes.write("\n**************************************************************************************\n")
        burroughsTicket = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblServiceCall_0")
        notes.write("Burroughs Ticket: " + burroughsTicket.text + " \n\n")
        print("Burroughs Ticket: " + burroughsTicket.text)

        tidelTicket = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblPendumRef_0")
        notes.write("Tidel Ticket: " + tidelTicket.text + " \n\n")
        print("Tidel Ticket: " + tidelTicket.text)

        safeSerial = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lbtnEquipID_0")
        notes.write("Safe Serial: " + safeSerial.text + " \n\n")
        print("Safe Serial: " + safeSerial.text)

        safePartNumber = "Safe Part Number: "
        notes.write(safePartNumber + "\n\n")

        siteName = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblSiteLoc_0")
        notes.write("Site Name: " + siteName.text + " \n\n")
        print("Site Name: " + siteName.text)

        siteStreetAddress = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblAddress1_0")
        siteCity = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblCity_0")
        siteState = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblState_0")
        siteZip = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblZip_0")

        notes.write("Site Address: " + siteStreetAddress.text + " \n" + siteCity.text + ", " + siteState.text + ",  " + siteZip.text + " \n\n")
        print("Site Address: " + siteStreetAddress.text + " \n" + siteCity.text + ", " + siteState.text + ",  " + siteZip.text + " \n\n")

        notes.write("Site Phone Number: " + " \n\n")

        reportedIssue = driver.find_element_by_id("MainContent_ChildContent1_txtDescNotes")
        notes.write("Reported Issue: " + reportedIssue.text + " \n\n")
        print("Reported Issue: " + reportedIssue.text +"\n\n")

        notes.write("Call Notes: " + " \n\n")

        weekends = [5,6]
        if dayOfWeek in weekends:
            notes.write("*************ATTN TECH*************\n")
            notes.write("No parts ordered on weekends, \n")
            notes.write("pull parts from truck stock or \n")
            notes.write("call in to order from Choice \n")
            notes.write("***********************************\n\n")
            notes.write("********************************************\n")
        notes.close()

    with open("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "r") as notes:
        lines = notes.readlines()
        with open ("tidelNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "a") as finalNotes:
            finalNotes.writelines(lines)
            finalNotes.close()
    driver.find_element_by_id("MainContent_ChildContent1_btnNext").click()
print("Done.")
driver.close()
