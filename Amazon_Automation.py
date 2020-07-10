from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from decouple import config
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
my_password = os.environ.get('My_PASS')
#my_password = str(config('My_PASS'))
#print(os.environ['MY_PASS'])
#print(my_password)

browser.get('https://www.amazon.in/')
time.sleep(1)
#assert 'Google' in browser.title
# time.sleep(2)

elem = browser.find_element_by_partial_link_text('Account & Lists') # Open your account
elem.click()
time.sleep(2)

elem = browser.find_element_by_id('ap_email')  # enter email
elem.send_keys('samihan25@gmail.com' + Keys.ENTER)
time.sleep(5)

elem = browser.find_element_by_id("ap_password")  # enter password
elem.send_keys(my_password + Keys.ENTER)
time.sleep(6)

elem = browser.find_element_by_id('twotabsearchtextbox')  # Find the search box
elem.send_keys('Agnipankh' + Keys.ENTER)
time.sleep(10)

elem = browser.find_element_by_link_text('Agnipankh')
elem.click()
time.sleep(10)

#Switch Browser Tab
#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

#windows = browser.window_handles

#time.sleep(3)
#browser.switch_to.window(windows[1])

browser.switch_to.window(browser.window_handles[1])
#elem = browser.find_element_by_tag_name('body')
#elem.send_keys(Keys.CONTROL + Keys.TAB)
time.sleep(5)

elem = browser.find_element_by_id('add-to-wishlist-button-submit')  # add to wishlist
elem.click()
time.sleep(10)

elem = browser.find_element_by_link_text('View Wish List') # view wishlist
elem.click()
time.sleep(10)

elem = browser.find_element_by_link_text('Add to Cart') # Add to cart
elem.click()
time.sleep(10)

elem = browser.find_element_by_link_text('Proceed to checkout') # proceed to buy
elem.click()
time.sleep(10)

elem = browser.find_element_by_link_text('Deliver to this address') # Deliver to this address
elem.click()
time.sleep(10)

elem = browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div[1]/form/div[1]/div[2]/div/span[1]/span/input') # Continue
elem.click()
time.sleep(10)

elem = browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/div[1]/div[2]/div/div/div/div') # deselect Amazon Pay amount
elem.click()
time.sleep(10)

browser.quit()