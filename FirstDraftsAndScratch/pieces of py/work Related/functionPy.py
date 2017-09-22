import datetime
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("window-size=1280,720")
driver = webdriver.Chrome(chrome_options=chrome_options)
baseURL = "http://test.pendum.com/ServiceCenter/ServiceCallDetail.aspx?type=serviceC"


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
    gathered = ({'customerName': customerName, 'tid': tid, 'callDriver': callDriver, 'caller': caller, 'callBack': callBack, 'serial': serial, 'address': address, 'zip': zip, 'notes': notes})
    return gathered


def documentIt():
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

inputNotes = gatherNotes()
documentIt()
quit()
