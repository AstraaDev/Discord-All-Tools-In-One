import requests
import time
from colorama import Fore
import os
import ctypes

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("WebHook Spammer - Made by Astraa")
    webhookspam()
    print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Webhooks url for spam: """)
    webhook = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } WebHooks: """)
    print(f"""\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Message to spam: """)
    message = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Message: """)
    print(f"""\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Amount of time for the attack (s):: """)
    timer = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Amount: """)
    input(f"""\n\n\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to Valid""")

    try:
        timeout = time.time() + 1 * float(timer) + 2

        while time.time() < timeout:
            response = requests.post(
                webhook,
                json = {"content" : message},
                params = {'wait' : True}
            )
            os.system('cls')
            time.sleep(1)
            if response.status_code == 204 or response.status_code == 200:
                print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Message sent""")
            elif response.status_code == 429:
                print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Rate limited ({response.json()['retry_after']}ms)""")
                time.sleep(response.json()["retry_after"] / 1000)
            else:
                print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Error code: {response.status_code}""")
    except:
        print(f"""      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Your request is invalid !""")
        time.sleep(2)
        os.system('cls')
        exit(0)
    
main()