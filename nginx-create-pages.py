import requests
import os
import json

url_404 = 'https://askiiart.net/sdlfjsadljfs'
html_404 = str(requests.get(url_404).text)

try:
    os.mkdir('pages')
except FileExistsError:
    pass

with open('status-codes.json', 'r') as codes_file:
    codes_dict = json.load(codes_file)

for code in codes_dict:
    new_html = html_404.replace('404 Not Found', f'{code} {codes_dict[code]}')
    with open(f'pages/{code}.html', 'w') as new_file:
        new_file.write(new_html)


exit()