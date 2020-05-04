#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122"
headers = {"user-agent" : USER_AGENT}

print('Googling...') 
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]), headers=headers)
res.raise_for_status()

# Retrieve top search results links.
soup = BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
links = []
for r in soup.find_all('div', class_='r'):
  anchor = r.select('a')
  if anchor:
    link = anchor[0]['href']
    links.append(link)

numOpen = min(5, len(links))
for i in range(numOpen):
  webbrowser.open(links[i])