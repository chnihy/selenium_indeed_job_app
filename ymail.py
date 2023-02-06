import yagmail
from os import environ, path
from dotenv import load_dotenv

# ENVIRONMENT CONFIG
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Sender:
	def __init__(self):
		password = environ.get('PASSWORD')
		username = environ.get('USERNAME')
		self.yag = yagmail.SMTP(username, password)
	
	def send(self, subject, contents, filepath):
		content = contents
		send_to = environ.get('SEND_TO')
		self.yag.send(send_to, subject, contents=[content, filepath])