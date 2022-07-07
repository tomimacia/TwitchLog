import requests

# poner tus datos de la api de twitch https://dev.twitch.tv/console/apps
client_id = 'uhi95gfyhdkgy8jxsabjw0vc10zpzj'
client_secret = '3g64x8o0dbyvwvzxilqdn6fnfas6wk'
streamer_name = 'LCK'

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body).json()

# data output



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
        #  print(streamer_name + ' is live: ' +
        #   stream_data['data'][0]['title'] + ' playing ' + stream_data['data'][0]['game_name'])
    else:
        return False
        # print(streamer_name + ' is not live')

