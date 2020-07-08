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
time.sleep(2)

elem = browser.find_element_by_link_text('Agnipankh')
elem.click()
time.sleep(2)

elem = browser.find_element_by_id('buy-now-button')  # buy now
elem.click()
time.sleep(2)

'''
elem = browser.find_element_by_partial_link_text('Account & Lists') # Open your account
hover = ActionChains(browser).move_to_element(elem)
hover.perform()
time.sleep(2)

elem = browser.find_element_by_xpath('/html/body/div[2]/header/div/div[1]/div[4]/div[2]/div[2]/div[2]/div[2]/a[1]/span')  # sign out
elem.click()
time.sleep(2)


elem = browser.find_element_by_id('add-to-wishlist-button-submit')  # add to wishlist
elem.click()
time.sleep(2)

elem = browser.find_element_by_id('nav-item-signout')  # sign out
elem.click()
time.sleep(2)



elem = browser.find_element_by_xpath('//*[@id="wishListMainButton-announce"]').click()  # add to wishlist
#find_element_by_xpath('//*[@id="a-autoid-1"]/span/input').click()
#//*[@id="wishListMainButton-announce"]
#elem.click()
time.sleep(2)

elem = browser.find_element_by_id('ap_email')  # enter email
elem.send_keys('samihan25@gmail.com' + Keys.ENTER)
time.sleep(2)

elem = browser.find_element_by_link_text('Add to Wish List')  # add to wishlist
elem.click()
time.sleep(2)

elem = browser.find_element_by_link_text('View Wish List') # view wishlist
elem.click()
time.sleep(2)

elem = browser.find_element_by_link_text('Add to Cart') # Add to cart
elem.click()
time.sleep(2)


elem = browser.find_element_by_partial_link_text('Proceed to Buy') # proceed to buy
elem.click()
time.sleep(2)

elem = browser.find_element_by_id('ap_email')  # enter email
elem.send_keys('samihan25@gmail.com' + Keys.ENTER)
time.sleep(2)

elem = browser.find_element_by_link_text('Proceed to checkout') # Proceed to checkout
elem.click()
time.sleep(2)

elem = browser.find_element_by_link_text('Deliver to this address') # Deliver to this address
elem.click()
time.sleep(2)

elem = browser.find_element_by_link_text('Continue') # Continue
elem.click()
time.sleep(2)

elem = browser.find_element_by_id('pp-W1vSIe-139') # Select Pay on Delivery
elem.click()
time.sleep(2)

elem = browser.find_element_by_link_text('Continue') # Continue
elem.click()
time.sleep(2)

elem = browser.find_element_by_link_text('Place your order') # Place your order
elem.click()
time.sleep(2)

elem = browser.find_element_by_partial_link_text('Hello,') # Open your account
elem.click()
time.sleep(2)

elem = browser.find_element_by_partial_link_text('Your Orders') # Open your account
elem.click()
time.sleep(2)

elem = browser.find_element_by_partial_link_text('Your Orders') # Open your account
elem.click()
time.sleep(2)

#time.sleep(20)
#browser.quit()

'''