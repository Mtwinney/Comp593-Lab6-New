import requests
import hashlib
import tempfile
import re
import os

url = "http://download.videolan.org/pub/videolan/vlc/last/win64/vlc-3.0.20-win64.exe"
expected_hash = "d8055b6643651ca5b9ad58c438692a481483657f3f31624cdfa68b92e8394a57"


def vlc_url_download(url, expected_hash):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() 

        the_hash = hashlib.sha256()
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in response.iter_content(chunk_size=1024):
                temp_file.write(chunk)
                the_hash.update(chunk)
            download_hash = the_hash.hexdigest()

        if download_hash == expected_hash:
            print("Success: SHA-256 matchees")
            temp_file_path  = temp_file.name
            destination_path = os.path.join(os.getenv('Temp'), "vlc_installer.exe")
            os.rename(temp_file_path, destination_path)
            print("Installer now located in:", destination_path)
        else:
            print("Error: SHA-256 doesn't match")
    except requests.RequestException as e:
            print (f"Installers download has failed: {e}")

vlc_url_download(url, expected_hash)
