import requests
from bs4 import BeautifulSoup

job_titles = ['full stack developer', 'website developer', 'ux designer', 'ux developer', 'ux/ui developer', 'front end developer']
job_city = input("City to search?")

if not job_city:
	exit()
else:

	#loop through our job titles
	for val in job_titles:
		webpage_response = requests.get("https://www.indeed.ca/jobs?q=" + val + "&l=" + job_city + "&limit=30")
		webpage = webpage_response.content
		soup = BeautifulSoup(webpage, "html.parser")

	#loop through result div and get the title
		for card in soup.find_all("div", class_="result"):
			cards_title = card.a.getText()
			
			for card in card.find_all('span', attrs={'class': 'company'}):
				cards_text = card.getText()

				print(cards_text)
				print(cards_title)