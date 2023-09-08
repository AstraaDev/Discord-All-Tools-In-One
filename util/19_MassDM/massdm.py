import requests
import threading
from colorama import Fore
from util.plugins.commun import setTitle, getheaders

setTitle("Mass DM")
clear()
massdmtitle()

def MassDM(token, channels, Message):
    for channel in channels:
        for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
            try:
                setTitle(f"Messaging {user}")
                requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers={'Authorization': token}, data={"content": f"{Message}"})
                print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Messaged: {user}")
            except Exception as e:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}")

print(f"{y}[{w}+{y}]{w} Enter the token of the account you want to Spam")
token = input(f"{y}[{b}#{y}]{w} Token: ")
validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
if validityTest.status_code != 200:
    print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} Invalid token")
    input(f"\n{y}[{b}#{y}]{w} Press ENTER to exit")
    main()
print(f"\n{y}[{w}+{y}]{w} Message that will be sent to every friend")
message = str(input(f"{y}[{b}#{y}]{w} Message: "))
clear()
processes = []

global channelIds
channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
if not channelIds:
    print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This guy is lonely, he aint got no dm's...")
    input(f"\n{y}[{b}#{y}]{w} Press enter to continue")
    main()
for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
    t = threading.Thread(target=MassDM, args=(token, channel, message))
    t.start()
    processes.append(t)
for process in processes:
    process.join()
input(f"\n{y}[{b}#{y}]{w} Press enter to continue")
main()
