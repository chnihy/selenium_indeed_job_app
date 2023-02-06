

from urllib.parse import unquote
urls=[
	'https://www.indeed.com/jobs?q=python&l=texas&vjk=3f6ff8cc5417e485',
	'https://www.indeed.com/jobs?q=python&l=texas&sc=0kf%3Aattr%28DSQF7%29%3B&vjk=e855a872c4729a80',
	'https://www.indeed.com/jobs?q=python&l=Arizona',
	'https://www.indeed.com/jobs?q=python&l=Arizona&vjk=2d50afd45f886f06',
	'https://www.indeed.com/jobs?q=python&l=Arizona&sc=0kf%3Aattr(DSQF7)%3B'
]

for url in urls:
	print(unquote(url))


https://www.indeed.com/jobs?q=python&l=arizona&sc=0kf%3Aattr(DSQF7)explvl(SENIOR_LEVEL)%3B&fromage=1
https://www.indeed.com/jobs?q=python&l=arizona&explvl(SENIOR_LEVEL)&fromage=(1)&sc=0kf%3Aattr(DSQF7)
https://www.indeed.com/jobs?q=python&l=arizona&sc=0kf%3Aattr(DSQF7)explvl(ENTRY_LEVEL)%3B
https://www.indeed.com/jobs?q=python&l=arizona&sc=0kf%3Aattr(DSQF7)explvl(SENIOR_LEVEL)%3B&fromage=1