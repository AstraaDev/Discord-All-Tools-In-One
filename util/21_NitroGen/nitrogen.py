import time
import os
from colorama import Fore
import random
import string
import ctypes
import requests
from util.plugins.commun import * 

def main(): 
    setTitle("Nitro Generator and Checker")
    clear()
    nitrogentitle()
    print(f"{y}[{w}#{y}]{w} Input How Many Codes to Generate and Check")
    num = int(input(f"""{y}[{b}#{y}]{w} Number of generation: """))
    print(f"\n{y}[{w}+{y}]{w} Do you wish to use a discord webhook? - [If so type it here or press enter to ignore]")
    url = input(f"{y}[{b}#{y}]{w} WebHook: ")
    webhook = url if url != "" else None
    valid = [] 
    invalid = 0 
    time.sleep(1)
    clear()

    for i in range(num): 
        try:
            code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 16))
            url = f"https://discord.gift/{code}"
            response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if response.status_code == 200:
                print(f"{w}[{Fore.GREEN}!{w}] {Fore.GREEN}VALID NITRO{w} : {url}")
                try:
                    requests.post(webhook, json={'content': url})
                except:
                    pass
                valid.append(url)
                with open("output/NitroCodes.txt", "w") as file:
                    file.write(url)
            elif response.status_code == 429:
                print(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} Rate limited, please wait {response.json()['retry_after']/1000} s")
                time.sleep(int(response.json()['retry_after'])/1000)
            else:
                print(f"{w}[{Fore.RED}!{w}] {Fore.RED}INVALID NITRO{w} : {url}")
                invalid += 1
        except Exception as e:
            print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error : {url} {e}")
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Astraa")
    print(f"""\n
{y}[{b}+{y}]{w} Results:
      {y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Valid: {len(valid)}
      {y}[{Fore.LIGHTRED_EX }!{y}]{w} Invalid: {invalid}
      {y}[{w}!{y}]{w} Valid Codes: {', '.join(valid )}""")
    input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    main()

main()
