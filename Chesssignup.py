import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--private')

driver = webdriver.Firefox(options = firefox_options)

driver.get("https://www.chess.com/")
Sign = driver.find_element(By.CLASS_NAME , "label")
Sign.click()

Sign_btn = driver.find_element(By.CLASS_NAME , "main-screen-button")
Sign_btn.click()
print("clicked")

Adv_btn = driver.find_element(By.CLASS_NAME , "skill-level-label")
Adv_btn.click()
print("clicked")
Ctn_btn1 = driver.find_element(By.CLASS_NAME , "skill-level-button")
Ctn_btn1.click()
print("clicked")
reg_input = driver.find_element(By.ID , "registration_email")

pass_input = driver.find_element(By.ID , "registration_password")

#Account Generator
characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

Gn_em = ""
for i in range(10):
    rn_let = random.choice(characters)
    Gn_em += rn_let
Gn_em += "@gmail.com"
print("email :" + Gn_em)

Gn_pass = ""
for i in range(6):
    let_pass = random.choice(characters)
    Gn_pass += let_pass
Gn_pass += "aA1"
print(f"password : {Gn_pass}")

#inserting the inputs
print("-inserting the inputs ...")

reg_input.send_keys(Gn_em)
pass_input.send_keys(Gn_pass)


Ctn_btn2 = driver.find_element(By.XPATH , "/html/body/div[1]/div/div[3]/main/div/form/div[2]/button")
Ctn_btn2.click()
print("clicked")
name_input = random.sample(characters , 7)
wait = WebDriverWait(driver, 10)
name = wait.until(EC.element_to_be_clickable((By.ID, "registration_username")))
name.send_keys(name_input)

Ctn_btn3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/main/div/form/div[3]/div/button")
Ctn_btn3.click()
print("clicked")

Skip_btn = driver.find_element(By.CLASS_NAME , "friends-later")
Skip_btn.click()
print("clicked")