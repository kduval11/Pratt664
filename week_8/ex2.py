import cloudscraper
from bs4 import BeautifulSoup
import time

base_url = "https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86"
page_number = 0
artwork_info_list = []

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
            object_url = element.find("a")["href"]
            artist_name = element.find("h3", class_="card__title").text.strip()

            object_page = scraper.get(f"https://www.phillipscollection.org{object_url}")
            object_soup = BeautifulSoup(object_page.text, 'html.parser')
            
            artwork_info = {
                'artist': artist_name,
                'material': "",
                'dimensions': ""
            }

            ul_elements = object_soup.find_all("ul", class_="collection-meta flex-layout__item")

            for ul_element in ul_elements:
                for li_element in ul_element.find_all("li"):
                    label_element = li_element.find("span", class_="collection-meta__type")
                    value_element = li_element.find("span", class_="collection-meta__value")

                    if label_element is not None and value_element is not None:
                        label = label_element.text.strip()
                        value = value_element.text.strip()

                        key = label.lower()

                        if "material" in key or "medium" in key:
                            artwork_info["material"] = value
                        else:
                            artwork_info[key] = value

            artwork_info_list.append(artwork_info)

        page_number += 1
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print("Failed to fetch the webpage:", e)
        break

for artwork_info in artwork_info_list:
    print(artwork_info)