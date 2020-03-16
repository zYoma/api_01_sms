import requests
from twilio.rest import Client
import os
import time

url = 'https://api.vk.com/method/'
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

    r = requests.post(method, params = data)
    return r.json()

def sms_sender(mesage):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= mesage,
        from_='+19367553922',
        to='+79298405593'
        )
    
    return message.sid

def get_status(user_id):
    r = get_json(user_id)
    status = r['response'][0]['online']
    return status

def main():
    while True:
        status = get_status(user_id='zyoma')
        if status == 1:
            sms_sender(mesage='User online!')
            break
        
        time.sleep(5)


if __name__ == '__main__':
    main()

