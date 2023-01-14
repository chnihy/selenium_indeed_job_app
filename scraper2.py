from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import *
from url_shortener import url_shorten
from search_criteria import criteria

import time
import sys



class Scraper:
	def __init__(self):
		# empty init vars
		#self.search_criteria = {}
		self.results = []
		
		# on init, we collect search criteria via sys.stdin
		#self.get_search_criteria()
		
		# set path of chrome driver
		PATH = './chromedriver'

		# init webdriver
		self.driver = webdriver.Chrome(PATH)
		
		# clearing cookies to ensure we load the right page
		self.driver.delete_all_cookies()

		# go to url
		#self.driver.get('http://www.indeed.com')
		self.what = "python"
		where = "remote"
		xp = "ENTRY LEVEL"
		days = "14"
		self.driver.get(f"https://www.indeed.com/jobs?q={self.what}&l={where}&sc=0kf%3Aexplvl%28{xp}%29%3B&fromage={days}&vjk=3d6e9fa285476184")
		
	
	def browser_run(self):
		## getting our search criteria vars
		#what_search_term = self.search_criteria["What"]
		#where_search_term = self.search_criteria["Where"]
		#date_posted = self.search_criteria["Date Posted"]
		#experience_level = self.search_criteria["Experience Level"]
		#
		## find all text fields on page
		#text_fields = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
#
		## create vars for fields
		#what = text_fields[0]
		#where = text_fields[1]
#
		## enter 'what' field text
		#what.send_keys(what_search_term)
#
		## Clear 'where' text - TODO: make this better
		#where.send_keys(Keys.BACK_SPACE * 25)
#
		## Enter new text into the text field
		#where.send_keys(where_search_term)
#
		## select Submit button
		#submit_btn = self.driver.find_element(By.CLASS_NAME, "yosegi-InlineWhatWhere-primaryButton")
		#submit_btn.click()
		#
		#time.sleep(2)
		#if date_posted != "":
		#	self.date_posted_criteria(date_posted)
		#
		#time.sleep(2)
		#if experience_level != "":
		#	self.experience_level_criteria(experience_level)
		#
		#time.sleep(2)
		self.get_results()
			
	

	def get_search_criteria(self):
		# take user input to populate search criteria
		for k,v in criteria.items():
			if type(v)== dict:
				print("select one: ")
				for kay,vee in v.items():
					print(f"  {kay}: {vee}")
			else:
				print(f"{k}: ")
			for line in sys.stdin:
				self.search_criteria[k] = line.rstrip()
				break

	def date_posted_criteria(self, date_posted):
		# update date posted criteria
		# retrieving the text from criteria dict
		dp = criteria['Date Posted'][date_posted]
		
		# finding/clicking date posted button
		date_posted_btn = self.driver.find_element(By.ID, "filter-dateposted")
		date_posted_btn.click()
		
		# finding/clickin our dp selection
		selection = self.driver.find_element(By.XPATH, f"//*[text()='{dp}']")
		selection.click()
	
	def experience_level_criteria(self, experience_level):
		# update experience level criteria
		# retrieving the text from criteria dict
		xp = criteria['Experience Level'][experience_level]
		print(xp)
		
		# finding/clicking date posted button
		xp_btn = self.driver.find_element(By.ID, "filter-explvl")
		xp_btn.click()
		
		# finding/clickin our xp selection
		#selection = .driver.find_element(By.XPATH, f"//*[text()='{xp}']")
		selection = self.driver.find_elements(By.CLASS_NAME, f"//*[contains(text(),'{xp}')]")
		print(selection.text)
		#selection = self.driver.find_element(By.CLASS_NAME, "yosegi-FilterPill-dropdownListItemLink")
		
		
	
	def get_results(self):
		# get the list of result titles and add to email content list
		result_titles = self.driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
		for result in result_titles:
			text = result.text + '\n'
			if self.what in text:
				link = url_shorten(result.get_attribute('href')) + '\n\n'
				self.results.append(text)
				self.results.append(link)
			#if self.search_criteria["What"] in text:
			#	link = url_shorten(result.get_attribute('href')) + '\n\n'
			#	self.results.append(text)
			#	self.results.append(link)
		self.go_to_next_page()

	def go_to_next_page(self):
		# find next button else quit
		try:
			next_page = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='pagination-page-next']")
			next_page.click()
			self.get_results()
		except:
			self.result_summary()
			self.results.append("\n\n --- End of results --- \n")

	def result_summary(self):
		#title = f"{self.search_criteria['What']} | {self.search_criteria['Where'] } | {self.search_criteria['Date Posted']} \n\n"
		
		totals = f"Total Results: {str(len(self.results))}"
		
		self.results.insert(0, totals)
		self.results.insert(0, title)