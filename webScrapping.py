import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")

#print(result.status_code)
#print(result.headers)
src= result.content
#print(src)

url=[] 
soup = BeautifulSoup(src , 'lxml')
for h2_tag in soup.find_all('h2'):
	a_tag = h2_tag.find('a')
	url.append(a_tag.attrs['href'])
	

print(url)
'''
for link in links:
	if "About" in link.text:
		print(link)
		print(link.attrs['href'])
		'''
