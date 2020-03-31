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

def get_video_pages_from_course(course_url):
    course_name = course_url.split('/')[-1]
    browser = webdriver.Chrome(executable_path='./chromedriver', options=options)
    browser.get(course_url)
    elements = browser.find_elements_by_xpath('//*[@id="curriculum-list"]/a')
    with open(f'{course_name}.txt', 'w') as f:
        for ele in elements:
            f.write(ele.get_attribute('href') + '\n')
    browser.quit()

if not cookies_present:
    browser = webdriver.Chrome(executable_path='./chromedriver', options=options)
    browser.get('https://academy.moz.com/')
    time.sleep(60 * 5) #5 minutes to fill in userdata and then quit
    browser.quit()
else:
    #We already have our login cookies
    options.add_argument('--headless')

    if not os.path.exists('course_directory.txt'):
        #If we haven't scraped the cards off the homepage then we do that

        browser = webdriver.Chrome(executable_path='./chromedriver', options=options)
        browser.get('https://academy.moz.com/')
        elements = browser.find_elements_by_xpath('//*[@id="catalog-courses"]/a')
        with open('course_directory.txt', 'w') as f:
            for ele in elements:
                f.write(ele.get_attribute('href') + '\n')
        browser.quit()
    else:
        #Get all the links from our courses
        with open('course_directory.txt', 'r') as f:
            for line in f:
                url = line.strip()
                get_video_pages_from_course(url)

