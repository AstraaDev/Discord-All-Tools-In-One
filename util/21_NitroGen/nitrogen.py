import time
import os
from colorama import Fore
import random
import string
import ctypes
from discord_webhook import DiscordWebhook 
import requests
from util.plugins.commun import * 


class NitroGen: 
    def __init__(self): 
        self.fileName = "temp/NitroCodes.txt" 

    def main(self): 
        setTitle("Nitro Generator and Checker")
        clear() 
        if os.name == "nt":
            print("")

        clear()
        nitrogentitle()
        print(f"""{y}[{w}#{y}]{w} Input How Many Codes to Generate and Check""")
        num = int(input(f"""{y}[{b}#{y}]{w} Number of generation: """))

        print(f"""\n{y}[{w}+{y}]{w} Do you wish to use a discord webhook? - [If so type it here or press enter to ignore]""")
        url = input(f"""{y}[{b}#{y}]{w} WebHook: """)
        time.sleep(1)
        clear()
        webhook = url if url != "" else None 
        valid = [] 
        invalid = 0 

        for i in range(num): 
            try: 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error : {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Astraa")
                print("")

        print(f"""\n
{y}[{b}+{y}]{w} Results:
          {y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Valid: {len(valid)}
          {y}[{Fore.LIGHTRED_EX }!{y}]{w} Invalid: {invalid}
          {y}[{w}!{y}]{w} Valid Codes: {', '.join(valid )}""")

        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
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

                file.write(f"https://discord.gift/{code}\n")

            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url)

                if response.status_code == 200:
                    print(f"{w}[{Fore.GREEN}!{w}] {Fore.GREEN}VALID NITRO{w} : {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"@everyone | A valid Nitro has been found => {nitro}"
                        ).execute()
                    else:
                        break
                else:
                    print(f"{w}[{Fore.RED}!{w}] {Fore.RED}INVALID NITRO{w} : {nitro} ")
                    invalid += 1

        return {"valid" : valid, "invalid" : invalid}

    def quickChecker(self, nitro, notify = None):

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"{w}[{Fore.GREEN}!{w}] {Fore.GREEN}VALID NITRO{w} : {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("temp/NitroCodes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"@everyone | A valid Nitro has been found => {nitro}"
                ).execute()

            return True

        else:
            print(f"{w}[{Fore.RED}!{w}] {Fore.RED}INVALID NITRO{w} : {nitro}", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()