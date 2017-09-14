#c:\python

# Copyright (c) 2017 Dayan Cretan
# @file: Unclaimer.py
# @brief: Unclaims tickets gblah put in a better long descript88ion here




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("window-size=1280,1024")
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()
driver.implicitly_wait(0)

#this opens and signs in to the website for work
#userUName = input("What's your username, please? ")
#userPWord = input("What's your password, please? ")
#userLName = input("What's your last name, please? ")

base_url = "http://test.pendum.com"
driver.get(base_url + "/ServiceCenter/ServiceCallDetail.aspx?type=serviceC")
driver.find_element_by_id("txtPassword").clear()
driver.find_element_by_id("txtPassword").send_keys("BURR2015")
driver.find_element_by_id("txtName").clear()
driver.find_element_by_id("txtName").send_keys("dcretan")
driver.find_element_by_id("btnSubmit").click()
driver.find_element_by_id("MainContent_Sub3b").click()

#This scrubs for triage tickets left in the provided last name
driver.find_element_by_id("MainContent_ChildContent1_dpOpenStartDate_txtDate").clear()
driver.find_element_by_id("MainContent_ChildContent1_dpOpenStartDate_txtDate").send_keys("")
driver.find_element_by_id("MainContent_ChildContent1_txtTech").clear()
driver.find_element_by_id("MainContent_ChildContent1_txtTech").send_keys("Cretan")
driver.find_element_by_id("btnSubmit").click()

#This notes how many tickets are currently assigned to the last name provided
tickets = driver.find_element_by_id("MainContent_ChildContent1_lblRecordsCount").text
print(tickets)

#This opens the first ticket
driver.find_element_by_link_text("Call ID").click()
driver.switch_to_active_element()
driver.find_element_by_id("MainContent_ChildContent1_gvResults_lbtnServiceCall_0").click()
driver.switch_to_default_content()

#This iterates over the list of open tickets placing them all back in Tri-Attempt and assigning them all to TSR, Triage
i=0
while i < int(tickets) :
    i+=1
    driver.find_element_by_id("MainContent_ChildContent1_ModifyCall").click()
    driver.switch_to_frame("Iframe")
    driver.find_element_by_id("ddlProbTask").send_keys("SVC / SVC100 Maintenance Needed")
    driver.find_element_by_id("ddlApptStatus").send_keys("TRI-ATTMPT")
    driver.find_element_by_id("btnApptNow").click()
    driver.find_element_by_id("ddlTechnician").send_keys("TSR, Triage-888002")
    driver.find_element_by_id("btnSave").click()
    driver.switch_to.default_content()
    driver.find_element_by_id("MainContent_ChildContent1_btnNext").click()
print("Done.")
driver.close()
