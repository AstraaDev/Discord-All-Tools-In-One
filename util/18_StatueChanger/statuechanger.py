import os, requests, os.path
from colorama import Fore
from util.plugins.commun import * 

setTitle("Statue Changer")
clear()
statuechangertitle()
print(f"""{y}[{w}+{y}]{w} Enter your token""")
usertoken = str(input(f"""{y}[{b}#{y}]{w} Token: """))
print(f"""\n{y}[{w}+{y}]{w} Choose Custom Status""")
status = input(f"""{y}[{b}#{y}]{w} Status: """)

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

CustomStatus = {"custom_status": {"text": status}}
try:
    r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=getheaders(usertoken), json=CustomStatus)
    print(f"""\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Status changed to "{status}" """)
except Exception as e:
    print(f"\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error: {e}")

input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
main()