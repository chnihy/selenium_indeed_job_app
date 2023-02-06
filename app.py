import os
from scraper import Scraper
from ymail import Sender
import datetime
from search_criteria import jobs, states

# instantiate Scraper and Sender objects
all_states = input("All states? y or n ")
if all_states.lower() != "y":
	scraper = Scaper()
sender = Sender()

# build search criterias
if all_states.lower() == "y":
	print("*")
	for state in states:
		for job in jobs:
			# init new scraper obj
			scraper = Scraper(get_search_criteria=False)
			
			# build search criteria
			scraper.search_criteria["What"] = job
			scraper.search_criteria["Where"] = state
			scraper.search_criteria["Date Posted"] = "1"
			scraper.search_criteria["Experience Level"] = "ENTRY_LEVEL"
			
			# run browser script via scraper
			print(scraper.search_criteria)
			scraper.run()
			
			# email results via sender
			contents = scraper.results
			subject = f"SELENIUM || {scraper.what} {datetime.datetime.today()}"
			filepath = scraper.csv_title
			if len(scraper.results) > 3:
				sender.send(subject, contents, filepath)

else:
	scraper.run()
	# email results via sender
	contents = scraper.results
	subject = f"SELENIUM || {scraper.what} {datetime.datetime.today()}"
	filepath = scraper.csv_title
	sender.send(subject, contents, filepath)

# delete csv file - because we already sent it in an email
os.remove(filepath)
#with open(f'exports/jobs-{scraper.csv_title}.txt', 'w') as f:
#	f.write('')