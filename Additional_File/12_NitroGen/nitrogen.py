import time
import os
from colorama import Fore
import random
import string
import ctypes
from discord_webhook import DiscordWebhook 
import requests


class NitroGen: 
    def __init__(self): 
        self.fileName = "temp/NitroCodes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Astraa")
        else: 
            print(f'\33]0;Nitro Generator and Checker - Made by Astraa\a', end='', flush=True) 

        nitrogen()
        print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Input How Many Codes to Generate and Check: """)
        num = int(input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Number of generation: """))

        print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Do you wish to use a discord webhook? - [If so type it here or press enter to ignore]""")
        url = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } WebHook: """)
        time.sleep(1)
        os.system('cls')
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
                print(f"{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Error : {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Astraa")
                print("")
            else: 
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Astraa\a', end='', flush=True)

        print(f"""\n
{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Results:\n
          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Valid: {len(valid)}
          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Invalid: {invalid}
          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Valid Codes: {', '.join(valid )}""")

        input(f"""\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to exit""")

    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print(f"{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Wait, Generating for you")

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
                    print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.GREEN}VALID NITRO{Fore.WHITE} : {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"@everyone | A valid Nitro has been found => {nitro}"
                        ).execute()
                    else:
                        break
                else:
                    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}INVALID NITRO{Fore.WHITE} : {nitro} ")
                    invalid += 1

        return {"valid" : valid, "invalid" : invalid}

    def quickChecker(self, nitro, notify = None):

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.GREEN}VALID NITRO{Fore.WHITE} : {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("temp/NitroCodes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"@everyone | A valid Nitro has been found => {nitro}"
                ).execute()

            return True

        else:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}INVALID NITRO{Fore.WHITE} : {nitro}", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()