import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)  
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.get_text(separator='\n', strip=True)  
        return data
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"  # Return error message if the request fails
