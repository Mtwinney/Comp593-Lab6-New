import requests
import re
import os
import hashlib

def vlc_url_download(url, expected_hash):
    try:
        response = requests.get(url, stream=True)