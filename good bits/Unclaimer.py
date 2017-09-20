#c:\python
# Copyright (c) 2017 Dayan Cretan
# @file: Unclaimer.py
# @brief: Takes triage tickets in my name and reassigns them to TSR, Triage in Tri-Attempt status

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("window-size=1280,1024")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(0)
base_url = "http://test.pendum.com/ServiceCenter/ServiceCallDetail.aspx?type=serviceC"

def click (button):
    driver.find_element_by_id(button).click()
    return

#this opens and signs in to the website for work
def login ():
    driver.get(base_url)
    driver.find_element_by_id("txtName").send_keys('dcretan')
    driver.find_element_by_id("txtPassword").send_keys('BURR2015')
    click('btnSubmit')
    return

#This scrubs for triage tickets left in the provided last name
def triSearch ():
    click("MainContent_Sub3b")
    driver.find_element_by_id("MainContent_ChildContent1_dpOpenStartDate_txtDate").clear()
    driver.find_element_by_id("MainContent_ChildContent1_dpOpenStartDate_txtDate").send_keys("")
    driver.find_element_by_id("MainContent_ChildContent1_txtTech").clear()
    driver.find_element_by_id("MainContent_ChildContent1_txtTech").send_keys('Cretan')
    click("btnSubmit")
    return

#This recognizes how many tickets there are to process, prepares for re-assigning them
def acknowledge ():
    driver.find_element_by_link_text('Call ID').click()
    driver.switch_to_active_element()
    click("MainContent_ChildContent1_gvResults_lbtnServiceCall_0")
    driver.switch_to_default_content()
    return

#This iterates over the list of open tickets placing them all back in Tri-Attempt assigned to TSR, Triage
def unClaim ():
    i=0
    while i < int(tickets) :
        i+=1
        print("Working on " + str(i) + ",")
        click("MainContent_ChildContent1_ModifyCall")
        driver.switch_to_frame("Iframe")
        driver.find_element_by_id("ddlProbTask").send_keys("SVC / SVC100 Maintenance Needed")
        driver.find_element_by_id("ddlApptStatus").send_keys("TRI-ATTMPT")
        click("btnApptNow")
        driver.find_element_by_id("ddlTechnician").send_keys("TSR, Triage-888002")
        click("btnSave")
        driver.switch_to.default_content()
        click("MainContent_ChildContent1_btnNext")
    return

login()
triSearch()
tickets = driver.find_element_by_id("MainContent_ChildContent1_lblRecordsCount").text
print(tickets)
acknowledge()
unClaim()
print("Done.")
driver.close()
