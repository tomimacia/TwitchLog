import pyautogui as pt
from isOnline import isLive
import moveclick as mc
import datetime

streamersMap = ['roshtein', 'xposed', 'yassuo',
                'VonDice', 'DeuceAce', 'FrankDimes']
connectedStreamers = []
dcStreamers = []
now = datetime.datetime.now()
file = open("data.txt", "a")
for streamer in streamersMap:
    if isLive(streamer):
        connectedStreamers.append(streamer)
    else:
        dcStreamers.append(streamer)
# cambiar las png de imagenesC

if(pt.locateOnScreen('imagenesC/chromesessionbar.png') is None):
    mc.locateAndClick('imagenesC/chromeLogo.png')


def closeDcTabs():
    for streamer in dcStreamers:
        while(pt.locateOnScreen(f'imagenesC/{streamer}/tab.png') or pt.locateOnScreen(f'imagenesC/{streamer}/tab2.png')):
            if(pt.locateOnScreen(f'imagenesC/{streamer}/tab.png')):
                mc.locateAndClick(f'imagenesC/{streamer}/tab.png')
                mc.closeTab()
            else:
                mc.locateAndClick(f'imagenesC/{streamer}/tab2.png')
                mc.closeTab()


def checkLiveStreaming():
    for streamer in connectedStreamers:
        if(pt.locateOnScreen(f'imagenesC/{streamer}/tab.png') or pt.locateOnScreen(f'imagenesC/{streamer}/tab2.png')):
            continue
        else:
            mc.locateAndClick('imagenesC/addTab.png')
            pt.typewrite(f'https://www.twitch.tv/{streamer}', interval=0.15)
            pt.press('enter')

    closeDcTabs()


checkLiveStreaming()
file.write('Time: ' + now.strftime('%H:%M:%S\n'))
file.write('Los streamers conectados son: ' + str(connectedStreamers)+"\n")
file.write('Los streamers desconectados son: ' + str(dcStreamers)+"\n\n")
mc.minimizar()
