from scraper import Scraper
from ymail import Sender

# instantiate Scraper and Sender objects
scraper = Scraper()
sender = Sender()

# run browser script via scraper
scraper.run()

# email results via sender
contents = scraper.results
subject = "SELENIUM APP | Today's job alerts"
sender.send(subject, contents)

# clear out csv file - because we already sent it in an email
with open('jobs.txt', 'w') as f:
	f.write('')