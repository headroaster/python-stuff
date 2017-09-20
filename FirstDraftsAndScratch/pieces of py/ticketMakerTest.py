#c:\python
# Copyright (c) 2017 Dayan Cretan
# @file: ticketMaker.py
# @desc: creates tickets in Service Center as well as creating a locally stored
#       document noting the tickets created

import datetime
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("window-size=1280,960")
driver = webdriver.Chrome(chrome_options=chrome_options)
base_url = "http://test.pendum.com/ServiceCenter/ServiceCallDetail.aspx?type=serviceC"

def login (website, username, password):
  driver.get(website)
  driver.find_element_by_id("txtName").send_keys(username)
  driver.find_element_by_id("txtPassword").send_keys(password)
  driver.find_element_by_id("btnSubmit").click()
  return

def dismissAlert ():
    try:
        print (driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
    except:
        print ("no alert")
        return

def gatherNotes ():
    customerName = input("What line is this coming in on? ")
    tid = input("What's the tid? ")
    callDriver = input("Why is this person calling you? ")
    caller = input("What's their name? ")
    callBack = input("What's their phone number? ")
    serial =  input("What's the serial number? ")
    address = input("What's the address? ")
    zip =  input("What's the ZIP or Postal Code? ")
    notes = input("What did you do, or what needs to be done? ")
    gathered = ({'customerName': customerName, 'tid': tid, 'callDriver': callDriver,
                 'caller': caller, 'callBack': callBack, 'serial': serial,
                 'address': address, 'zip': zip, 'notes': notes})
    return gathered


def makeTicket ():
        driver.find_element_by_id("MainContent_Sub3a").click()
        linesOfBiz = ({"Cardtronics" : "2000300",  "ASAI" : "2000800", "ATM USA" : "2001200", "National" : "2001300", "OptConnect" : "2001600",
                      "EGlobal ATM" : "2001700", "Cord Financial" : "2002000", "CT Can" : "2002300", "CAI" : "2002400", "First" : "2002600",
                      "ISA" : "2003200", "Kahuna" : "2003600",  "Jarrett" : "2003800",  "Paramount" : "2004400",  "Access One" : "2004700",
                      "IntelliCall" : "2005900", "Tidel" : "2000600"})

        if inputNotes['customerName'] in linesOfBiz:
            customer = linesOfBiz[inputNotes['customerName']]
            #print("The customer's account number is {customer}".format(customer=linesOfBiz[inputNotes['customerName']]))
        else:
            customer = ("")

        if inputNotes['tid'] != (""):
            TID = inputNotes['tid']
        else:
            TID = ("phone support")

        if customer != ("") or customer != ("Tidel"):
            Serial = ""
        else:
            Serial = inputNotes['serial']

        #This selects for either a specific or generic ticket using any combination of the 6 available fields.
        driver.find_element_by_id("MainContent_ChildContent1_txtEquipment").send_keys(TID)
        driver.find_element_by_id("MainContent_ChildContent1_txtCustomer").send_keys(customer)
        driver.find_element_by_id("MainContent_ChildContent1_txtCustomerName").send_keys(inputNotes['customerName'])
        driver.find_element_by_id("MainContent_ChildContent1_txtSerialNum").send_keys(Serial)
        driver.find_element_by_id("MainContent_ChildContent1_txtAddress").send_keys(inputNotes['address'])
        driver.find_element_by_id("MainContent_ChildContent1_txtZip").send_keys(inputNotes['zip'])
        driver.find_element_by_id("MainContent_ChildContent1_btnSubmit").click()

        #Confirms the location, equipment, or customer
        driver.switch_to_frame("fancybox-frame")
        driver.find_element_by_id("gvResults_LinkButton1_0").click()
        driver.switch_to.default_content()

        #This opens the specific ticket
        driver.find_element_by_id("MainContent_ChildContent1_OpenCall").click()

        #Captures the text of any alert and dismisses said alert
        dismissAlert()

        #Submits note information to the ticket
        driver.switch_to_frame("Iframe")
        driver.find_element_by_id("ddlTask").send_keys("ITS - Internal Tech Support")
        driver.find_element_by_id("btnSubmitTask").click()

        dismissAlert()

        driver.find_element_by_id("txtProbDesc").send_keys(inputNotes['callDriver'])
        driver.find_element_by_id("txtCallerName").send_keys(inputNotes['caller'])
        driver.find_element_by_id("txtCustPhone").send_keys(inputNotes['callBack'])
        driver.find_element_by_id("txtResolutionNotes").send_keys(inputNotes['notes'])

        driver.find_element_by_id("ddlCategory").send_keys("DISPENSER")

        dismissAlert()

        driver.find_element_by_id("ddlProblemCode").send_keys("Other")

        dismissAlert()

        driver.find_element_by_id("ddlRepairAction").send_keys("FIXED VIA PHONE")
        driver.find_element_by_id("btnComplete").click()

        dismissAlert()

        driver.switch_to.default_content()
        return


def documentThis():
    with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "w") as notes:
        notes.write("\n***************************************************************************************************\n")
        notes.write("Customer Name: " + inputNotes['customerName'] + "\n")
        notes.write("TID:  " + inputNotes['tid']+ "\n")
        notes.write("Call Driver: " + inputNotes['callDriver'] + "\n")
        notes.write("Caller's Name: " + inputNotes['caller'] + "\n")
        notes.write("Phone Number: " + inputNotes['callBack'] + "\n")
        notes.write("Notes: " + inputNotes['notes'] + "\n")
        notes.write("\n***************************************************************************************************\n")
        notes.close()

    with open("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "r") as notes:
            lines = notes.readlines()
            with open ("finalNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "a") as finalNotes:
                finalNotes.writelines(lines)
                notes.close()
                finalNotes.close()
    return


def documentThat():
    with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "w") as notes:
        notes.write("\n***************************************************************************************************\n")
        serviceCallNumber = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblServiceCall_0")

        notes.write(serviceCallNumber.text + " " + inputNotes['customerName'] + " \n")
        notes.write(driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_Label1_0").text + "\n")
        notes.write(driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_Label4_0").text+ "\n")
        notes.write(driver.find_element_by_id("MainContent_ChildContent1_txtDescNotes").text+ "\n")
        notes.write(driver.find_element_by_id("MainContent_ChildContent1_txtResNotes").text+ "\n")
        notes.write("\n***************************************************************************************************\n")
        print("Created: " + serviceCallNumber.text)
        notes.close()
    with open("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "r") as notes:
            lines = notes.readlines()
            with open ("ticketNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "a") as finalNotes:
                finalNotes.writelines(lines)
                notes.close()
                finalNotes.close()
    return


#This gathers your username, password, and last name for later use.  Hardcoded and unnecessary for now.
userUName = "dcretan"   #input("What's your username, please? ")
userPWord = "BURR2015"  #input("What's your password, please? ")

#This gathers the necessary information to fill out the ticket.
inputNotes = gatherNotes()

#This opens and signs in to the website for work
login(base_url, userUName, userPWord)

#This opens a phone support ticket making sure we're opening a ticket for a valid customer.
makeTicket()

#Creates .txt documents capturing call number created and  notes gathered for and submitted to this call
documentThis()
documentThat()

driver.close()
