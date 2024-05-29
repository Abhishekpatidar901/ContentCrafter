from bs4 import BeautifulSoup
import requests

url = "https://webscrapper.io/test-sites/tables"
response = requests.get(url)
print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')