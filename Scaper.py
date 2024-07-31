import requests
from bs4 import Beautifulsoup
def scrape_Website (url) :
response = request.get (url)
soup = 
Beautifulsoup (response.content, 'html parser')
data =
soup.get_text(seperator = '\n',
strip = True)
return data
