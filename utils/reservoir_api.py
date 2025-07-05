import requests

BASE_URL = "https://api.reservoir.tools"

def get_top_collections(limit=10, sort_by="allTimeVolume"):
    url = f"{BASE_URL}/collections/v5"
    params = {
        "limit": limit,
        "sortBy": sort_by
    }
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()["collections"]
    else:
        print("Error:", response.status_code, response.text)
        return []
