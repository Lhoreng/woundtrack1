from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Controllers import function_login, function_add_patient, function_assessment, function_measurements
import os
import time

usern = "woundtrackdemo"
userpass = "Woundtrack2020@"

function_login.login(usern, userpass)

fname_random = ["Leonel", "Juana", "Deandra", "Jazmin", "Keila", "Claudine", "Kathleen", "Sandra", "Yael", "Frieda", "Emile", "Dane", "Carmella", "Rosalva", "Denita", "Marvis", "Vilma", "Lucila", "Coral", "James", "Jerald", "Buford", "Vennie" ] 

lname_random = ["Cathy", "Melody", "Siobhan", "Annmarie", "Tanna", "Liliana", "Keshia", "Irwin", "Jacqualine", "Leigh", "Sulema", "Marty", "Mike", "Shonta", "Lane", "Eldora", "Adah", "Leland", "Teresia", "Chloe", "Cordie", "Hal", "Sherryl", "Reggie", "Chery", "Columbus", "Edith"]
    
fn = random.choice(fname_random)
ln = random.choice(lname_random)
mrn = random.randint(0, 999)
no_wounds = random.randint(0, 99)

# mrn ="002"
# lname = "Aguilar2"
# fname = "Bimbim2"
# no_wounds = 15

function_add_patient.add_patient(
    mrn,
    str(ln),
    str(fn),
    no_wounds)

function_assessment.pin("0200")

function_assessment.parameters()  

function_measurements.digital()