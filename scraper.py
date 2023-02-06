import time
import datetime
import sys

from helpers import *
from url_shortener import url_shorten
from search_criteria import criteria

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class Scraper:
	def __init__(self, get_search_criteria=True):
		# empty init vars
		self.search_criteria = {}
		self.results = []
		self.csv_title = f'exports/jobs-{datetime.datetime.now()}.txt'
		self.strict_mode = False
		
		# on init, we collect search criteria via sys.stdin
		if get_search_criteria == True:
			self.get_search_criteria()
		
			
		
	
	def run(self, get_search_criteria = True):
		# set path of chrome driver
		PATH = './chromedriver'

		# init webdriver
		self.driver = webdriver.Chrome(PATH)
		
		# clearing cookies to ensure we load the right page
		self.driver.delete_all_cookies()
		
		# generate url and open in browser
		self.url = self.build_url()
		self.driver.get(self.url)
		
		# save search criteria as var for other methods
		self.what = self.search_criteria["What"]
		
		# main app method run
		self.get_results(self.what)
		
	def get_results(self, what):
		# get the list of result titles and add to email content list
		result_titles = self.driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
		
		# iterate through page titles
		for result in result_titles:
			text = result.text
			
			# adding a deeper layer of search - match EXACTLY our 'what' var
			if self.strict_mode == True:
				if what in text.lower():
					link = url_shorten(result.get_attribute('href'))
					self.results.append(f"{text}")
					self.results.append(f"{link}")
					self.write_csv(f"{text.rstrip()},{link.rstrip()},\n")
			else:
				link = url_shorten(result.get_attribute('href'))
				self.results.append(f"{text}")
				self.results.append(f"{link}")
				self.write_csv(f"{text.rstrip()},{link.rstrip()},\n")
		# click next page button
		self.go_to_next_page()	
	
	def go_to_next_page(self):
		# find next button
		try:
			next_page = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='pagination-page-next']")
			next_page.click()
			self.get_results(self.what)
		# if no more next button break loop
		except:
			self.result_summary(self.search_criteria)

	
	def result_summary(self, search_criteria):
		totals = f"Total Results: {str(len(self.results)/2)}"
		self.results.insert(0, totals)
		self.results.insert(0, f"{self.search_criteria['What']} | {self.search_criteria['Where']} | {self.search_criteria['Experience Level'].lower()} ")
		self.results.insert(0, f"URL: {self.url}")
		
	def get_search_criteria(self):
		# take user input to populate search criteria
		strict_mode = input("Strict mode? Y or N: ")
		if strict_mode.lower() == "y":
			self.strict_mode = True
		for k,v in criteria.items():
			if type(v)== dict:
				print(f"{k} Select One: ")
				for kay,vee in v.items():
					print(f"  {kay}: {vee}")
				for line in sys.stdin:
					self.search_criteria[k] = criteria[k][line.rstrip()]
					break
			else:
				print(f"{k}: ")
				for line in sys.stdin:
					self.search_criteria[k] = line.rstrip()
					break
	
	def build_url(self):

		what = self.search_criteria['What']
		where = self.search_criteria['Where']
		xp = self.search_criteria['Experience Level']
		days = self.search_criteria['Date Posted']
		remote = "&sc=0kf%3Aattr(DSQF7)"
		if xp == None:
			xp = ""
		#url = f"https://www.indeed.com/jobs?q={what}&l={where}&explvl(SENIOR_LEVEL)&fromage={days}{remote}"
		url = f"https://www.indeed.com/jobs?q={what}&l={where}{remote}explvl({xp})%3B&fromage={days}"
		return url


	def write_csv(self, line):
		with open(self.csv_title, 'a') as csv:
			csv.write(f"{line}")
			