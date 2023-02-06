import search_criteria

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", 
		"Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
		"Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", 
		"Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
		"New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", 
		"Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", 
		"Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
		
adjectives = ["","entry level", "junior"]

jobs = ["python", "developer",
		"etl", "data engineer",
		"qa", "quality assurance analyst", "qa engineer", "manual qa",
		"software tester"]
		
def run():
	sc = search_criteria
	for state in states:
		for job in jobs:
			sc["What"] = job
			sc["Where"] = state
			sc["Date Posted"] = 1
			