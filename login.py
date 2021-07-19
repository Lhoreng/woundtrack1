# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from Controllers import function_login, function_add_patient, function_assessment, function_measurements, function_users, function_TMandSettings
import random

usern = "woundtrackdemo"
userpass = "Woundtrack2020@"

function_login.login(usern, userpass)

fname_random = ["Leonel", "Juana", "Deandra", "Jazmin", "Keila", "Claudine", "Kathleen", "Sandra", "Yael", "Frieda", "Emile", "Dane", "Carmella", "Rosalva", "Denita", "Marvis", "Vilma", "Lucila", "Coral", "James", "Jerald", "Buford", "Vennie" ] 

lname_random = ["Cathy", "Melody", "Siobhan", "Annmarie", "Tanna", "Liliana", "Keshia", "Irwin", "Jacqualine", "Leigh", "Sulema", "Marty", "Mike", "Shonta", "Lane", "Eldora", "Adah", "Leland", "Teresia", "Chloe", "Cordie", "Hal", "Sherryl", "Reggie", "Chery", "Columbus", "Edith"]

fn = random.choice(fname_random)
ln = random.choice(lname_random)
mrn = random.randint(0, 999)
no_wounds = random.randint(0, 99)

function_add_patient.add_patient(
    mrn,
    str(ln),
    str(fn),
    no_wounds)

function_assessment.pin("0200")
function_assessment.parameters()  
function_measurements.digital()
function_measurements.treatment_order()
function_measurements.analytics()

#USERS MODULE
userln_random = ["Leonel", "Juana", "Deandra", "Jazmin", "Keila", "Claudine", "Kathleen", "Sandra", "Yael", "Frieda", "Emile", "Dane", "Carmella", "Rosalva", "Denita", "Marvis", "Vilma", "Lucila", "Coral", "James", "Jerald", "Buford", "Vennie" ] 

userfn_random = ["Cathy", "Melody", "Siobhan", "Annmarie", "Tanna", "Liliana", "Keshia", "Irwin", "Jacqualine", "Leigh", "Sulema", "Marty", "Mike", "Shonta", "Lane", "Eldora", "Adah", "Leland", "Teresia", "Chloe", "Cordie", "Hal", "Sherryl", "Reggie", "Chery", "Columbus", "Edith"]

useremail_random = ["lorraine@mailinator.com", "yow@mailinator.com", "kyla@mailinator.com", "mori@mailinator.com","ali@mailinator.com","jen@mailinator.com","jeza@mailinator.com","greg@mailinator.com","grey@mailinator.com","cong@mailinator.com","viy@mailinator.com","iris@mailinator.com","regs@mailinator.com","jazz@mailinator.com","kez@mailinator.com","loleng@mailinator.com","enzo@mailinator.com","clyde@mailinator.com","ron@mailinator.com",]

username_random = ["denden", "tesy", "gin", "gigi", "herald", "joko", "nate", "hlen" , "erene", "sue", "holly", "jenny", "raine", "cazzy"]

uln = random.choice(userln_random)
ufn = random.choice(userfn_random)
uemail = random.choice(useremail_random)
un = random.choice(username_random)

function_users.add_user(
    str(uln),
    str(ufn),
    str(uemail),
    str(un))


function_TMandSettings.treatment()

function_TMandSettings.settings()

function_TMandSettings.logs()
