import pyshorteners

def url_shorten(url):
	s = pyshorteners.Shortener()
	return s.tinyurl.short(url)
