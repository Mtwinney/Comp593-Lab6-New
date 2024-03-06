import requests 
import hashlib

# Send GET message to download the file
file_url = 'https://raw.githubusercontent.com/JeremyDalby/SampleFiles/main/dog.jpg'
resp_msg = requests.get(file_url)
# Check whether the download was successful
if resp_msg.status_code == requests.codes.ok:
# Extract binary file content from response message body
    file_content = resp_msg.content
# Calculate SHA-256 hash value  
image_hash = hashlib.sha256(file_content).hexdigest()
# Print the hash value
print(image_hash)