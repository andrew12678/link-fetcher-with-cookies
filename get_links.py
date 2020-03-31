from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import time

data_dir_name = "selenium"
cookies_present = False

if os.path.exists(data_dir_name):
    cookies_present = True

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_argument("user-data-dir={}".format(data_dir_name))

if not cookies_present:
    browser = webdriver.Chrome(executable_path='./chromedriver', options=options)
    browser.get('https://academy.moz.com/')
    time.sleep(60 * 5) #5 minutes to fill in userdata and then quit
    browser.quit()

#options.add_argument('--headless')