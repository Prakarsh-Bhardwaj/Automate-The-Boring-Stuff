# Automail program
# Set wait times according to your network connections!
# TODO : Turn it into command line emailer and send content from a file.
# Usage : python automail.py <address>  -s <subject> -a <relative path of atachment if any> -c <content file or string> 
# IMPORTANT : geckodriver.exe needs to be present in the same directory as the program.
                                      
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time , sys 

firefox = webdriver.Firefox(executable_path=r"D:\\Programs\\geckodriver.exe")
firefox.get("https://mail.google.com")
mail = "@gmail.com"
password = ""
print("Logging In....")
mailfield = firefox.find_element_by_name("identifier")
mailfield.send_keys(mail + Keys.ENTER)
time.sleep(1)
passfield = firefox.find_element_by_name("password")
passfield.send_keys(password + Keys.ENTER)
time.sleep(10)
compose = firefox.find_element_by_css_selector(".z0 div")
compose.click()
time.sleep(10)
email = firefox.find_element_by_css_selector(".vO")
email.send_keys("bhardwajprakarsh@gmail.com")
subject = firefox.find_element_by_css_selector(".aoT")
subject.send_keys("Automail is here")
text = firefox.find_element_by_css_selector(".Am")
text.send_keys("This is a automated mail!!!")
time.sleep(1)
send = firefox.find_element_by_css_selector(".dC div")
send.click()
print("Mail sent!")

