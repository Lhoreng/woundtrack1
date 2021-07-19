from Controllers import function_login
import time
import pyautogui


def add_user(
    uln,
    ufn,
    uemail,
    un):
    
    users = function_login.driver.find_element_by_xpath('//*[@id="collapsed__nav"]/div[2]/a/i')
    users.click()
    time.sleep(5)  
    
    addbtn = function_login.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/div/div/button')
    addbtn.click()
    time.sleep(5)
    
    #add user info
    userln = function_login.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/form/div/div[2]/table/tbody/tr[1]/td[2]/div/div/input')
    userln.send_keys(ufn)
    time.sleep(5)
    
    userfn = function_login.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/form/div/div[2]/table/tbody/tr[2]/td[2]/div/div/input')
    userfn.send_keys(uln)
    time.sleep(5)
    
    user_email = function_login.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/form/div/div[2]/table/tbody/tr[3]/td[2]/div/div/input')
    user_email.send_keys(uemail)
    time.sleep(5)
    
    username = function_login.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/form/div/div[2]/table/tbody/tr[4]/td[2]/div/div/input')
    username.send_keys(un)
    time.sleep(5)
    
    title = function_login.driver.find_element_by_xpath('//html/body/div[6]/div/div/div/form/div/div[2]/table/tbody/tr[6]/td[2]/div/div/select')
    title.click()
    time.sleep(5)
    
    titleOpt = function_login.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/form/div/div[2]/table/tbody/tr[6]/td[2]/div/div/select/option[2]')
    titleOpt.click()
    time.sleep(5)
    
    pyautogui.doubleClick(728, 405)
    time.sleep(5)
    
    pm_role = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/div/div[2]/table/tbody/tr[8]/td/table/tbody/tr/td[1]/div/label/input')
    pm_role.click()
    time.sleep(5)
    
    um_role = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/div/div[2]/table/tbody/tr[8]/td/table/tbody/tr/td[2]/div/label/input')
    um_role.click()
    time.sleep(5)
    
    usersavebtn = function_login.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/div/div[3]/div[1]/button')
    usersavebtn.click()
    time.sleep(5)
    
    