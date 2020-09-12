#!/usr/bin/env python3

from selenium import webdriver 
import time
import sys
from selenium.webdriver.common.keys import Keys


username = ""
password = ""



folderName = sys.argv[1]
url='https://www.github.com/'

# driver = webdriver.Chrome("/home/gourav/Downloads/chrome/chromedriver_linux64/chromedriver")

driver = webdriver.Firefox("/home/gourav/Downloads/geckodriver-v0.27.0-linux64")


driver.get('https://www.youtube.com/')
driver.find_element_by_name('search_query').send_keys("disstrack stabil")
driver.find_element_by_id('search-icon-legacy').click()
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div').click()


time.sleep(3)




# ............../////////////////opening new tab



driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(url)


driver.find_element_by_link_text("Sign in").click()
driver.find_element_by_id('login_field').send_keys(username)
driver.find_element_by_id('password').send_keys(password)

time.sleep(1)





driver.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]').click()


driver.find_element_by_link_text("New").click()
driver.find_element_by_id('repository_name').send_keys(folderName)
driver.find_element_by_id('repository_description').send_keys("Automation Project Using bash and python")

# driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button').click()
time.sleep(3)
# print(driver.find_element_by_css_selector('button.btn:nth-child(10)'))


driver.find_element_by_css_selector('button.btn:nth-child(10)').click()
driver.find_element_by_css_selector('div.Header-item:nth-child(1) > a:nth-child(1) > svg:nth-child(1)').click()
driver.get('https://github.com/LON3WO7F')
driver.find_element_by_css_selector('.box-shadow-none > nav:nth-child(1) > a:nth-child(2)').click()

"""
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.youtube.com/")

"""
