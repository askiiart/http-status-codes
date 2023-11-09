import requests
import os
import json

# Replace with a known-404 page for whatever you want. Doing this so the nginx version is accurate.
url_404 = 'https://askiiart.net/sdlfjsadljfs'
html_404 = str(requests.get(url_404).text)
boykisser_url = 'https://askiiart.net/assets/boykisser.png'
gandalf_url = '/you.gif'

try:
    os.mkdir('pages')
except FileExistsError:
    pass

with open('status-codes.json', 'r') as codes_file:
    codes_dict = json.load(codes_file)

for code in codes_dict:
    new_html = html_404.replace('404 Not Found', f'{code} {codes_dict[code]}')
    if code == "404":
        new_html = new_html.replace("<h1>404 You Made A Typo In The URL, Didn't You?</h1>",
                                    f"<h1>404 You Made A Typo In The URL, Didn't You?</h1><br><img src={boykisser_url} alt=\"boykisser\" width=\"350\"")
    elif code == "300":
        # 57% Yes
        # - 43% No
        # - (300 Multiple Choices is the actual error code? Geddit?)
        new_html = new_html.replace(
            '<h1>300 Poll</h1>', '<h1>300 Poll</h1><br>57% Yes, 43% No<br>(300 Multiple Choices is the actual error code? Geddit?)')
    elif code == "403":
        new_html = new_html.replace('<h1>403 You Shall Not Pass</h1>',
                                    f'<h1>403 You Shall Not Pass</h1><br><img src={gandalf_url} alt=\"gandalf saying you looped infinitely\" width=\"350\"')
    with open(f'pages/{code}.html', 'w') as new_file:
        new_file.write(new_html)
