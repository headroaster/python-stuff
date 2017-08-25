import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

chrome_options = Options()
chrome_options.add_argument("window-size=1280,1024")

driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()

#This gathers your username, password, and last name for later use.
userUName = "dcretan"   #input("What's your username, please? ")
userPWord = "BURR2015"  #input("What's your password, please? ")

#This gathers the necessary information to fill out the ticket.
customerName = input("What line is this coming in on? ")
tid = input("What is the TID for this machine? ")
callDriver = input("Why is this person calling you? ")
caller = input("What's their name? ")
callBack = input("What's their phone number? ")
notes = input("What did you do, or what needs to be done? ")

#This opens and signs in to the website for work
base_url = "http://test.pendum.com"
driver.get(base_url + "/ServiceCenter/ServiceCallDetail.aspx?type=serviceC")
driver.find_element_by_id("txtName").send_keys(userUName)
driver.find_element_by_id("txtPassword").send_keys(userPWord)
driver.find_element_by_id("btnSubmit").click()

#This opens a phone support ticket

#This handles making sure we're opening a ticket for a valid customer.
driver.find_element_by_id("MainContent_Sub3a").click()
linesOfBiz = ({"Cardtronics" : "2000300",  "ASAI" : "2000800", "ATM USA" : "2001200", "National" : "2001300", "OptConnect" : "2001600",
              "EGlobal ATM" : "2001700", "Cord Financial" : "2002000", "CT Can" : "2002300", "CAI" : "2002400", "First" : "2002600",
              "ISA" : "2003200", "Kahuna" : "2003600",  "Jarrett" : "2003800",  "Paramount" : "2004400",  "Access One" : "2004700",
              "IntelliCall" : "2005900", "Tidel" : "2000600"})
while True:

    if customerName in linesOfBiz:
        customer = linesOfBiz[customerName]
        #print("The customer's account number is {customer}".format(customer=linesOfBiz[customerName]))
        break
    else:
        print ("'ya dun fucked up.")

tid = "phone support" #input("What's the TID?")
serial = "" #input("What's the serial number? ")
address = "" #input("What's the address? ")
zip = "" #input("What's the ZIP or Postal Code? ")

#This selects for either a specific or generic ticket using any combination of the 6 available fields.
driver.find_element_by_id("MainContent_ChildContent1_txtEquipment").send_keys(tid)
driver.find_element_by_id("MainContent_ChildContent1_txtCustomer").send_keys(customer)
#driver.find_element_by_id("MainContent_ChildContent1_txtCustomerName").send_keys(customerName)
#driver.find_element_by_id("MainContent_ChildContent1_txtSerialNum").send_keys(serial)
#driver.find_element_by_id("MainContent_ChildContent1_txtAddress").send_keys(address)
#driver.find_element_by_id("MainContent_ChildContent1_txtZip").send_keys(zip)
driver.find_element_by_id("MainContent_ChildContent1_btnSubmit").click()

#Confirms the location, equipment, or customer
driver.switch_to_frame("fancybox-frame")
driver.find_element_by_id("gvResults_LinkButton1_0").click()
driver.switch_to.default_content()

#This opens the specific ticket
driver.find_element_by_id("MainContent_ChildContent1_OpenCall").click()

#Captures the text of any alert and dismisses said alert
try:
    print (driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
except:
    print ("no alert")

#Submits note information to the ticket
driver.switch_to_frame("Iframe")
driver.find_element_by_id("ddlTask").send_keys("ITS - Internal Tech Support")
driver.find_element_by_id("btnSubmitTask").click()

try:
    print (driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
except:
    print ("no alert")


driver.find_element_by_id("txtProbDesc").send_keys(callDriver)
driver.find_element_by_id("txtCallerName").send_keys(caller)
driver.find_element_by_id("txtCustPhone").send_keys(callBack)
driver.find_element_by_id("txtResolutionNotes").send_keys(notes)

#Makes appropriate selections in the dropdowns; accepts monotonous alerts
driver.find_element_by_id("ddlCategory").send_keys("DISPENSER")
try:
    print (driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
except:
    print ("no alert")

driver.find_element_by_id("ddlProblemCode").send_keys("Other")
try:
    print (driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
except:
    print ("no alert")

driver.find_element_by_id("ddlRepairAction").send_keys("FIXED VIA PHONE")
driver.find_element_by_id("btnComplete").click()
try:
    print (driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
except:
    print ("no alert")

driver.switch_to.default_content()

#Creates .txt documents capturing call number created and  notes gathered for and submitted to this call
with open ("tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt", "w") as notes:
    notes.write("\n***************************************************************************************************\n")
    serviceCallNumber = driver.find_element_by_id("MainContent_ChildContent1_lstViewResult_lblServiceCall_0")
    notes.write(serviceCallNumber.text + " " + customerName + " \n")
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

driver.close()
