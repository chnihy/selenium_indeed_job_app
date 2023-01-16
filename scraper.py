import time
import sys

from helpers import *
from url_shortener import url_shorten
from search_criteria import criteria

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Scraper:
	def __init__(self):
		# empty init vars
		self.search_criteria = {}
		self.results = []
		
		# on init, we collect search criteria via sys.stdin
		self.get_search_criteria()
		
		# set path of chrome driver
		PATH = './chromedriver'

		# init webdriver
		self.driver = webdriver.Chrome(PATH)
		
		# clearing cookies to ensure we load the right page
		self.driver.delete_all_cookies()

		# go to url
		#self.driver.get('http://www.indeed.com')
		#self.what = "python"
		#self.where = "remote"
		#self.xp = "ENTRY LEVEL"
		#days = "14"

		self.url = self.build_url()
		self.driver.get(self.url)
		
	
	def run(self):
		self.what = self.search_criteria["What"]
		self.get_results(self.what)
			
	def get_search_criteria(self):
		# take user input to populate search criteria
		for k,v in criteria.items():
			if type(v)== dict:
				print(f"{k} Select One: ")
				for kay,vee in v.items():
					print(f"  {kay}: {vee}")
				for line in sys.stdin:
					self.search_criteria[k] = criteria[k][kay]
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
		url = f"https://www.indeed.com/jobs?q={what}&l={where}&sc=0kf%3Aexplvl%28{xp}%29%3B&fromage={days}&vjk=3d6e9fa285476184"
		return url
	
	def get_results(self, what):
		# get the list of result titles and add to email content list
		result_titles = self.driver.find_elements(By.CLASS_NAME, "jcs-JobTitle")
		for result in result_titles:
			text = result.text
			if what in text.lower():
				link = url_shorten(result.get_attribute('href'))
				self.results.append(f"{text}\n")
				self.results.append(f"{link}\n\n")
				self.write_csv(f"{text.rstrip()},{link.rstrip()},\n")
		self.go_to_next_page()

	def go_to_next_page(self):
		# find next button else quit
		try:
			next_page = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='pagination-page-next']")
			next_page.click()
			self.get_results(self.what)
		except:
			self.result_summary(self.search_criteria)
			self.results.append("\n\n --- End of results --- \n")

	def result_summary(self, search_criteria):		
		totals = f"Total Results: {str(len(self.results)/2)}"
		
		self.results.insert(0, self.url)
		self.results.insert(0, totals)
		self.results.insert(0, f"{self.search_criteria['What']} | {self.search_criteria['Where']} | {self.search_criteria['Experience Level'].lower()} ")
		
	def write_csv(self, line):
		with open('jobs.txt', 'a') as csv:
			csv.write(f"{line}")
			