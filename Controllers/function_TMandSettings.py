from Controllers import function_login
import time

def treatment():
    
    
    time.sleep(5)
    tm = function_login.driver.find_element_by_xpath('//*[@id="collapsed__nav"]/div[3]/a/i')
    tm.click()
    time.sleep(5)
    
   
    newtreatbtn = function_login.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/div/div/button')
    newtreatbtn.click()
    time.sleep(5)
    
    field = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[1]/td[2]/div/div/div/a')
    field.click()
    time.sleep(10)
    
    fieldopt = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[1]/td[2]/div/div/div/div/ul/li[2]')
    fieldopt.click()
    time.sleep(10)
    
    entry = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[2]/table/tbody/tr[2]/td[2]/div/div/input')
    entry.send_keys("sample101")
    time.sleep(10)
    
    treatmentsavebtn = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div/div[3]/div[1]/button')
    treatmentsavebtn.click()
    time.sleep(5)
    
    
def settings():
    
    settingmenu = function_login.driver.find_element_by_xpath('//*[@id="collapsed__nav"]/div[4]/a/i')
    settingmenu.click()
    time.sleep(5)
    
    compro = function_login.driver.find_element_by_xpath('//*[@id="collapsed__nav"]/div[4]/ul/li[2]/a')
    compro.click()
    time.sleep(5)
    
    admininfo = function_login.driver.find_element_by_xpath('//*[@id="Form"]/div[1]/table/tbody/tr[9]/td[2]/div[1]/div/input')
    admininfo.send_keys("medisource")
    time.sleep(5)
    
    admininfosave = function_login.driver.find_element_by_xpath('//*[@id="Form"]/div[2]/div[1]/button')
    admininfosave.click()
    time.sleep(5)
    
def logs ():
    
    auditlogs = function_login.driver.find_element_by_xpath('//*[@id="collapsed__nav"]/div[4]/ul/li[3]/a')
    auditlogs.click()
    time.sleep(5)
