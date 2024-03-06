import requests
# Send GET message to download the file
file_url = 'https://raw.githubusercontent.com/JeremyDalby/SampleFiles/main/jokes.txt'
resp_msg = requests.get(file_url)

# Check whether the download was successful
if resp_msg.status_code == requests.codes.ok:

# Extract text file content from response message body
    file_content = resp_msg.text

# Split the text file content into a list of jokes
jokes = file_content.split('~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# Print the 5th joke in the list
print(jokes[4])