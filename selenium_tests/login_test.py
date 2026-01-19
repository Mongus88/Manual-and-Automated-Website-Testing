import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.get("https://www.ambringa.hu/")

time.sleep(1)

cooky_accept = driver.find_element(By.CLASS_NAME, "js-nanobar-close-cookies")
cooky_accept.click()

login = driver.find_element(By.ID, "header-middle-login")
login.click()

email_login = driver.find_element(By.ID, "email_login")
email_login.send_keys("user01@user02.hu")

password_login = driver.find_element(By.ID, "password_login")
password_login.send_keys("1234")

time.sleep(1)

accept = driver.find_element(By.XPATH, "//button[contains(., 'Belépés')]")
accept.click()
