import requests
from decouple import config

# env variables for twitch API
client_id = config("TWITCH_CLIENT_ID_KEY")
client_secret = config("TWITCH_CLIENT_SECRET_KEY")
streamer_name = 'LCK'

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body).json()

headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + r['access_token']
}


def isLive(streamer_name):
    stream = requests.get(
        'https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)
    stream_data = stream.json()
    if len(stream_data['data']) == 1:
        return True
    else:
        return False
