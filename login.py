from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Controllers import function_login, function_add_patient, function_assessment, function_measurements
import os
import time

usern = "woundtrackdemo"
userpass = "Woundtrack2020@"

function_login.login(usern, userpass)

mrn ="002"
lname = "Aguilar2 hhhhh"
fname = "Bimbim2 hhhhh "
no_wounds = 15

function_add_patient.add_patient(
    mrn,
    lname,
    fname,
    no_wounds)

function_assessment.pin("0200")

function_assessment.parameters()  

function_measurements.digital()
