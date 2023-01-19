# selenium_indeed_job_app
 A simple selenium app for scraping jobs on Indeed
 
Uses the <a href="https://github.com/SeleniumHQ/selenium">Selenium</a> and <a href="https://github.com/kootenpv/yagmail">Yagmail</a> libraries

You can update your search terms ("what") and location ("where") - and Selenium Driver will return a list of job titles that match your term as well as the links to those jobs.

## You will need to create a .env file for authorization
Like this:
```
#.env
USERNAME = "myusername"
PASSWORD = "password"
SEND_TO = "send@gmail.com"
```
Or you could just put the authorization somewhere in the main app file

### More automation coming soon: 
- Automatically apply to jobs with Indeed easy apply


# How to use:
CD to directory, install requirements, then:
'''
python3 app.py
'''
