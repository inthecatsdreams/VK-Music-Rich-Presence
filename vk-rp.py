from bs4 import BeautifulSoup
import requests
from pypresence import Presence



def html_bs(username):
    url = f"https://vk.com/{username}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    xd = soup.find("div", {"class": "pp_status"})
    status = None 
    if xd != None:
        status = xd.text
    else:
        status = None
    
    return status


def prettify_status(status):
    status_arr = status.split("—")
    return status_arr

app_id = "833702633431629904"
RPC = Presence(app_id)  # Initialize the Presence class
RPC.connect() 

while True:

    artist = None
    song_name = None
    username = "inthecatsdreams"
    discord_status = ""
    status_text = html_bs(username)

    if  status_text != None:
        artist = prettify_status(status_text)[0]
        song_name = prettify_status(status_text)[1]
        RPC.update(large_image="logo", large_text=f"Listening to:", small_text=f"{song_name} by {artist}", details=song_name, state=artist)

    else:
        discord_status = "Nothing is playing"
        RPC.update(large_image="logo", large_text=discord_status, small_text=discord_status, details="Playback is paused", state=discord_status)

    



