from scraper import Scraper
from ymail import Sender

# instantiate Scraper object
scraper = Scraper()
sender = Sender()

# run browser script
scraper.browser_run()

# email results
contents = scraper.get_results()
subject = "SELENIUM APP | Today's job alerts"
sender.send(subject, contents)