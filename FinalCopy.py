
import requests
import hashlib
import tempfile
import re
import os
import subprocess
import sys

def main():
    #1
    url = "http://download.videolan.org/pub/videolan/vlc/last/win64/vlc-3.0.20-win64.exe.sha256"
    url1 = "http://download.videolan.org/pub/videolan/vlc/last/win64/vlc-3.0.20-win64.exe"
    expected_hash = "d8055b6643651ca5b9ad58c438692a481483657f3f31624cdfa68b92e8394a57"

    expected_sha256 = get_expected_sha256(url)

    if expected_sha256:
        print("Expected SHA-256 hash:", expected_sha256)
    else:
        print("Error: SHA-256 hash value was not found")

    #2
    installer_path(url1, expected_hash)

    #3
    run_installer(url, expected_hash)

def get_expected_sha256(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

def installer_path(url1, expected_hash):
    try:
        response = requests.get(url1, stream=True)
        response.raise_for_status() 

        the_hash = hashlib.sha256()
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in response.iter_content(chunk_size=1024):
                temp_file.write(chunk)
                the_hash.update(chunk)
            download_hash = the_hash.hexdigest()

        if download_hash == expected_hash:
            print("Success: SHA-256 matches")
            temp_file_path  = temp_file.name
            destination_path = os.path.join(os.getenv('Temp'), "vlc_installer.exe")
            
            # Check if the destination file already exists
            if os.path.exists(destination_path):
                os.remove(destination_path)  # Remove the existing file
            
            os.rename(temp_file_path, destination_path)
            print("Installer now located in:", destination_path)
        else:
            print("Error: SHA-256 doesn't match")
    except requests.RequestException as e:
        print(f"Installer download failed: {e}")

#4
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
            temp_file_path  = temp_file.name
            destination_path = os.path.join(os.getenv('Temp'), "vlc_installer.exe")
            
            # Check if the destination file already exists
            if os.path.exists(destination_path):
                os.remove(destination_path)  # Remove the existing file
            
            os.rename(temp_file_path, destination_path)
            print("Installer now located in:", destination_path)
        else:
            print("Error: SHA-256 doesn't match")
    except requests.RequestException as e:
        print(f"Installer download failed: {e}")
#5
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

#6
def delete_installer():
    try:
        if sys.platform.startswith('win'):
            subprocess.run(["wmic", "product", "where", "name='VLC media player'", "call", "uninstall"], check=True)
            print("VLC has been uninstalled successfully.")
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            # Uninstall VLC on Linux or macOS
            subprocess.run(["sudo", "apt-get", "remove", "--purge", "vlc"], check=True)
            print("VLC has been uninstalled successfully.")
        else:
            print("Unsupported operating system.")
    except subprocess.CalledProcessError as e:
        print(f"Error uninstalling VLC: {e}")

if __name__ == "__main__":
    delete_installer()
