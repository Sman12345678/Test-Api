import requests
from bs4 import BeautifulSoup
import urllib3
"""
I disabled ssl certificate check, be careful bro
But with it disabled we can scrap many sites.
"""

# Disable annoying warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_website(url):
    try:
        # SSL verification disabled✌️
        response = requests.get(url, verify=False)  
        response.raise_for_status()  
        
        # Parse the content
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.get_text(separator='\n', strip=True)  # Extract the text
        
        return data
    except requests.exceptions.RequestException as e:
        # W check errors. 
        return f"An error bro: {e}"  
