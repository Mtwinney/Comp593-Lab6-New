import requests
import re

url = "http://download.videolan.org/pub/videolan/vlc/last/win64/vlc-3.0.20-win64.exe.sha256"

def url_from_hash(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None
    

hash_value = url_from_hash(url)

if hash_value:
    print("Hash Value is:", hash_value)
else:
    print("Error: SHA-256 hash value was not found")
    