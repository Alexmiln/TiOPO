import requests
from bs4 import BeautifulSoup
from url_normalize import url_normalize
import os.path
from datetime import datetime
from urllib.parse import urlparse

found_urls = set()
to_visit_urls = set()
checked_urls = set()
visited_urls = set()
result = set()

valid_links = set()
invalid_links = set()

# main_link = 'http://links.qatl.ru/'
# main_link = 'http://lasdsadinks.qatl.ru/'
main_link = 'https://www.travelline.ru/'

class LINK:
	url: str
	status: int

	def __init__(self, url, status):
		self.url = url
		self.status = status


def getAbsoluteLink(main: str, found_link: str, ):
	if found_link == '#':
		return main

	if found_link is None:
		return None

	if main in found_link:
		return found_link

	if found_link.startswith(('http', 'ftp', 'tel:', 'mailto:')):
		return None

	return main_link + found_link


def parseLinks(url: str):
	reqs = requests.get(url)
	soup = BeautifulSoup(reqs.text, 'html.parser')

	for link in soup.find_all('a'):
		if url_normalize(getAbsoluteLink(url, link.get('href'))) is not None:
			found_urls.add(url_normalize(getAbsoluteLink(url, link.get('href'))))


def checkLink(url: str):
	global to_visit_urls
	global checked_urls
	code = requests.head(url).status_code
	link = LINK(url, code)
	result.add(link)
	checked_urls.add(url)
	if code < 400:
		to_visit_urls.add(url)
	else:
		visited_urls.add(url)


def checkAllUrls(url):
	i = 1
	parseLinks(url)
	visited_urls.add(url)
	for link in found_urls:
		if link not in checked_urls:
			print('CHECKING: ', link)
			checkLink(link)
		if link in to_visit_urls:
			if link not in visited_urls:
				url = link

		i = i + 1

	if url in to_visit_urls:
		if url not in visited_urls:
			checkAllUrls(url)


def writeResults(links, status):
	path = f"results/{urlparse(main_link).netloc}_{status}_links.txt"
	os.makedirs(os.path.dirname(path), exist_ok=True)
	i = 1
	with open(path, "w") as f:
		f.write(status + ' links\n')
		for link in links:
			f.write(str(i) + '. ' + link.url + ' || ' + str(link.status) + '\n')
			i = i + 1
		f.write('Total ' + status + ' links count: ' + str(len(links)) + '\n')
		f.write('Checking date: ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


try:
	print('CHECKING: ', main_link)
	checkLink(main_link)

	if main_link in to_visit_urls:
		checkAllUrls(main_link)

		for link in result:
			if link.status < 400:
				valid_links.add(link)
			else:
				invalid_links.add(link)

		writeResults(valid_links, 'valid')
		writeResults(invalid_links, 'invalid')

except requests.ConnectionError:
	print('INVALID MAIN LINK')
