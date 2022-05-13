import requests
import random
from time import sleep
from colorama import Fore

from util.plugins.commun import setTitle, getheaders, proxy

def selector(token, users):
    clear()
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies=proxy(), headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Created groupchat")
            elif response.status_code == 429:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Created groupchat")
            elif response.status_code == 429:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    main()

groupspamtitle()
print(f"""{y}[{w}+{y}]{w} Enter the token of the account you want to Spam""")
token = input(f"""{y}[{b}#{y}]{w} Token: """)

print(f'\n{y}[{w}+{y}]{w} Do you want to choose user(s) yourself to groupchat spam or do you want to select randoms?')
print(f'''
{y}[{w}01{y}]{w} choose user(s) yourself
{y}[{w}02{y}]{w} randomize the users
                    ''')
secondchoice = int(input(
    f'{y}[{b}#{y}]{w} Choice: '))

if secondchoice not in [1, 2]:
    input(f'{y}[{Fore.LIGHTRED_EX}!{y}]{w} Invalid Second Choice')
    main()

#if they choose to import the users manually
if secondchoice == 1:
    setTitle(f"Creating groupchats")
    #if they choose specific users
    print(f'\n{y}[{w}+{y}]{w} Input the users you want to create a groupchat with (separate by , id,id2,id3)')
    recipients = input(f'{y}[{b}#{y}]{w} Users ID: ')
    user = recipients.split(',')
    if "," not in recipients:
        input(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} You didn't have any commas (,) format is id,id2,id3")
        main()
    input(f"\n\n\n{y}[{b}#{y}]{w} Press enter to continue (\"ctrl + c\" at anytime to stop)")
    selector(token, user)

#if they choose to randomize the selection
elif secondchoice == 2:
    setTitle(f"Creating groupchats")
    IDs = []
    #Get all users to spam groupchats with
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        IDs.append(friend['id'])
    input(f"\n{y}[{b}#{y}]{w} Press enter to continue (\"ctrl + c\" at anytime to stop)")
    randomizer(token, IDs)