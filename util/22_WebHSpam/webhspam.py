import requests
import time
from colorama import Fore
import threading
from util.plugins.commun import * 

def webhookspam():
    setTitle("WebHook Spammer")
    clear()
    webhspamtitle()
    print(f"{y}[{w}+{y}]{w} Enter the WebHook you want to spam ")
    webhook = input(f"{y}[{b}#{y}]{w} WebHook Link: ")
    try:
        requests.post(webhook, json={'content': ""})
    except:
        print(f"      {y}[{Fore.LIGHTRED_EX }!{y}]{w} Your WebHook is invalid !")
        time.sleep(2)
        clear()
        main()
    print(f"\n{y}[{w}+{y}]{w} Enter the message to spam ")
    message = input(f"{y}[{b}#{y}]{w} Message: ")
    print(f"\n{y}[{w}+{y}]{w} Amount of messages to send ")
    amount = int(input(f"{y}[{b}#{y}]{w} Amount: "))
    def spam():
        requests.post(webhook, json={'content': message})
    for x in range(amount):
        threading.Thread(target = spam).start()
    
    clear()
    webhspamtitle()
    print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Webhook has been correctly spammed")
    input(f"\n{y}[{b}#{y}]{w} Press ENTER to exit")
    main()

webhookspam()
