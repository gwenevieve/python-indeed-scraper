import requests
from bs4 import BeautifulSoup
import json

job_titles = ['full stack developer', 'website developer', 'ux designer', 'ux developer', 'ux/ui developer', 'front end developer']
job_city = input("City to search?")

job_data = {}

if not job_city:
	exit()
else:

	#loop through our job titles
	for val in job_titles:
		webpage_response = requests.get("https://www.indeed.ca/jobs?q=" + val + "&l=" + job_city + "&limit=2")
		webpage = webpage_response.content
		soup = BeautifulSoup(webpage, "html.parser")

	#loop through result div and get the title
		for card in soup.find_all("div", class_="result"):
			for card in card.find_all('a', attrs={'class': 'jobtitle'}):
				job_data['Job Title'] = card.getText().strip()

		for card in soup.find_all("div", class_="result"):
			for card in card.find_all('span', attrs={'class': 'company'}):
				job_data['Company'] = card.getText().strip()

		for card in soup.find_all("div", class_="result"):		
			for card in card.find_all('div', attrs={'class': 'summary'}):
				job_data['Summary'] = card.getText().strip()
	
				with open('joblist.txt', 'a') as outfile:  
					json.dump(job_data, outfile, sort_keys=True, indent=4)