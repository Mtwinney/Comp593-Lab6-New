import requests
import re
import os
import hashlib

url = "http://download.videolan.org/pub/videolan/vlc/last/win64/vlc-3.0.20-win64.exe"
expected_hash = "d8055b6643651ca5b9ad58c438692a481483657f3f31624cdfa68b92e8394a57"


def installer_data(url, expected_hash):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        the_hash = hashlib.sha256()
        with open("vlc_installer.exe", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
                the_hash.update(chunk)
            download_hash = the_hash.hexdigest()

        if download_hash == expected_hash:
            print("Success: SHA-256 matches")
        else:
            print("Error: SHA-256 does not match")
            os.remove("vlc_installer.exe")
    except requests.RequestException as e:
        print(f"Installer download failed: {e}")

installer_data(url, expected_hash)
