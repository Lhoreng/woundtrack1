from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Controllers import function_login, function_add_patient, function_assessment
# from eclipse2.workspace2.Woundtrack import Controllers
import os
import time
import pyautogui
import autoit
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def digital ():
    #
    # wound_image = function_login.driver.find_element_by_xpath('//*[@id="myImg"]').click()
    # time.sleep(3)
    
    
    woundimage = os.getcwd()+"\wound.jpg"
    
    upload = function_login.driver.find_element(By.XPATH, '//*[@id="myImg"]')
    upload.click()
    time.sleep(2)
    autoit.control_set_text("Open","Edit1", woundimage)
    autoit.control_send("Open","Edit1","{ENTER}")   
    
    
    