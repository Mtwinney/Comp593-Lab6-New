import requests

file_url = 'https://raw.githubusercontent.com/JeremyDalby/SampleFiles/main/jokes.txt'
resp_msg = requests.get(file_url)

if resp_msg.status_code == requests.codes.ok:

    file_content = resp_msg.text

    with open(r'C:/temp/jokes.txt', 'w') as file:
        file.write(file_content)
