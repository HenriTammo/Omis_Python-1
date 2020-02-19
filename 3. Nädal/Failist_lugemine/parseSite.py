import requests
from bs4 import BeautifulSoup
page = requests.get('https://ilm.ee/')
#print(page)
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(id="header-weather")
#print(result.prettify())
hetkeIlmList =  result.find("div", class_= "row nopadding tana")
vastus = hetkeIlmList.text
#sprint(vastus)

def convert(lst):
	return(lst[0].split())
	
vastusListSegane = [vastus]
vastusList = convert(vastusListSegane)
#print(vastusList)

parseTester = "."
LoplikLause = ""
for x in vastusList:
	if x.endswith(parseTester):
		x=x+"\n"
	LoplikLause = LoplikLause + " " + x
	
print(LoplikLause)

