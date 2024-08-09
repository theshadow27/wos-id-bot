import re
import time
import hashlib
import requests

def generate_sign(fid, timestamp, secret_key):
    query_string = f"fid={fid}&time={timestamp}"
    full_string = query_string + secret_key
    sign = hashlib.md5(full_string.encode('utf-8')).hexdigest()
    return sign

def handle_message(message, bot_name, secret_key, api_url):
    # Find all 8-10 digit numbers in the message
    numbers = re.findall(r'\b\d{8,10}\b', message)
    if not numbers:
        return "No valid numbers found in the message."

    response_messages = []
    current_time = int(time.time() * 1000)

    for number in numbers:
        sign = generate_sign(number, current_time, secret_key)
        data = {
            'sign': sign,
            'fid': number,
            'time': current_time
        }

        # Call the API
        response = requests.post(api_url, data=data)
        response_json = response.json()

        if response_json['code'] == 0:
            nickname = response_json['data']['nickname']
            response_messages.append(f"{number}: {nickname}")
        else:
            response_messages.append(f"{number}: Error {response_json.get('err_code', 'Unknown error')}")

    # Return the formatted response
    return '\n'.join(response_messages)

