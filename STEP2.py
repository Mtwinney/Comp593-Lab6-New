
import requests
import hashlib
import platform
import re

def vlc_url_download():
    try:
        response = requests.get("http://download.videolan.org/pub/videolan/vlc/last/win64/")
        response.raise_for_status()

        if platform.machine().endswith('64'):
            dl_link = re.search(r'href="(vlc-[\d.]+-win64\.exe)"', response.text)
        else:
            dl_link = re.search(r'href="(vlc-[\d.]+-win64\.exe)"', response.text)

        if dl_link:
            return dl_link.group(1)
        else:
            return None
    except requests.RequestException as e:
        print(f"URL Not Found: {e}")
        return None

def get_sha256_hash(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return hashlib.sha256(response.content).hexdigest()
    except requests.RequestException as e:
        print(f"Error locating {url}: {e}")
        return None

latest_vlc_vers = vlc_url_download()
if  latest_vlc_vers:
    expected_hash_url = f"http://download.videolan.org/pub/videolan/vlc/last/win64/{latest_vlc_vers}.sha256"
    expected_hash = get_sha256_hash(expected_hash_url)
    if expected_hash:
        print("Expected SHA256 hash:", expected_hash)
    else:
        print("Expected Hash Value not found")
else:
    print("Failed to locate latest VLC installer")