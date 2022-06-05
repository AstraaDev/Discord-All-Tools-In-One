import time, os, requests, random, os.path
from colorama import Fore
from util.plugins.commun import * 

def settingstheme():
    setTitle("Settings Changer")
    clear()
    settingscyclertitle()

    print(f"""{y}[{Fore.LIGHTBLUE_EX }#{y}]{w} You can change:\n          {y}[{w}1{y}]{w} Statue\n          {y}[{w}2{y}]{w} Color Theme\n          {y}[{w}3{y}]{w} Language\n\n""")
    choice = input(f"""{y}[{Fore.LIGHTBLUE_EX }#{y}]{w} Setting to change: """)

    if choice == "1":
        print(f"\n{y}[{w}+{y}]{w} Enter the token of the account with which you want to cycle the statue")
        token = input(f"{y}[{b}#{y}]{w} Token: ")
        print(f"\n{y}[{w}+{y}]{w} How many statues do you want to cycle (max 4)")
        statue_number = int(input(f"{y}[{b}#{y}]{w} Number: "))
        print(f"\n{y}[{w}+{y}]{w} Time between each change in seconds (Recommended time: 5)")
        times = int(input(f"{y}[{b}#{y}]{w} Time : "))
        print("\n")
        statues = []

        headers = {'Authorization': token, 'Content-Type': 'application/json'}

        if statue_number >= 1 and statue_number <= 4:
            for loop in range(0, statue_number):
                print(f"""{y}[{w}+{y}]{w} Choose Custom Status #{loop+1}""")
                choice = str(input(f"""{y}[{b}#{y}]{w} Status #{loop+1}: """))
                statues.append(choice)
        else:
            print(f"""\n{y}[{w}+{y}]{w} Invalid number of statues""")
            input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()

        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to start""")
        clear()
        while True:
            for i in range(len(statues)):
                CustomStatus = {"custom_status": {"text": statues[i]}}
                try:
                    r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
                    print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Status changed to "{statues[i]}" """)
                    i += 1
                    time.sleep(times)
                except Exception as e:
                    print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error: {e}")
                    time.sleep(times)

    elif choice == "2":
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
    elif choice == "3":
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
