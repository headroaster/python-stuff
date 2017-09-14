import datetime
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("window-size=1280,720")
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

def getTarget ():
        driver.find_element_by_id("MainContent_Sub3a").click()
        linesOfBiz = {"Cardtronics" : "2000300",  "ASAI" : "2000800", "ATM USA" : "2001200",
            "National" : "2001300", "OptConnect" : "2001600", "EGlobal ATM" : "2001700",
            "Cord Financial" : "2002000", "CT Can" : "2002300", "CAI" : "2002400",
            "First" : "2002600", "ISA" : "2003200", "Kahuna" : "2003600",  "Jarrett" : "2003800",
             "Paramount" : "2004400",  "Access One" : "2004700", "IntelliCall" : "2005900",
             "Tidel" : "2000600", "Tidel - Loomis" : "2000601"}
        tidels = ['2000600', '2000601']
        _customer = ""
        _customerName = ""
        _Serial = ""
        _Address = ""
        _Zip = ""
        _TID = ""

        if inputNotes['customerName'] in linesOfBiz:
            _customer = linesOfBiz[inputNotes['customerName']]
        else:
            pass

        if inputNotes['tid'] != (""):
            _TID = inputNotes['tid']
        else:
            _TID = ("phone support")

        if linesOfBiz[inputNotes['customerName']] != ("") or linesOfBiz[inputNotes['customerName']] not in tidels:
            _Serial = ""
        else:
            _customer = linesOfBiz[inputNotes['customerName']]
            _Serial = linesOfBiz[inputNotes['serial']]
            _TID = ""

        fields = {'Equipment' : _TID, 'Customer' : _customer, 'CustomerName' : _customerName,
                   'SerialNum' : _Serial, 'Address' : _Address, 'Zip' : _Zip}

        #This selects for either a specific or generic ticket using any combination of the 6 available fields.
        for item in fields:
            driver.find_element_by_id("MainContent_ChildContent1_txt" + item).send_keys(fields[item])
            click("MainContent_ChildContent1_btnSubmit")
            #This confirms the location, equipment, or customer
            driver.switch_to_frame("fancybox-frame")
            click("gvResults_LinkButton1_0")
        driver.switch_to.default_content()
        return


base_url = "http://test.pendum.com/ServiceCenter/ServiceCallDetail.aspx?type=serviceC"
login(base_url, "dcretan", "BURR2015")
inputNotes = gatherNotes()
getTarget()
