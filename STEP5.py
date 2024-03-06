import requests
import tempfile
import subprocess
import hashlib
import re
import os

url = "http://download.videolan.org/pub/videolan/vlc/last/win64/vlc-3.0.20-win64.exe"
expected_hash = "d8055b6643651ca5b9ad58c438692a481483657f3f31624cdfa68b92e8394a57"
def run_installer(url, expected_hash):
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
            print("Success: SHA-256 matches")
            # Get the path of the temporary file
            temp_file_path = temp_file.name
            # Move the temporary file to the destination folder
            file_destination = os.path.join(os.getenv('TEMP'), "vlc_installer.exe")
            # Delete the existing file if it exists
            if os.path.exists(file_destination):
                os.remove(file_destination)
            os.rename(temp_file_path, file_destination)
            print("Installer saved to:", file_destination)
            # Run the installer
            subprocess.run(file_destination, check=True)
        else:
            print("Error: SHA-256 does not match")
    except requests.RequestException as e:
        print(f"Installer download failed: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error running installer: {e}")

run_installer(url, expected_hash)
