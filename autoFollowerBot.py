from selenium import webdriver
from selenium.webdriver.common.by import By
import time

############# FIREFOX WEBDRIVER ##############
#browser = webdriver.Firefox()
#browser.get('http://twitter.com/')
##############################################

############# CHROME WEBDRIVER ##############
driver = webdriver.Chrome('C:\\python\\chromedriver.exe')
driver.get('http://twitter.com/')
#############################################

############# LOGIN PAGE ####################
time.sleep(1) #wait for page to load
driver.find_element_by_css_selector("a.Button.StreamsLogin.js-login").click()  #login button

time.sleep(1) #wait for page to  load
user = driver.find_element_by_css_selector("input.text-input.email-input.js-signin-email") #username field
user.send_keys(input())


passwd = driver.find_element_by_css_selector("input[type='password']") #password field
passwd.click()
passwd.send_keys(input())


submit = driver.find_element_by_css_selector("input.submit.btn.primary-btn.js-submit") #login submit field
submit.click()
#############################################

time.sleep(2) 
# Logged in! 

############### Follow recommended followers ###################
driver.find_element_by_css_selector("a.js-view-all-link").click() #recommended followers

#### Iterate recommended Followers List ####
table = driver.find_element(By.TAG_NAME, "ol")

count = 0
for row in table.find_elements_by_css_selector("span.button-text.follow-text"):
    table = driver.find_element(By.TAG_NAME, "ol")
    row.click()
    count+=100
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, "+str(count)+")")
    
    while True:
        table = driver.find_element(By.TAG_NAME, "ol")
        time.sleep(2)
        for row in table.find_elements_by_css_selector("span.button-text.follow-text"):
            row.click()
            count+=1
            time.sleep(1)
            if (count/12 == 1):
              count = 0
              driver.refresh()
              driver.execute_script("window.scrollTo(0, 0)")
              
        else:
            break
#################################################################

# Continues following recommended followers forever until you stop! #
