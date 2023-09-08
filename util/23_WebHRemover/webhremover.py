import os
import requests
from colorama import Fore
from util.plugins.commun import * 

setTitle("WebHook Remover")
clear()
webhremovertitle()

def webhooksremover():
    try:
        print(f"{y}[{w}+{y}]{w} Enter the WebHook you want to delete ")
        webhook = input(f"""{y}[{b}#{y}]{w} WebHook Link: """)
        requests.delete(webhook.rstrip())
        print(f"\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Webhook has been deleted")
        input(f"\n{y}[{b}#{y}]{w} Press ENTER to exit")
        main()
    except:
        print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} Webhook could not be deleted")
        input(f"\n{y}[{b}#{y}]{w} Press ENTER to exit")
        main()
          
webhooksremover()
