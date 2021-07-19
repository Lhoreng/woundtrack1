from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Controllers import function_login
import os
import time
import pyautogui
import autoit
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



def digital ():
    #
    # wound_image = function_login.driver.find_element_by_xpath('//*[@id="myImg"]').click()
    time.sleep(3)
    woundimage = os.getcwd()+"\wound.jpg"
    
    upload = function_login.driver.find_element(By.XPATH, '//*[@id="myImg"]')
    upload.click()
    time.sleep(2)
    autoit.control_set_text("Open","Edit1", woundimage)
    autoit.control_send("Open","Edit1","{ENTER}")   
    
    time.sleep(10)
    digitalbtn = function_login.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[2]/div[2]/span/div[2]/div/a')
    digitalbtn.click()
    time.sleep(15)
    # function_login.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # scrolldown = function_login.execute_script("window.scrollTo(0,5000)")
    # continuebtn = function_login.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[4]/div/button[1]')[0]
    # continuebtn.click()
    # continuebtn = function_login.driver.find_element_by_link_text("Continue").click()
    # time.sleep(5)
    # continuebtn = function_login.driver.findelement(By.linkText("CONTINUE")).click();('//*[@id="onProcessFalse-0-0"]/div[4]/div/button[1]')
    # continuebtn.click()
    pyautogui.doubleClick(1030, 855)
    # time.sleep(3)
    # pyautogui.doubleClick(866, 742)
    time.sleep(10)
  

    editdigital = function_login.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[2]/div[2]/span/div[2]/div/a')
    editdigital.click()
    # Edit digital Measurement
    
    # function_login.driver.execute_script("window.scrollTo(0,1000)")
    # source1 = function_login.driver.find_element_by_xpath('//*[@id="canvas"]')
    # action = ActionChains(function_login.driver)
    # action.drag_and_drop_by_offset(source1, 497, 2585).perform()
    time.sleep(10)
    pyautogui.dragTo(867, 918, 10)
    time.sleep(5)

    ref_obj = function_login.driver.find_element_by_xpath('//*[@id="reference-obj"]')
    ref_obj.send_keys(5)
    time.sleep(5)
    
    setbtn = function_login.driver.find_element_by_xpath('//*[@id="auto-compute"]')
    setbtn.click()
    time.sleep(3)  
    
    pyautogui.doubleClick(900, 496)
    pyautogui.doubleClick(843, 570)
    pyautogui.doubleClick(834, 662)
    pyautogui.doubleClick(845, 748)
    pyautogui.doubleClick(874, 811)
    pyautogui.doubleClick(902, 846)
    pyautogui.doubleClick(951, 851)
    pyautogui.doubleClick(1007, 834)
    pyautogui.doubleClick(1050, 794)
    pyautogui.doubleClick(1047, 702)
    pyautogui.doubleClick(1014, 626)
    pyautogui.doubleClick(971, 545)
    pyautogui.doubleClick(936, 511)
    time.sleep(5)
    undobtn = function_login.driver.find_element_by_xpath('//*[@id="area_undo"]')
    undobtn.click()
    time.sleep(5)
    clearbtn = function_login.driver.find_element_by_xpath('//*[@id="area_clear"]')
    clearbtn.click()
    pyautogui.doubleClick(900, 496)
    time.sleep(10)
    
    pyautogui.doubleClick(900, 496)
    pyautogui.doubleClick(843, 570)
    pyautogui.doubleClick(834, 662)
    pyautogui.doubleClick(845, 748)
    pyautogui.doubleClick(874, 811)
    pyautogui.doubleClick(902, 846)
    pyautogui.doubleClick(951, 851)
    pyautogui.doubleClick(1007, 834)
    pyautogui.doubleClick(1050, 794)
    pyautogui.doubleClick(1047, 702)
    pyautogui.doubleClick(1014, 626)
    pyautogui.doubleClick(971, 545)
    pyautogui.doubleClick(936, 511)
    pyautogui.doubleClick(900, 496)
    
    time.sleep(3)
    grid = function_login.driver.find_element_by_xpath('/html/body/div[6]/div/div/form/div/div[2]/div/div[1]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/table/tbody/tr[1]/td/label/input')
    grid.click()
    

    time.sleep(5)
    gran = function_login.driver.find_element_by_xpath('/html/body/div[6]/div/div/form/div/div[2]/div/div[1]/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/input[2]')
    gran.send_keys(95)
    
    time.sleep(5)
    savebtn = function_login.driver.find_element_by_xpath('/html/body/div[6]/div/div/form/div/div[2]/div/div[1]/table/tbody/tr/td[2]/div[3]/button[2]')
    savebtn.click()
 
 
def treatment_order():
       
    time.sleep(5)
    treatment = function_login.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[19]/table-column-treatment/div[3]/button')
    treatment.click()
    
    time.sleep(5)
    freq = function_login.driver.find_element_by_xpath('//*[@id="narrativeform"]/div/table/tbody/tr[3]/td[2]/span/tags-input/div/div/input')
    freq.click()
    
    time.sleep(5)
    freq_opt = function_login.driver.find_element_by_xpath('//*[@id="narrativeform"]/div/table/tbody/tr[3]/td[2]/span/tags-input/div/auto-complete/div/ul/li[1]/ti-autocomplete-match/ng-include/span')
    freq_opt.click()
    
    time.sleep(5)
    technique = function_login.driver.find_element_by_xpath('//*[@id="narrativeform"]/div/table/tbody/tr[4]/td[2]/span/label[1]/input')
    technique.click()
    
    time.sleep(5)
    cleanser = function_login.driver.find_element_by_xpath('//*[@id="narrativeform"]/div/table/tbody/tr[5]/td[2]/span/tags-input/div/div/input')
    cleanser.click()
    
    time.sleep(5)
    cleanser_opt = function_login.driver.find_element_by_xpath('//*[@id="narrativeform"]/div/table/tbody/tr[5]/td[2]/span/tags-input/div/auto-complete/div/ul/li[1]/ti-autocomplete-match/ng-include/span')
    cleanser_opt.click()
    
    
    time.sleep(5)
    insertbtn = function_login.driver.find_element_by_xpath('//*[@id="narrativeform"]/div/table/tbody/tr[23]/td[2]/button')
    insertbtn.click()
    
    time.sleep(5)
    save_form = function_login.driver.find_element_by_xpath('//*[@id="parent"]/div[2]/div/div/div/div/div[3]/div/div[1]/button')
    save_form.click()
    
def analytics():
    
    time.sleep(5)
    wound_analytics = function_login.driver.find_element_by_xpath('//*[@id="parent"]/div[2]/div/div/div/div/div[3]/ul/li[2]/a')
    wound_analytics.click()
    
    time.sleep(15)
    printbtn = function_login.driver.find_element_by_xpath('//*[@id="createRpt"]')
    printbtn.click()
    
    time.sleep(15)
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    time.sleep(5)
    
    # time.sleep(5)
    # actions = ActionChains(function_login.driver)      
    # actions.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()
    # function_login.driver.close()
    #

    # time.sleep(5)
    # treatment = function_login.driver.find_element_by_xpath('')
    # treatment.click()
    #

    
    
    
    
    
    