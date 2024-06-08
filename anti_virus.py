import http.client
import requests
import os
import json
import base64

with open('text.txt.txt ', 'rb')as f:

    file_content = f.read()
    
    test_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    api_key = 'e5b2e8b471ed089ee29d31da0683c12f4c56bc84bb859e66bd1fd2acacb0c82e'

    params = {'apikey': api_key}
    files = {'file': file_content}

    test_response = requests.post(test_url, params=params, files=files)
    data = test_response.json()

    if test_response.status_code == 200:
        data = test_response.json()
        print(f"Scan ID: {data.get('scan_id')} \nThe file you've scanned is safe (:")

    else:
        print('the file is unsafe to use')