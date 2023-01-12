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

class Scraper:
	def __init__(self):
		# set path of chrome driver
		PATH = './chromedriver'

		# init webdriver
		self.driver = webdriver.Chrome(PATH)

		# go to url
		self.driver.get('http://www.indeed.com') 

		self.results = []
		
		# clear cookies
		#driver.delete_all_cookies()
		#driver.refresh()
	
	def browser_run(self, what_search_term="Junior Python", where_search_term="Remote"):
		# find all text fields	
		text_fields = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')

		# create vars for fields
		what = text_fields[0]
		where = text_fields[1]

		# enter 'what' field text
		what.send_keys(what_search_term)

		# Clear text - TODO: make this better
		where.send_keys(Keys.BACK_SPACE * 25)

		# Enter new text into the text field
		where.send_keys(where_search_term)

		# select Submit button
		submit_btn = self.driver.find_element(By.CLASS_NAME, "yosegi-InlineWhatWhere-primaryButton")
		submit_btn.click()

		# change search criteria to 24 hours
		date_posted_btn = self.driver.find_element(By.ID, "filter-dateposted")
		date_posted_btn.click()
		selection = self.driver.find_element(By.CLASS_NAME, "yosegi-FilterPill-dropdownListItemLink")
		selection.click()

	def get_results(self):
		# get the list of result titles and add to email content list
		result_titles = self.driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
		for result in result_titles:
			text = result.text + '\n'
			link = result.get_attribute('href') + '\n\n'
			self.results.append(text)
			self.results.append(link)
		return self.results


		# close
		#self.driver.close()

		#d = Driver()