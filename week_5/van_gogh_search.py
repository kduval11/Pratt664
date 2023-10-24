import requests
import json

base_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"

search_params = {
    "q": "van gogh",
    "isOnView": True,
    "hasImages": True
}

response = requests.get(base_url, params=search_params)

if response.status_code == 200:
    data = response.json()


    object_ids = data.get("objectIDs", [])

    
    object_id_json = json.dumps(object_ids, indent=2)

    print(object_id_json)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

