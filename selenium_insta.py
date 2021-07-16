from selenium import webdriver
import time
myUsername = "***"
myPassword = "***"

browser = webdriver.Edge(executable_path=r'***')

browser.get("https://www.instagram.com")
time.sleep(3)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
username.send_keys(myUsername)
password.send_keys(myPassword)

time.sleep(2)

login = browser.find_element_by_xpath(
    "//*[@id='loginForm']/div/div[3]/button/div")
login.click()

time.sleep(6)

browser.close()
