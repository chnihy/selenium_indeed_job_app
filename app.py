from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


# helper functions
def nn():
	print("\n\n")

def show_dict(obj):
	nn()
	print(" :: Dict :: ")
	for k,v in obj.__dict__.items():
		print(f"{k}: {v}")
	nn()

def show_dir(obj):
	nn()
	print(" :: Dir ::")
	for x in dir(obj):
		if "__" in x:
			pass
		else:
			print(x)
	nn()


# set path of chrome driver
PATH = './chromedriver'

# init webdriver
driver = webdriver.Chrome(PATH)

# go to url
driver.get('http://www.indeed.com') 

# clear cookies
#driver.delete_all_cookies()
#driver.refresh()

# find all text fields	
text_fields = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')

# create vars for fields
what = text_fields[0]
where = text_fields[1]

# enter 'what' field text
what.send_keys("Junior Python")

# Clear text - TODO: make this better
where.send_keys(Keys.BACK_SPACE * 25)

# Enter new text into the text field
where.send_keys("Remote")

# select Submit button
submit = driver.find_element(By.CLASS_NAME, "yosegi-InlineWhatWhere-primaryButton")
submit.click()

# get the list of result titles
result_titles = driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
for result in result_titles:
	print(result.text)
	print(result.get_attribute('href') + '\n') 

# close
driver.close()

#d = Driver()