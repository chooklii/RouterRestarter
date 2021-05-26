from config import PASSWORD
import schedule
import time

#Import necessary packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

sSiteUrl = "http://192.168.0.1/"
sSettingsUrl = "?status_restart&mid=StatusRestart"

sXPathUsername = "//input[@id='UserName']"
sXPathPassword = "//input[@id='Password']"
sXPathButtonLogin = "//input[@id='LoginBtn']"
sXPathButtonRestart = "//input[@id='PAGE_RESTART_RESTART']"
sXPathConfirmRestart = "//input[@id='PAGE_RESTART_POPUP_APPLY1']"

# init selenium Driver
def initSelenium():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--ignore-certificate-errors")
    Cdriver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    Cdriver.get(sSiteUrl)
    return Cdriver

# login to Router
def login(driver):
    # insert Password
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, sXPathPassword)))
    inputPassword = driver.find_element_by_xpath(sXPathPassword)
    inputPassword.send_keys(PASSWORD)

    # Login
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, sXPathButtonLogin)))
    buttonLogin = driver.find_element_by_xpath(sXPathButtonLogin)
    buttonLogin.click()
    return

def restartRouter(driver):
    # Navigate to Restart Button
    driver.get(sSiteUrl + sSettingsUrl)
    # Restart
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, sXPathButtonRestart)))
    buttonRestart = driver.find_element_by_xpath(sXPathButtonRestart)
    buttonRestart.click()

    # ConfirmRestart
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, sXPathConfirmRestart)))
    confirmRestart = driver.find_element_by_xpath(sXPathConfirmRestart)
    confirmRestart.click()


def restart():
    print("Restart Router")
    driver = initSelenium()
    login(driver)
    restartRouter(driver)
    time.sleep(5)

schedule.every().day.at("03:00").do(restart)

while True:
    schedule.run_pending()
    time.sleep(600)
