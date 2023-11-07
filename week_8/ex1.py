import cloudscraper
from bs4 import BeautifulSoup
import time

base_url = "https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86"
page_number = 0
artwork_titles = []

while True:
    page_url = f"{base_url}&page={page_number}"
    scraper = cloudscraper.create_scraper()

    try:
        page = scraper.get(page_url)
        page.raise_for_status()

        soup = BeautifulSoup(page.text, 'html.parser')
        primary_media_elements = soup.find_all("div", class_="card grid__item")

        if not primary_media_elements:
            break

        for element in primary_media_elements:
            artwork_title = element.find("p").text.strip()
            artwork_titles.append(artwork_title)

        page_number += 1
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print("Failed to fetch the webpage:", e)
        break

print(artwork_titles)
