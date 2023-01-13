# selenium_indeed_job_app
 A simple selenium app for scraping jobs on Indeed

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
- get complete list of jobs from last X num of days
- Filter out jobs that don't feature exact search terms
- Automatically apply to jobs with Indeed easy apply

