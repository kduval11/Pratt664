import requests
import cloudscraper
from bs4 import BeautifulSoup
import csv
import time


links = []
i=0
while i <= 2:
    time.sleep(0.25)
    page_url = f"https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86&page={i}"
    scraper = cloudscraper.create_scraper()
    page = scraper.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    primary_media_elements = soup.find_all("div", "grid__content")
    for div_elem in primary_media_elements:
        link_elem = div_elem.find('a')
        link = link_elem.attrs['href']
        links.append(link)

print(len(links))
