import requests
import json

base_search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
base_object_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

search_params = {
    "q": "van gogh",
    "isOnView": 'true',
    "hasImages": 'true'
}

search_response = requests.get(base_search_url, params=search_params)

if search_response.status_code == 200:
    search_data = search_response.json()
    object_ids = search_data.get("objectIDs", [])
    
    object_titles = []


    for object_id in object_ids:
        object_details_url = f"{base_object_url}/{object_id}"
        object_details_response = requests.get(object_details_url)

        if object_details_response.status_code == 200:
            object_details = object_details_response.json()
            title = object_details.get("title", "Title not available")
            object_titles.append(title)
        else:
            object_titles.append("Title not available")

    print(object_titles)

else:
    print(f"Failed to retrieve data. Status code: {search_response.status_code}")
