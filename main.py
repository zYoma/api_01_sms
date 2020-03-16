import requests
from twilio.rest import Client
import os
import time

url = 'http://api.vk.com/method/'
token = os.environ['sms_token']
account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

def get_json(user_id):
    method = url + 'users.get'
    data = {
        'user_ids': user_id,
        'fields': 'online',
        'access_token' : token,
        'v' : '5.103',
    }

    r = requests.get(method, data)
    return r.json()

def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='User online!',
        from_='+19367553922',
        to='+79298405593'
        )

def check_status():
    r = get_json('zyoma')
    status = r['response'][0]['online']
    if status == 1:
        send_sms()
        return True

    return False

def main():
    offline = False
    while not offline:
        offline = check_status()
        time.sleep(5)


if __name__ == '__main__':
    main()

