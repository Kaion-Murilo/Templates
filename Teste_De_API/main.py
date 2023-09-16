manga_id = "f98660a1-d2e2-461c-960d-7bd13df8b76d"
import requests

base_url = "https://api.mangadex.org"

r = requests.get(f"{base_url}/manga/{manga_id}/feed")

print([chapter["id"] for chapter in r.json()["data"]])