import time
import os
import requests
from itertools import cycle
from colorama import Fore

def cyclecolortheme():
    os.system('cls')
    cyclecolorthemetitle()
    print(f"""{y}[{w}+{y}]{w} Enter the token of the account you want to Cycle Color theme : """)
    token = input(f"""{y}[{b}#{y}]{w} Token: """)

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        print(f"""\n{y}[{w}+{y}]{w} Enter the number of cycles : """)
        amount = int(input(f"""{y}[{b}#{y}]{w} Amount: """))
        print()
        modes = cycle(["light", "dark"])
        os.system('cls')
        for i in range(amount):
            print(f"""{y}[{Fore.LIGHTGREEN_EX }{i+1}{y}]{w} Theme Color has been changed""")
            time.sleep(0.12)
            setting = {'theme': next(modes)}
            requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
        os.system('cls')
        cyclecolorthemetitle()
        print(f"""{y}[{b}#{y}]{w} Finished Trolling""")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
        main()
    else:
      print(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} Invalid token""")
      input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
      main()
          
cyclecolortheme()
